from dash import Input, Output, State, ctx
from dash.exceptions import PreventUpdate

from app import app,server

import pandas as pd
import numpy as np
from datetime import date


# Functions
from components.functions import plot_map, fields_loading, geo_loading, experts_loading, location_options_management, geo_to_dropdown, ok_to_save, experts_filename



# Gestion des champs de Identité

@app.callback(
    Output("abstract_identity", "children"),
    Output("abstract_identity", "style"),
    
    Output("input_compagny_name","valid"),
    Output("input_last_name","valid"),
    
    Output("input_compagny_name","value"),   
    Output("input_last_name","value"), 
    Output("input_first_name","value"),
    
    Input("cleaning_confirmation_modal","is_open"),
    Input("creating_confirmation_modal","is_open"),
    
    Input("input_compagny_name","value"),   
    Input("input_last_name","value"), 
    Input("input_first_name","value"), 
    )

def identity_management(to_supp_1, to_supp_2, compagny_name, last_name, first_name):
    
    style = {"color" : "red", "marginLeft" : "20px"}

    if to_supp_1 == True or to_supp_2 == True:
        
        identity = []
        
        compagny_name = ""
        last_name = ""
        first_name = ""
        
        input_compagny_name_valid = False
        input_last_name_valid = False
        
        return identity, style, input_compagny_name_valid, input_last_name_valid, compagny_name, last_name, first_name
    
    else:
        
        identity = ["", "", ""]
        
        if str(compagny_name).strip() != "": 
            
            identity[0] = str(compagny_name) + " - "
            input_compagny_name_valid = True
        else:
            input_compagny_name_valid = False
            
        if str(last_name).strip() != "":
            
            identity[1] = str(last_name) + " - "
            input_last_name_valid = True
        else:
            input_last_name_valid = False

        if str(first_name).strip() != "":
            
            identity[2] = str(first_name)
            
    
        return identity, style, input_compagny_name_valid, input_last_name_valid, compagny_name, last_name, first_name



# Gestion des champs de Contact

@app.callback(
    Output("abstract_contact", "children"),
    Output("abstract_contact", "style"),
    
    Output("input_email","valid"),
    Output("input_phone_1","valid"),
    Output("input_phone_2","valid"),
    
    Output("input_email","value"),   
    Output("input_phone_1","value"), 
    Output("input_phone_2","value"),
    Output("input_website","value"),
    
    Input("cleaning_confirmation_modal","is_open"),
    Input("creating_confirmation_modal","is_open"),
    
    Input("input_email","value"),   
    Input("input_phone_1","value"), 
    Input("input_phone_2","value"),
    Input("input_website","value")
    )

def contact_management(to_supp_1, to_supp_2, email, phone_1, phone_2, website):
    
    style = {"color" : "red", "marginLeft" : "20px"}
    
    contact = [email, phone_1, phone_2, website]

    if to_supp_1 == True or to_supp_2 == True:
        
        contact = []
    
        email = ""
        phone_1 = ""
        phone_2 = ""
        website = ""
        
        input_email_valid = False
        input_phone_1_valid = False
        input_phone_2_valid = False
        
        return contact, style, input_email_valid, input_phone_1_valid, input_phone_2_valid, email, phone_1, phone_2, website
    
    else:
        
        contact = ["", "", "", ""]
        
        if str(email).strip() != "": 
        
            contact[0] = str(email) + " - "
            input_email_valid = True
        else:
            input_email_valid = False
        
        if str(phone_1).strip() != "": 
            
            contact[1] = str(phone_1) + " - "
            input_phone_1_valid = True
        else:
            input_phone_1_valid = False
            
        if str(phone_2).strip() != "": 
            
            contact[2] = str(phone_2) + " - "
            input_phone_2_valid = True
        else:
            input_phone_2_valid = False

        if str(website).strip() != "": 
            
            contact[3] = str(website)
            
    
        return contact, style, input_email_valid, input_phone_1_valid, input_phone_2_valid, email, phone_1, phone_2, website



# Gestion des champs de Localisation

@app.callback(
    Output("abstract_location", "children"),
    Output("abstract_location", "style"),
    
    Output("input_city_name","valid"),
    
    Output("input_city_zip_code","value"),   
    Output("input_city_name","value"), 
    Output("input_county_name","value"),
    Output("input_region_name","value"),
    
    Output("input_region_name", "options"),
    Output("input_county_name", "options"),
    Output("input_city_name", "options"),
    
    Input("cleaning_confirmation_modal","is_open"),
    Input("creating_confirmation_modal","is_open"),
    
    Input("input_city_zip_code","value"),   
    Input("input_city_name","value"), 
    Input("input_county_name","value"),
    Input("input_region_name","value"),
    
    State("input_region_name", "options"),
    State("input_county_name", "options"),
    State("input_city_name", "options")
    )

def location_management(to_supp_1, to_supp_2, city_zip_code, city_name, county_name, region_name, regions_list, counties_list, cities_list):
    
    style = {"color" : "red", "marginLeft" : "20px"}

    geo = geo_loading()
       
    input_city_name_valid = False

    if to_supp_1 == True or to_supp_2 == True:
        
        location = []
        
        region_name = ""
        county_name = ""
        city_name = ""
        city_zip_code = ""
        
        cities_list = ""
        counties_list = [{"label":c, "value":c} for c in sorted(list(geo.county_name.unique()))]
        regions_list = [{"label":r, "value":r} for r in sorted(list(geo.region_name.unique()))]
        
        return location, style, input_city_name_valid, city_zip_code, city_name, county_name, region_name, regions_list, counties_list, cities_list
    
    else:
        
    # MàJ de l'abstract  et des dropdowns 
    
        if ctx.triggered_id=="input_region_name":       # 1) Région est modifié
            
            regions_list, counties_list, cities_list = location_options_management("region_name",region_name, regions_list, counties_list, cities_list)
                
            county_name = ""
            city_zip_code = ""
            city_name = ""
            
            location = [str(city_zip_code), str(city_name), str(county_name), str(region_name)]
            
            input_city_name_valid = False
                  
                  
        elif ctx.triggered_id=="input_county_name":     # 2) Département est modifié
              
            regions_list, counties_list, cities_list = location_options_management("county_name",county_name, regions_list, counties_list, cities_list)
              
            region_name = geo.loc[geo.county_name == county_name, "region_name"].unique()[0]
            city_zip_code = ""
            city_name = ""
              
            location = [str(city_zip_code), str(city_name), str(county_name) + " - ", str(region_name)]
            
            input_city_name_valid = False
              
        elif ctx.triggered_id=="input_city_name":       # 3) ville est modifiée

            if region_name != "" and county_name == "":     # Cas 1 : on connait la région mais pas le département
                
                county_name = geo.loc[(geo.region_name == region_name) & (geo.city_name == city_name), "county_name"].unique()[0]    

                regions_list, counties_list, cities_list = location_options_management("region_name",region_name, regions_list, counties_list, cities_list)
                regions_list, counties_list, cities_list = location_options_management("county_name",county_name, regions_list, counties_list, cities_list)
                # A optimiser...
            
            # Cas 2 : on connait la région et le département   ---   Donc les listes sont OK ! Rien à faire de plus, on enchaine.

            city_zip_code = geo.loc[(geo.county_name == county_name) & (geo.city_name == city_name), "city_zip_code"].unique()[0]
                
            location = [str(city_zip_code) + " - ", str(city_name) + " - ", str(county_name) + " - ", str(region_name)]
                
            input_city_name_valid = True
                
              
        elif ctx.triggered_id=="input_city_zip_code":       # 3) zip_code est modifié   >   On modifie tout. Mais attention aux communes ayant le même zip_code
                  
            regions_list = geo_to_dropdown(geo, "city_zip_code", city_zip_code.strip(), "region_name")
            counties_list = geo_to_dropdown(geo, "city_zip_code", city_zip_code.strip(), "county_name")  
            cities_list = geo_to_dropdown(geo, "city_zip_code", city_zip_code.strip(), "city_name")
            
            location = ["", "", "", ""]
                  
            if len(regions_list) == 1:
                region_name = regions_list[0]['value']
                location[3] = str(region_name)
            else:
                location[3] = ""    
               
            if len(counties_list) == 1:
                county_name = counties_list[0]['value']
                location[2] = str(county_name) + " - "
            else:
                location[2] = "" 
               
            if len(cities_list) == 1:
                city_name = cities_list[0]['value']
                location[1] = str(city_name) + " - "
                input_city_name_valid = True
            else:
                location[1] = ""
                input_city_name_valid = False
               
            location[0] = str(city_zip_code) + " - "
            
        else:
            location=[]
    
    return location, style, input_city_name_valid, city_zip_code, city_name, county_name, region_name, regions_list, counties_list, cities_list   


# Gestion des champs de Activité

@app.callback(
    Output("abstract_activity", "children"),
    Output("abstract_activity", "style"),
       
    Output("input_activity_field","value"),   
    Output("input_activity_reach","value"), 
    Output("input_activity_remote","value"),
    
    Input("cleaning_confirmation_modal","is_open"),
    Input("creating_confirmation_modal","is_open"),
    
    Input("input_activity_field","value"),   
    Input("input_activity_reach","value"), 
    Input("input_activity_remote","value")
    )

def activity_management(to_supp_1, to_supp_2, activity_field, activity_reach, activity_remote):
    
    style = {"color" : "red", "marginLeft" : "20px"}
    
    if to_supp_1 == True or to_supp_2 == True:
        
        activity = ["", "10 km - ", "Pas de télétravail"]
    
        activity_field = []
        activity_reach = "10"
        activity_remote = []
        
        return activity, style, activity_field, activity_reach, activity_remote
    
    else:
        
        activity = ["", "10 km - ", "Pas de télétravail"]
        
        if activity_field != []:
            tempo = ""
            for i in range(len(activity_field)):
                tempo += str(activity_field[i]) + ', ' 
            activity[0] = str(tempo) + " - "


        if str(activity_reach) != "" and str(activity_reach) != "0":
            
            activity[1] = str(activity_reach) + " km - "
        else:
            activity[1] = "Ne se déplace pas - "


        if activity_remote != [] and  activity_remote != "":
            
            activity[2] = "Télétravail OK"
        else:
            activity[2] = "Pas de télétravail"
    
    
        return activity, style, activity_field, activity_reach, activity_remote



# Gestion des champs de Vérification

@app.callback(
    Output("abstract_verification", "children"),
    Output("abstract_verification", "style"),
       
    Output("input_last_contact","disabled"),
      
    Output("input_check","value"), 
    Output("input_last_contact","date"),
    
    Input("cleaning_confirmation_modal","is_open"),
    Input("creating_confirmation_modal","is_open"),
    
    Input("input_check","value"), 
    Input("input_last_contact","date")
    )

def verification_management(to_supp_1, to_supp_2, check, last_contact):
    
    style = {"color" : "red", "marginLeft" : "20px"}

    if to_supp_1 == True or to_supp_2 == True:
        
        verification = ["", ""]
    
        date_is_disabled = True
    
        check = []
        last_contact = None
        
        return verification, style,  date_is_disabled, check, last_contact
    
    else:
        
        verification = ["", ""]
           
        if check != [] and  check != "":
            
            verification[0] = "Vérifié - "
            date_is_disabled = False
            
        else:
            
            verification[0] = "Pas vérifié - "
            date_is_disabled = True
            last_contact = None


        if ctx.triggered_id == "input_check" and check != [] and  check != "" :
            last_contact = pd.to_datetime(date.today()).strftime("%Y-%m-%d")
            verification[1] = str(last_contact)


        if not last_contact is None:
            
            verification[1] = str(last_contact)
            
        else:
            
            verification[1] = ""


        return verification, style,   date_is_disabled,  check, last_contact




# Gestion des champs de Progression du remplissage

@app.callback(
    Output("form_progress","value"),
    Output("form_progress","label"),
    
    Input("input_compagny_name","value"),   
    Input("input_last_name","value"), 
    Input("input_email","value"),   
    Input("input_phone_1","value"), 
    Input("input_phone_2","value"),
    Input("input_city_name","value"),
    Input("input_activity_field","value"), 
    )

def progression_management(compagny_name, last_name, email, phone_1, phone_2, city_name, activity_field):

    progress_rate = 0
    progress_label = ""

    if compagny_name or last_name :
        progress_rate = progress_rate + 25
        
    if email or phone_1 or phone_2 :
        progress_rate = progress_rate + 25
        
    if city_name :
        progress_rate = progress_rate + 25
       
    if activity_field :
        progress_rate = progress_rate + 25

    progress_label = str(progress_rate) + "%"

    return progress_rate, progress_label



# Gestion de la carte de localisation  

@app.callback(
    Output("form_graph_location","figure"),
    
    Input("input_region_name", "value"),
    Input("input_county_name", "value"),
    Input("input_city_name", "value"),
    )
def maj_form_graph(region, county, city):
    
    geo = geo_loading()
    
    df = geo.loc[geo.city_name == "Chartres"]    # ... et pourquoi pas !?  --> plot_map() ne fonctionne pas si pas de data en entrée
    
    if region:
        df = geo.loc[geo.region_name == region]
        
    if county:
        df = geo.loc[geo.county_name == county]
        
    if city:
        df = geo.loc[(geo.city_name == city) & (geo.county_name == county) & (geo.region_name == region)]   
             
    fig = plot_map(df)
    return fig



# Activation du bouton de validation

@app.callback(
    Output("creation_form_valid_btn", "disabled"),
    Input("form_progress","value"),
    )
def maj_abstract(value):
    if value == 100:
        return False
    else:
        return True



# Gestion du Message de demande de confirmation nettoyage

@app.callback(
    Output("cleaning_modal", "is_open"),
    
    Input("creation_form_delete_btn","n_clicks"),
    Input("cleaning_cancel","n_clicks"),
    Input("cleaning_valid","n_clicks"),
    State("cleaning_modal", "is_open"),
    )
def cleaning_modal_management(n1, n2, n3, is_open):
    if n1>0 or n2>0 or n3>0:
        return not is_open
    else:
        return is_open



# Gestion du Message information nettoyage effectif

@app.callback(
    Output("cleaning_confirmation_modal","is_open"),
    
    Input("cleaning_valid", "n_clicks"),
    State("cleaning_confirmation_modal","is_open"),
    )
def cleaning_valid_button_management(n3, is_open):
    if n3>0:
        return not is_open
    else: 
        return is_open



# Gestion du Message de demande de confirmation de la création

@app.callback(
    Output("creation_modal", "is_open"),
    
    Input("creation_form_valid_btn","n_clicks"),
    Input("creation_cancel","n_clicks"),
    Input("creation_valid","n_clicks"),
    State("creation_modal", "is_open"),
    )
def creation_modal_management(n1, n2, n3, is_open):
    if n1>0 or n2>0 or n3>0:
        return not is_open
    else:
        return is_open


# Gestion du Message information création effectif

@app.callback(
    Output("creating_confirmation_modal","is_open"),
    
    Input("creation_valid", "n_clicks"),
    State("creating_confirmation_modal","is_open"),
    
    )
def creating_valid_button_management(n3, is_open):
    if n3>0:
        return not is_open
    else: 
        return is_open




# Création des lignes 

@app.callback(
    Output("form_provider", "active_item"),
    
    Input("creating_confirmation_modal","is_open"),
    Input("cleaning_confirmation_modal","is_open"),
    
    State("input_compagny_name","value"),   
    State("input_last_name","value"), 
    State("input_first_name","value"),
    
    State("input_email","value"),   
    State("input_phone_1","value"), 
    State("input_phone_2","value"),
    State("input_website","value"),
    
    State("input_city_name","value"), 
    State("input_county_name","value"),
    State("input_region_name","value"),
    
    State("input_activity_field","value"),   
    State("input_activity_reach","value"), 
    State("input_activity_remote","value"),
    
    State("input_check","value"), 
    State("input_last_contact","date"),
    
    )
def expert_creation(to_create_1, to_create_2, input_compagny_name, input_last_name, input_first_name, 
                    input_email, input_phone_1, input_phone_2, input_website, 
                    input_city_name, input_county_name, input_region_name, 
                    input_activity_field, input_activity_reach, input_activity_remote, 
                    input_check, input_last_contact):
    
    fields = fields_loading()
    geo = geo_loading()
    experts = experts_loading()
    

    if to_create_1 == True :
               
        data=[]
        nL = len(input_activity_field)

        # recodage de ceraines données

        geo_id = int(geo.loc[(geo.city_name == input_city_name) & (geo.county_name == input_county_name) & (geo.region_name == input_region_name), "id"]) 

        if input_activity_remote == [1]:
            input_activity_remote = 1
        else:
            input_activity_remote = 0
            
        if input_check == [1]:
            input_check = 1
        else:
            input_check = 0
            
        if not input_last_contact is None:
            input_last_contact = pd.to_datetime(input_last_contact)
        else :
            input_last_contact = pd.NaT

        data = {
                "id" : [max(experts.id)+i+1 for i in range(nL)],
                "created_at" : [pd.to_datetime(date.today()) for i in range(nL)],
                "updated_at" : [pd.to_datetime(date.today()) for i in range(nL)],
                "deleted_at" : [np.nan for i in range(nL)],
                
                "first_name" : [str(input_first_name) for i in range(nL)],
                "last_name" : [str(input_last_name) for i in range(nL)],
                "compagny_name" : [str(input_compagny_name) for i in range(nL)],
                "email" : [str(input_email) for i in range(nL)],
                "phone_1" : [str(input_phone_1) for i in range(nL)],
                "phone_2" : [str(input_phone_2) for i in range(nL)],
                "website" : [str(input_website) for i in range(nL)],

                "geo_id" : [int(geo_id) for i in range(nL)],
                
                "reach" : [int(input_activity_reach) for i in range(nL)],
                "remote_work" : [int(input_activity_remote) for i in range(nL)],
                
                "field_id" : [int(fields.loc[fields.title == input_activity_field[i], "id"]) for i in range(nL)],
                
                "check" : [input_check for i in range(nL)],
                "last_contact" : [input_last_contact for i in range(nL)],      
        }
 
        df = pd.DataFrame(data, columns=experts.columns)

        experts = pd.concat([experts, df])
        
        file ="data/"+ experts_filename
        ok_to_save(file, experts)

        
        return "form_identity"

    elif to_create_2 == True:
        
        return "form_identity"
    
    else :  
        
        raise PreventUpdate
    