from dash import Input, Output, State, html, dash_table, ctx
import dash_bootstrap_components as dbc

from app import app,server

import pandas as pd
from datetime import date


# Functions
from components.functions import geo_to_dropdown, big_one_building, experts_loading, geo_loading, fields_loading, location_options_management, ok_to_save, experts_filename



# Gestion de la table dynamique du Module de Modification en fonction du Reset

@app.callback(
    Output("table_to_modify", "filter_query"),
    Output("table_to_modify", "hidden_columns"),
    Output("table_to_modify", "selected_rows"),
    Output("table_to_modify", "selected_row_ids"),
    Output("table_to_modify", "sort_by"),
    Output("table_to_modify", "data"),
    
    Output("table_to_modify", "page_current"),
    
    # Output("select_one_to_modify","n_clicks"),
    # Output("change_selection_cancel_btn", "n_clicks"),
    # Output("change_selection_valid_btn", "n_clicks"),
    
    Input('reset_table_to_modify','n_clicks'),
    Input("modification_confirmation_modal","is_open"),
    
    State("table_to_modify", "filter_query"),
    State("table_to_modify", "hidden_columns"),
    State("table_to_modify", "selected_rows"),
    State("table_to_modify", "selected_row_ids"),
    State("table_to_modify", "sort_by"),
    State("table_to_modify", "data"),
    State("table_to_modify", "page_current"),
    )

def table_to_delete_management(n, is_open, state_query, state_hidden, state_selected, state_ids_selected, state_sorting, data, page_current):
    
    hidden_columns_init=["id","created_at", "updated_at", "deleted_at", "city_zip_code", "region_name", "reach", "remote_work", "check", "last_contact", "lat", "lon"]
 
    df = big_one_building()
    
    
    if (ctx.triggered_id=="reset_table_to_modify" and n>0) or is_open == True :
    
        state_query = ""
        state_hidden = hidden_columns_init
        state_selected = []
        state_ids_selected = []
        state_sorting = []
        data = df.to_dict('records')
        page_current = 0
        
        # change_selection_cancel_btn = 0             ##   Pourquoi ??? je ne sais plus...
        # change_selection_valid_btn = 0              ##   Pourquoi ??? je ne sais plus...
        
    else:
         
        state_query = "" if state_query is None else state_query
        state_hidden = hidden_columns_init if state_hidden == hidden_columns_init else state_hidden
        state_selected = [] if state_selected is None else state_selected
        state_ids_selected = [] if state_ids_selected is None else state_ids_selected
        state_sorting = [] if state_sorting is None else state_sorting
        data = df.to_dict('records')
        page_current = 0
         
        # change_selection_cancel_btn = 0             ##   Pourquoi ??? je ne sais plus...
        # change_selection_valid_btn = 0              ##   Pourquoi ??? je ne sais plus...
        
    return state_query, state_hidden, state_selected, state_ids_selected, state_sorting, data, page_current



# MàJ du nombre de lignes sélectionnées

@app.callback(
    Output("kpi_rows_selected_to_modify","children"),
    Input("table_to_modify", "selected_row_ids"),
)
def kpi_selected_rows_to_modify(ids_selected):
    
    if not ids_selected is None:
        return str(len(ids_selected))
    else:
        return 0



# Gestion du Message de demande de confirmation de modification

@app.callback(
    Output("change_selection_modal", "is_open"),
    
    Input("select_one_to_modify","n_clicks"),
    Input("change_selection_cancel_btn", "n_clicks"),
    Input("change_selection_valid_btn", "n_clicks"),
    
    State("change_selection_modal", "is_open"),
    )
def change_selection_modal_management(n1, n2, n3, is_open):
    if n1>0 or n2>0 or n3>0:
        return not is_open
    else:
        return is_open


# Personnalisation du Message de sélection pour modification

@app.callback(
    Output("change_selection_verification_modal_body", "children"),
    Output("change_selection_valid_btn", "disabled"),
    
    Input("change_selection_modal","is_open"),
    State("table_to_modify", "selected_row_ids"),
    )
def removing_modal_customization(is_open, ids_selected):
    
    if is_open == False or len(ids_selected)==0:  
        
        new_body = "Cette action ne va rien modifier ! La sélection d'un expert est recquise."
        valid_is_disabled = True
        
    else:
        
        big_one = big_one_building()
        df = big_one.loc[:,("id","first_name", "last_name", "compagny_name")]
        df = df[df.id.isin(ids_selected)]
        
        df_expert_unique = df.loc[:,("first_name", "last_name", "compagny_name")]
        df_expert_unique.rename(columns={"first_name": "Prénom","last_name": "Nom","compagny_name": "Société"},inplace=True)
        df_expert_unique.drop_duplicates(inplace=True)

        new_body=dbc.Row(
                    dbc.Col(
                        [
                        dbc.Label("Confirmer le souhait de modifier l'expert suivant."),
                        html.Br(),
                        dash_table.DataTable(id='change_selection_table_to_display',
                                columns=[{"name": i, "id": i} for i in df_expert_unique.columns], 
                                data=df_expert_unique.to_dict('records'),
                                style_table={'border': 'thin lightgrey solid'},
                                style_header={'backgroundColor':'lightgrey','fontWeight':'bold','textAlign':'center'},
                                style_cell={'textAlign':'left',
                                            #'font_family': 'cursive',
                                            'font-size': '12px',
                                            'width':'10%'})
                        ],
                    ),
                )
        
        valid_is_disabled = False
        
    return new_body, valid_is_disabled



# Gestion du Message information du chargement de la sélection

@app.callback(
    Output("change_selection_confirmation_modal","is_open"),
    
    Input("change_selection_valid_btn", "n_clicks"),
    State("change_selection_confirmation_modal","is_open"),
    
    )
def change_selection_modal_management(n3, is_open):
    if n3>0:
        return not is_open
    else: 
        return is_open
 
 

    
# Gestion des champs de Identité

@app.callback(
    Output("compagny_name_to_modify","value"),
    Output("last_name_to_modify","value"),
    Output("first_name_to_modify","value"),
    
    Output("compagny_name_to_modify","style"),
    Output("last_name_to_modify","style"),
    Output("first_name_to_modify","style"),

    Input("change_selection_confirmation_modal","is_open"),
    Input("modification_cancellation_confirmation_modal","is_open"),
    
    Input("table_to_modify", "selected_row_ids"),
    
    Input("compagny_name_to_modify","value"),
    Input("last_name_to_modify","value"),
    Input("first_name_to_modify","value"),
    )

def identity_to_modify_management(to_charge_1, to_charge_2, ids_selected,  compagny_name_legacy, last_name_legacy, first_name_legacy):
    
    no=""
    style={"backgroundColor":"white"}
    modification_style={"backgroundColor":"yellow"}
    
    compagny_name_style = style
    last_name_style = style
    first_name_style = style
    
    
    if not ids_selected is None and len(ids_selected)==1 :
    
        # Chargement du profil
    
        experts = experts_loading()
        df = experts.loc[experts.id == ids_selected[0]]

        compagny_name = df.compagny_name.astype('str').item()
        last_name = df.last_name.astype('str').item()
        first_name = df.first_name.astype('str').item()
        
        if compagny_name == "nan":
            compagny_name = no
        if last_name == "nan":
            last_name = no
        if first_name == "nan":
            first_name = no
    
        if to_charge_1 == True or to_charge_2 == True:
    
            pass
    
        else:
            
            if (compagny_name_legacy != compagny_name) and (str(compagny_name_legacy) != no):
                compagny_name = compagny_name_legacy
                compagny_name_style = modification_style
            
            if (last_name_legacy != last_name) and (str(last_name_legacy) != no):
                last_name = last_name_legacy
                last_name_style = modification_style

            if (first_name_legacy != first_name) and (str(first_name_legacy) != no):
                first_name = first_name_legacy
                first_name_style = modification_style
            
    else:
        
        compagny_name = no
        last_name = no
        first_name = no
        
    return compagny_name, last_name, first_name, compagny_name_style, last_name_style, first_name_style


    

# Gestion des champs de Contact

@app.callback(
    Output("email_to_modify","value"),
    Output("phone_1_to_modify","value"),
    Output("phone_2_to_modify","value"),
    Output("website_to_modify","value"),
    
    Output("email_to_modify","style"),
    Output("phone_1_to_modify","style"),
    Output("phone_2_to_modify","style"),
    Output("website_to_modify","style"),
    
    Input("change_selection_confirmation_modal","is_open"),
    Input("modification_cancellation_confirmation_modal","is_open"),
    
    Input("table_to_modify", "selected_row_ids"),
    
    Input("email_to_modify","value"),
    Input("phone_1_to_modify","value"),
    Input("phone_2_to_modify","value"),
    Input("website_to_modify","value"),
    )

def contact_to_modify_management(to_charge_1, to_charge_2, ids_selected,  email_legacy, phone_1_legacy, phone_2_legacy, website_legacy):
    
    no=""
    style={"backgroundColor":"white"}
    modification_style={"backgroundColor":"yellow"}
    
    email_style = style
    phone_1_style = style
    phone_2_style = style
    website_style = style
    
    
    if not ids_selected is None and len(ids_selected)==1 :
    
        # Chargement du profil
    
        experts = experts_loading()
        df = experts.loc[experts.id == ids_selected[0]]

        email = df.email.astype('str').item()
        phone_1 = df.phone_1.astype('str').item()
        phone_2 = df.phone_2.astype('str').item()
        website = df.website.astype('str').item()
        
        if email == "nan":
            email = no
        if phone_1 == "nan":
            phone_1 = no
        if phone_2 == "nan":
            phone_2 = no
        if website == "nan":
            website = no
    
    
        if to_charge_1 == True or to_charge_2 == True:
    
            pass
    
        else:
            
            if (email_legacy != email) and (str(email_legacy) != no):
                email = email_legacy
                email_style = modification_style
            
            if (phone_1_legacy != phone_1) and (str(phone_1_legacy) != no):
                phone_1 = phone_1_legacy
                phone_1_style = modification_style
                
            if (phone_2_legacy != phone_2) and (str(phone_2_legacy) != no):
                phone_2 = phone_2_legacy
                phone_2_style = modification_style
                
            if (website_legacy != website) and (str(website_legacy) != no):
                website = website_legacy
                website_style = modification_style
    
    else:
    
        email = no
        phone_1 = no
        phone_2 = no
        website = no
    
    return email, phone_1, phone_2, website, email_style, phone_1_style, phone_2_style, website_style
     


# Gestion des styles de Localisation

@app.callback(
    Output("region_name_to_modify","style"),
    Output("county_name_to_modify","style"),
    Output("city_name_to_modify","style"),
    
    State("table_to_modify", "selected_row_ids"),
    
    Input("region_name_to_modify","value"),
    Input("county_name_to_modify","value"),
    Input("city_name_to_modify","value")
    )

def location_to_modify_style_management(ids_selected,  region_name_inbox, county_name_inbox, city_name_inbox):
    
    no=""
    style={"backgroundColor":"white"}
    modification_style={"backgroundColor":"yellow"}
    
    region_name_style = style
    county_name_style = style
    city_name_style = style
    
    if not ids_selected is None and len(ids_selected)==1 :
        
        # Chargement du profil
    
        experts = experts_loading()
        df = experts.loc[experts.id == ids_selected[0]]
        geo_id = int(df.geo_id)
        
        geo = geo_loading()
        
        region_name = geo.loc[geo.id == geo_id, "region_name"].item()
        county_name = geo.loc[geo.id == geo_id, "county_name"].item()
        city_name = geo.loc[geo.id == geo_id, "city_name"].item()
        
        if (region_name_inbox != region_name):
            region_name_style = modification_style

        if (county_name_inbox != county_name):
            county_name_style = modification_style

        if (city_name_inbox != city_name):
            city_name_style = modification_style
        
    return region_name_style, county_name_style, city_name_style
    
    
    
# Gestion des champs de Localisation

@app.callback(
    Output("region_name_to_modify","value"),
    Output("county_name_to_modify","value"),
    Output("city_zip_code_to_modify","value"),
    Output("city_name_to_modify","value"),

    Output("region_name_to_modify","options"),
    Output("county_name_to_modify","options"),
    Output("city_name_to_modify","options"),

    Input("change_selection_confirmation_modal","is_open"),
    Input("modification_cancellation_confirmation_modal","is_open"),
    
    State("table_to_modify", "selected_row_ids"),
    
    Input("region_name_to_modify","value"),
    Input("county_name_to_modify","value"),
    Input("city_name_to_modify","value"),
    
    State("region_name_to_modify","options"),
    State("county_name_to_modify","options"),
    State("city_name_to_modify","options"),
    )

def location_to_modify_management(to_charge_1, to_charge_2, ids_selected,  region_name_inbox, county_name_inbox, city_name_inbox, regions_list_inbox, counties_list_inbox, cities_list_inbox):
    
    no=""
    regions_list = regions_list_inbox
    counties_list = counties_list_inbox
    cities_list = cities_list_inbox
      
    if not ids_selected is None and len(ids_selected)==1 :
    
        # Chargement du profil
    
        experts = experts_loading()
        df = experts.loc[experts.id == ids_selected[0]]
        geo_id = int(df.geo_id)
        
        geo = geo_loading()
        
        region_name = geo.loc[geo.id == geo_id, "region_name"].item()
        county_name = geo.loc[geo.id == geo_id, "county_name"].item()
        city_zip_code = geo.loc[geo.id == geo_id, "city_zip_code"].item()
        city_name = geo.loc[geo.id == geo_id, "city_name"].item()
    
        if to_charge_1 == True or to_charge_2 == True:
            
            regions_list = sorted(list(geo.region_name.unique()))
            regions_list = [{"label":n, "value":n} for n in regions_list]
            
            counties_list = geo_to_dropdown(geo, "region_name", region_name, "county_name")
            cities_list = geo_to_dropdown(geo, "county_name", county_name, "city_name")          
        
        else:
              
            # 1) Région est modifié
    
            if ctx.triggered_id=="region_name_to_modify":

                region_name = region_name_inbox
                regions_list, counties_list, cities_list = location_options_management("region_name",region_name, regions_list, counties_list, cities_list)
                
                county_name = no
                city_zip_code = no
                city_name = no

            # 2) Département (de la région) est modifié
    
            elif ctx.triggered_id=="county_name_to_modify":
                
                county_name = county_name_inbox
                region_name = geo.loc[geo.county_name == county_name_inbox, "region_name"].unique()[0]
                
                regions_list, counties_list, cities_list = location_options_management("county_name",county_name, regions_list, counties_list, cities_list)

                city_zip_code = no
                city_name = no
                    
            # 3) ville (du département) est modifié
    
            elif ctx.triggered_id=="city_name_to_modify":

                region_name = region_name_inbox
                county_name = county_name_inbox
                city_name = city_name_inbox
                city_zip_code = geo.loc[(geo.region_name == region_name_inbox) & (geo.county_name == county_name_inbox) & (geo.city_name == city_name_inbox), "city_zip_code"].unique()[0]
    
    else:
    
        region_name = no
        county_name = no
        city_zip_code = no
        city_name = no
    
    return region_name, county_name, city_zip_code, city_name,  regions_list, counties_list, cities_list
    
    
    
      
# Gestion des champs de Activité

@app.callback(
    Output("activity_field_to_modify","value"),
    Output("activity_reach_to_modify","value"),
    Output("activity_remote_to_modify","value"),
    
    Output("activity_field_to_modify","style"),
    Output("activity_reach_to_modify","style"),
    Output("activity_remote_to_modify","style"),

    Input("change_selection_confirmation_modal","is_open"),
    Input("modification_cancellation_confirmation_modal","is_open"),
    
    Input("table_to_modify", "selected_row_ids"),
    
    Input("activity_field_to_modify","value"),
    Input("activity_reach_to_modify","value"),
    Input("activity_remote_to_modify","value")
    )

def activity_to_modify_management(to_charge_1, to_charge_2, ids_selected,   activity_field_legacy, activity_reach_legacy, activity_remote_legacy):
    no=""
    style={"backgroundColor":"white"}
    modification_style={"backgroundColor":"yellow"}
       
    activity_field_style = style
    activity_reach_style = style
    activity_remote_style = style
    
    if not ids_selected is None and len(ids_selected)==1 :
    
        # Chargement du profil
    
        experts = experts_loading()
        df = experts.loc[experts.id == ids_selected[0]]

        fields = fields_loading()
        
            # Attention, il peut y avoir plusieurs fields !
        expert_identity = experts.loc[experts.id == ids_selected[0], ["compagny_name", "last_name", "first_name"]]       
        df_list = experts.loc[(experts.compagny_name == expert_identity.compagny_name.item()) & (experts.last_name == expert_identity.last_name.item()) & (experts.first_name == expert_identity.first_name.item())]
        field_id_list = list(df_list.field_id.unique())
        activity_field = [fields.loc[fields.id == int(i), "title"].item() for i in field_id_list]
        
        
        activity_reach = df.reach.astype('str').item()  
         
        if df.remote_work.astype('str').item() == '0':
            activity_remote = []
        else:
            activity_remote = [1]
        
    
        if activity_reach == "nan":
            activity_reach = no   
            
        if to_charge_1 == True or to_charge_2 == True:
    
            pass
    
        else:
            
            if (activity_field_legacy != activity_field) and (activity_field_legacy != no):
                activity_field = activity_field_legacy
                activity_field_style = modification_style
            
            if (activity_reach_legacy != activity_reach) and (str(activity_reach_legacy) != no):
                activity_reach = activity_reach_legacy
                activity_reach_style = modification_style

            if (activity_remote_legacy != activity_remote) :
                activity_remote = activity_remote_legacy
                activity_remote_style = modification_style
            
    else:

        activity_field = []
        activity_reach = no
        activity_remote = []

    return activity_field, activity_reach, activity_remote, activity_field_style, activity_reach_style, activity_remote_style
        


# Gestion des champs de Verification

@app.callback(
    Output("check_to_modify","value"),
    Output("last_contact_to_modify","date"),
    
    Output("check_to_modify","style"),
    Output("last_contact_to_modify","style"),
    
    Input("change_selection_confirmation_modal","is_open"),
    Input("modification_cancellation_confirmation_modal","is_open"),

    State("table_to_modify", "selected_row_ids"),
    
    Input("check_to_modify","value"),
    Input("last_contact_to_modify","value"),
    )

def identity_to_modify_management(to_charge_1, to_charge_2, ids_selected,  check_legacy, last_contact_legacy):
    no=""
    style={"backgroundColor":"white"}
    modification_style={"backgroundColor":"yellow"}
    
    check_style = style
    last_contact_style = style
    
    if not ids_selected is None and len(ids_selected)==1 :
        
        # Chargement du profil
        
        experts = experts_loading()
        df=experts.loc[experts.id == ids_selected[0]]

        if df.check.astype('str').item() == '0':
            check = []
        else:
            check = [1]      

        last_contact = df.last_contact.item()

        # if to_charge_1 == True or to_charge_2 == True:

        if ctx.triggered_id == "check_to_modify":
        
            if (check_legacy != check) and (check_legacy != no):
                check = check_legacy
                check_style = modification_style
                
            if check == [1] :
                if str(last_contact) == "NaT":
                    last_contact = pd.to_datetime(date.today()).strftime("%Y-%m-%d")
            else:
                last_contact = pd.NaT
                
        if ctx.triggered_id == "last_contact_to_modify":     
                
            if (last_contact_legacy != last_contact) and (last_contact_legacy != no):
                last_contact = last_contact_legacy
                last_contact_style = modification_style   

    else:
        
        check = []
        last_contact = pd.NaT

    return check, last_contact, check_style, last_contact_style
    


# Gestion de la mise à dispo du DatePickSingle

@app.callback(
    Output("last_contact_to_modify","disabled"),

    Input("check_to_modify","value")
    )
def DatePickerSingle_management(checked):
    if checked == [1]:
        return False
    else:
        return True

        
# Gestion du Message de demande de confirmation d'annulation de la modification

@app.callback(
    Output("modification_cancellation_modal", "is_open"),
    
    Input("modification_cancellation_btn","n_clicks"),
    Input("modification_cancellation_cancel_btn", "n_clicks"),
    Input("modification_cancellation_valid_btn", "n_clicks"),
    
    State("modification_cancellation_modal", "is_open"),
    )
def modification_cancellation_modal_management(n1, n2, n3, is_open):
    if n1>0 or n2>0 or n3>0:
        return not is_open
    else:
        return is_open


# Gestion du Message de demande de confirmation d'exécution de la modification

@app.callback(
    Output("modification_validation_modal", "is_open"),
    
    Input("modification_validation_btn","n_clicks"),
    Input("modification_validation_cancel_btn", "n_clicks"),
    Input("modification_validation_valid_btn", "n_clicks"),
    
    State("modification_validation_modal", "is_open")
    )
def modification_validation_modal_management(n1, n2, n3, is_open):
    if n1>0 or n2>0 or n3>0:
        return not is_open
    else:
        return is_open
    
    
# Gestion du Message information de l'annulation de la modification

@app.callback(
    Output("modification_cancellation_confirmation_modal","is_open"),
    
    Input("modification_cancellation_valid_btn", "n_clicks"),
    State("modification_cancellation_confirmation_modal","is_open")
    )
def modification_cancellation_valid_modal_management(n3, is_open):
    if n3>0:
        return not is_open
    else: 
        return is_open
    
    
# Gestion du Message information de la confirmation de la modification

@app.callback(
    Output("modification_confirmation_modal","is_open"),
    
    Input("modification_validation_valid_btn", "n_clicks"),
    State("modification_confirmation_modal","is_open")
    )
def modification_confirmation_valid_modal_management(n3, is_open):
    if n3>0:
        return not is_open
    else: 
        return is_open
    
    
    
# Disponibilité du bouton "Modifier"

@app.callback(
    Output("modification_validation_btn","disabled"),
    
    Input("compagny_name_to_modify","style"),
    Input("last_name_to_modify","style"),
    Input("first_name_to_modify","style"),
    Input("email_to_modify","style"),
    Input("phone_1_to_modify","style"),
    Input("phone_2_to_modify","style"),
    Input("website_to_modify","style"),
    Input("region_name_to_modify","style"),
    Input("county_name_to_modify","style"),
    Input("city_name_to_modify","style"),
    
    Input("activity_field_to_modify","style"),
    Input("activity_reach_to_modify","style"),
    Input("activity_remote_to_modify","style"),
    Input("check_to_modify","style"),
    Input("last_contact_to_modify","style")
    )
def modification_validation_button_management(compagny_name_style, last_name_style, first_name_style, 
                                              email_style, phone_1_style, phone_2_style, website_style, 
                                              region_name_style, county_name_style, city_name_style, 
                                              activity_field_style, activity_reach_style, activity_remote_style,
                                              check_style, last_contact_style):
    
    cnt = 0
    modification_style={"backgroundColor":"yellow"}
    
    if compagny_name_style == modification_style:
        cnt += 1
        
    if last_name_style == modification_style:
        cnt += 1
        
    if first_name_style == modification_style:
        cnt += 1
        
    if email_style == modification_style:
        cnt += 1
        
    if phone_1_style == modification_style:
        cnt += 1
        
    if phone_2_style == modification_style:
        cnt += 1
        
    if website_style == modification_style:
        cnt += 1
        
    if region_name_style == modification_style:
        cnt += 1
        
    if county_name_style == modification_style:
        cnt += 1
        
    if city_name_style == modification_style:
        cnt += 1
        
    if activity_field_style == modification_style:
        cnt += 1
        
    if activity_reach_style == modification_style:
        cnt += 1
        
    if activity_remote_style == modification_style:
        cnt += 1
        
    if check_style == modification_style:
        cnt += 1
        
    if last_contact_style == modification_style:
        cnt += 1

    if cnt >0:                                 ###  Possibilité de récupérer le nombre de modifications effectuées !
        return False
    else:
        return True
    

    
    
# Modification des lignes    +     Gestion des items de l'accordéon
    
@app.callback(
    Output("modification_steps","active_item"),
    
    Input("modification_confirmation_modal","is_open"),
    Input("change_selection_valid_btn","n_clicks"),

    State("table_to_modify", "selected_row_ids"),
    
    State("compagny_name_to_modify","value"),   
    State("last_name_to_modify","value"), 
    State("first_name_to_modify","value"),
    
    State("email_to_modify","value"),   
    State("phone_1_to_modify","value"), 
    State("phone_2_to_modify","value"),
    State("website_to_modify","value"),
    
    State("region_name_to_modify","value"),
    State("county_name_to_modify","value"),
    State("city_name_to_modify","value"),  
    
    State("activity_field_to_modify","value"),   
    State("activity_reach_to_modify","value"), 
    State("activity_remote_to_modify","value"),
    
    State("check_to_modify","value"), 
    State("last_contact_to_modify","date"),

    )
def expert_modification(is_open, n, ids_selected,  
                         compagny_name_modified, last_name_modified, first_name_modified, 
                         email_modified, phone_1_modified, phone_2_modified, website_modified, 
                         region_name_modified, county_name_modified, city_name_modified,
                         activity_field_modified, activity_reach_modified, activity_remote_modified, 
                         check_modified, last_contact_modified):
    
    if is_open == True :
        
        fields = fields_loading()
        geo = geo_loading()
        experts = experts_loading()
        
        # Lignes initiales de l'expert 
                
        expert_identity = experts.loc[experts.id == ids_selected[0], ["compagny_name", "last_name", "first_name"]]                                                                                                     # Ici, je n'ai qu'une ligne
        expert_old = experts.loc[(experts.compagny_name == expert_identity.compagny_name.item()) & (experts.last_name == expert_identity.last_name.item()) & (experts.first_name == expert_identity.first_name.item())]         # Ici, je récupère toutes les lignes

        # Reconstruction des lignes de l'expert
        
        expert_new = pd.DataFrame(columns=expert_old.columns)  
               
            # Le nombre de Field pilote le nombre de lignes 
        
        fields_new = [int(fields.loc[fields.title == activity_field_modified[i], "id"]) for i in range(len(activity_field_modified))]
        fields_old = [int(i) for i in list(expert_old.field_id)]
        
        expert_new.field_id = list(set(fields_old + fields_new))  # on supprime les doublons
        
            # Données communes à toutes les lignes
        
                ## Identity
            
        expert_new.compagny_name = compagny_name_modified
        expert_new.last_name = last_name_modified
        expert_new.first_name = first_name_modified
        
                ## Contact
        
        expert_new.email = email_modified    
        expert_new.phone_1 = phone_1_modified
        expert_new.phone_2 = phone_2_modified
        expert_new.website = website_modified
        
                ## Location
        
        geo_id_new = geo.loc[(geo.city_name == city_name_modified) & (geo.county_name == county_name_modified) & (geo.region_name == region_name_modified), "id"] 
        geo_id_new=list(geo_id_new)[0]
            
        expert_new.geo_id = geo_id_new
            
                ## Activity
            
        expert_new.reach = int(activity_reach_modified)
            
        if activity_remote_modified==[1]:
            expert_new.remote_work = int(1)
        else:
            expert_new.remote_work = int(0)
        
                ## Verification
        
        if check_modified==[1]:
            expert_new.check = int(1)
        else:
            expert_new.check = int(0)
        
        expert_new.last_contact = last_contact_modified
        

            # Données spécifiques à la ligne (existait-elle avant la modification ?)
        
        cnt = 0
        
        for f_id in expert_new.field_id:
            
            print(f_id)
            
            if f_id in fields_old :          # Dans l'ancienne liste ... 
                
                id_current = int(expert_old.loc[expert_old.field_id == f_id,"id"].item())
                expert_new.loc[expert_new.field_id == f_id,"id"] = id_current
                expert_new.loc[expert_new.field_id == f_id,"created_at"] = expert_old.loc[expert_old.field_id == f_id,"created_at"].item()
                expert_new.loc[expert_new.field_id == f_id,"updated_at"] = pd.to_datetime(date.today()).strftime("%Y-%m-%d")
                
                if f_id in fields_new :     # et dans la nouvelle >> on MàJ !
                    
                    expert_new.loc[expert_new.field_id == f_id,"deleted_at"] = pd.NaT
                    
                else:                       # mais pas dans la nouvelle >> on supp !
                    
                    expert_new.loc[expert_new.field_id == f_id,"deleted_at"] = pd.to_datetime(date.today()).strftime("%Y-%m-%d")
                
                
                # Modification effective de la table experts 
                for column in experts.columns:
                    experts.loc[experts.id == id_current, column] = expert_new.loc[expert_new.id == id_current, column].item()

                
            else:                            # PAS dans l'ancienne  >> on crée !
           
                id_current = max(list(experts.id))+cnt+1
                expert_new.loc[expert_new.field_id == f_id,"id"] = id_current
                cnt += 1
                expert_new.loc[expert_new.field_id == f_id,"created_at"] = pd.to_datetime(date.today()).strftime("%Y-%m-%d")
                expert_new.loc[expert_new.field_id == f_id,"updated_at"] = pd.to_datetime(date.today()).strftime("%Y-%m-%d")
                expert_new.loc[expert_new.field_id == f_id,"deleted_at"] = pd.NaT  
                               
                experts = pd.concat([experts, expert_new.loc[expert_new.id == id_current]], axis=0)
                    
        # Sauvegarde
        
        file ="data/"+ experts_filename
        ok_to_save(file, experts)
        
        
        return "selection_step_to_modify"
        
    else:
        
        if (ctx.triggered_id=="change_selection_valid_btn" and n>0):
            return "expert_profile_to_modify"
        else:
            return "selection_step_to_modify"
        
   


        