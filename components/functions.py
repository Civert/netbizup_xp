import werkzeug
import pandas as pd
import json
import plotly.express as px


experts_filename = "experts_test.csv"


# safe_file_path = werkzeug.utils.secure_filename(file)

def data_loading(directory, file_name):
    
    file = directory + file_name
    
    df = pd.read_csv(file, sep=";", dtype = "object")
    
    return df



def fields_loading():

    fields = data_loading("data/","fields.csv")

    fields = fields.astype({'id':"int64"})
    fields['created_at'] = pd.to_datetime(fields['created_at'])
    fields['updated_at'] = pd.to_datetime(fields['updated_at'])     

    return fields



def geo_loading():

    geo = data_loading("data/","geo.csv")
    
    geo = geo.astype({"id":"int64", 
                    "lat":"float64", 
                    "lon":"float64",
                    })
    geo['created_at'] = pd.to_datetime(geo['created_at'])
    geo['updated_at'] = pd.to_datetime(geo['updated_at'])

    # On supprime pour le moment, tous les DOM + Corse, car pas dans le scope !
    geo = geo.loc[(geo.region_name != "Corse") & (geo.region_name != "Guadeloupe") & (geo.region_name != "Martinique") & (geo.region_name != "La Réunion") & (geo.region_name != "Guyane") & (geo.region_name != "Mayotte")]

    return geo




def experts_loading():
    
    experts = data_loading("data/", experts_filename)
     
    experts = experts.astype({"id":"int64", 
                          "geo_id":"int64",  
                          "field_id":"int64", 
                         })
    experts['created_at'] = pd.to_datetime(experts['created_at'])
    experts['updated_at'] = pd.to_datetime(experts['updated_at'])
    experts['deleted_at'] = pd.to_datetime(experts['deleted_at'])
    experts['last_contact'] = pd.to_datetime(experts['last_contact'])
    
    return experts



def big_one_building():
     
    geo = geo_loading()
    fields = fields_loading()
    experts = experts_loading()
    experts = experts.loc[experts.deleted_at.isnull()]      # On garde les lignes "deleted_at" null
     
    df_geo = geo.loc[:,("id", "city_zip_code","city_name","county_name","region_name","lat","lon")]
    df_fields=fields.loc[:,("id", "title")]
    tempo = pd.merge(experts, df_fields, how="left", left_on="field_id", right_on="id")
    big_one = pd.merge(tempo, df_geo, how="left", left_on="geo_id", right_on="id")
    big_one = big_one.drop(columns = ["geo_id","field_id","id_y","id"])
    big_one.rename(columns={"id_x": "id","title": "field"}, inplace=True)
    big_one.loc[(big_one.check == "0") , "check"] = "Non"
    big_one.loc[big_one.check == "1", "check"] = "Oui"
    big_one.loc[(big_one.remote_work == "0") , "remote_work"] = "Non"
    big_one.loc[big_one.remote_work == "1", "check"] = "Oui"
    
    return big_one



def focus_to_plot():

    geo = geo_loading()
    fields = fields_loading()
    experts = experts_loading()
    experts = experts.loc[experts.deleted_at.isnull()]      # On garde les lignes "deleted_at" null

    df_geo = geo.loc[:,("id", "city_name", "lat", "lon")]
    df_fields=fields.loc[:,("id", "title")]
    df_experts=experts.loc[:,("id", "geo_id", "field_id")]

    tempo = pd.merge(df_experts, df_fields, how="left", left_on="field_id", right_on="id")
    focus = pd.merge(tempo, df_geo, how="left", left_on="geo_id", right_on="id")
    focus = focus.drop(columns = ["geo_id","field_id","id_y","id"])
    focus.rename(columns={"id_x": "id","title": "field"}, inplace=True)

    return focus


def kpi_to_dashboard():
    
    experts = experts_loading()
    experts = experts.loc[experts.deleted_at.isnull()]      # On garde les lignes "deleted_at" null

    # Calcul des KPI

    expert_identities = experts.loc[:,("last_name", "first_name", "compagny_name")]
    nb_experts = expert_identities.copy()
    nb_experts.drop_duplicates(inplace=True)
    kpi_nb_experts = len(nb_experts)

    nb_cities = experts.loc[:,("geo_id")]
    nb_cities.drop_duplicates(inplace=True)
    kpi_nb_cities = len(nb_cities)

    expert_identities["nb_fields"]=1
    nb_fields_by_expert = expert_identities.groupby(by=["last_name", "first_name", "compagny_name"],group_keys = False, as_index=False)["nb_fields"].sum()
    kpi_nb_fields_by_expert = round(nb_fields_by_expert["nb_fields"].mean(),2)
    
    return kpi_nb_experts, kpi_nb_cities, kpi_nb_fields_by_expert


def carte_choropleth(code_label, name_label):
      
    fields = fields_loading()
    geo = geo_loading()
    experts = experts_loading()
    experts = experts.loc[experts.deleted_at.isnull()]      # On garde les lignes "deleted_at" null
    
    df_geo = geo.loc[:,("id", code_label, name_label)]
    df_fields=fields.loc[:,("id", "title")]
    df_experts=experts.loc[:,("id", "geo_id", "field_id")]
    tempo = pd.merge(df_experts, df_fields, how="left", left_on="field_id", right_on="id")
    tempo["nb_expert"]=1 
    focus = pd.merge(tempo, df_geo, how="outer", left_on="geo_id", right_on="id")
   
    focus = focus.drop(columns = ["geo_id","field_id","id_y","id"])
    focus.rename(columns={"id_x": "id","title": "field"}, inplace=True)
    
    df = focus.groupby(by=[code_label, name_label],group_keys = True, as_index=False)["nb_expert"].sum()   
    
    if name_label == "region_name":
        with open('./data/regions.geojson') as fp:
            gjson = json.load(fp)
    elif name_label == "county_name":
        with open('./data/departements.geojson') as fp:
            gjson = json.load(fp)
        
    fig = px.choropleth(
                        df,
                        locations=code_label,
                        geojson=gjson,
                        featureidkey='properties.code',
                        hover_name=name_label,
                        #color_continuous_scale="Viridis",
                        color_continuous_scale="Oranges",
                        #color_discrete_sequence= px.colors.sequential.Oranges,
                        
                        color="nb_expert",
                        projection='gnomonic',
                        center={'lon':48.864716,'lat':2.349014},
                        labels={'nb_expert':"Nb d'experts"} 
                        )
    fig.update_geos(showcountries=False, showcoastlines=False, showland=False, fitbounds="locations", visible=False)
    fig.update_layout(margin={'l': 10, 'r': 10, 't': 30, 'b': 10})
    #fig.update_layout(height=00)
    fig.update_layout(plot_bgcolor='rgb(0,0,0)')

    return fig


# Visualiser les villes de France sélectionnées sur un fond de carte "open-street-map" - focus métropole 

def plot_map(df_geo):
    fig = px.scatter_mapbox(
                    data_frame=df_geo, 
                    lat="lat", 
                    lon="lon",  
                    hover_data=["city_name"], 
                    labels={'city_name':"Commune"}, 
                    #hover_name="CITY_NAME",
                    color_discrete_sequence=["orangered"], 
                    zoom=4.25, 
                    height=400, 
                    mapbox_style="open-street-map",
                    center=dict(
                        lat=47.083328,
                        lon=1.8
                    ),
                    #margin={"r":0,"t":0,"l":0,"b":0},
            )
    
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    
    return fig 


# Visualiser la couverture des communes par domaine

def plot_treemap():
    
    focus = focus_to_plot()
    
    field_geo = focus.loc[:,("field", "city_name")]
    field_geo["nb"]=1
    field_geo = field_geo.groupby(by=["field", "city_name"],group_keys = False, as_index=False)["nb"].sum()
        
    fig = px.treemap(
                field_geo, 
                path=["field", "city_name","nb"], 
                values="nb",
                color="nb",
                #hover_data=["field", "city_name"],
                color_continuous_scale='oranges'
                #color_continuous_midpoint=np.average(df['lifeExp'], weights=df['pop'])),
                )
    fig.update_traces(root_color="#585858")
    fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
    
    return fig



# Filtrer les données géographiques et en faire une liste exploitable pour une liste déroulante

def geo_to_dropdown(table, att_set, setpoint, att_focus):
    
    new_list = table.loc[table[att_set] == setpoint, att_focus]
    new_list = sorted(list(new_list.unique()))
    new_list = [{"label":n, "value":n} for n in new_list]
    
    return new_list

   


# Fonction de sauvegarde du DataFrame dans un fichier CSV encodé en "utf-8"

def ok_to_save(file_name, df):
    
    df.to_csv(file_name, sep=";", encoding="utf-8", index=False)




# Fonction de MàJ des options des champs de Location

def location_options_management(trigger, value, regions_list_old, counties_list_old, cities_list_old):
    
    geo = geo_loading()

    regions_list = [{"label":n, "value":n} for n in sorted(list(geo.region_name.unique()))]
    counties_list = [{"label":n, "value":n} for n in sorted(list(geo.county_name.unique()))]
    cities_list = ""
    
    if trigger == "region_name":
        
        counties_list = geo_to_dropdown(geo, "region_name", value, "county_name")
        cities_list = geo_to_dropdown(geo, "region_name", value, "city_name")
        
    elif trigger == "county_name":
        
        region_name = geo.loc[ (geo.county_name == value), "region_name"].unique()[0]
        counties_list = geo_to_dropdown(geo, "region_name", region_name, "county_name")
        cities_list = geo_to_dropdown(geo, "county_name", value, "city_name")
        
    elif trigger == "city_zip_code":
        
        try:
            region_name = geo.loc[ (geo.city_zip_code == value), "region_name"].unique()[0]
            counties_list = geo_to_dropdown(geo, "region_name", region_name, "county_name")
            
            county_name = geo.loc[ (geo.city_zip_code == value), "county_name"].unique()[0]
            cities_list = geo_to_dropdown(geo, "county_name", county_name, "city_name")
        except:
            pass
    
    else:
        
        regions_list = regions_list_old
        counties_list = counties_list_old
        cities_list = cities_list_old
    
    return regions_list, counties_list, cities_list
        
        