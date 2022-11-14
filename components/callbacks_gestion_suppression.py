from dash import Input, Output, State, ctx, html, dash_table
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc

from app import app,server

import pandas as pd
from datetime import date


# Functions
from components.functions import big_one_building, experts_loading, ok_to_save, experts_filename



# Gestion de la table dynamique du Module Suppression en fonction du Reset et Focus

@app.callback(
    Output("table_to_delete", "filter_query"),
    Output("table_to_delete", "hidden_columns"),
    Output("table_to_delete", "selected_rows"),
    Output("table_to_delete", "selected_row_ids"),
    Output("table_to_delete", "sort_by"),
    Output("table_to_delete", "data"),
    
    Output("switch_focus_to_delete","on"),
    Output("table_to_delete", "row_deletable"),
    Output("table_to_delete", "row_selectable"),
    
    Output("table_to_delete", "page_current"),
    
    Input('reset_table_to_delete','n_clicks'),
    Input("removing_confirmation_modal","is_open"),
    Input("switch_focus_to_delete","on"),
    
    State("table_to_delete", "filter_query"),
    State("table_to_delete", "hidden_columns"),
    State("table_to_delete", "selected_rows"),
    State("table_to_delete", "selected_row_ids"),
    State("table_to_delete", "sort_by"),
    State("table_to_delete", "data"),
    State("table_to_delete", "page_current"),
    )

def table_to_delete_management(n, is_open, focus_on, state_query, state_hidden, state_selected, state_ids_selected, state_sorting, data, page_current):
    
    hidden_columns_init=["id","created_at", "updated_at", "deleted_at", "city_zip_code", "region_name", "reach", "remote_work", "check", "last_contact", "lat", "lon"]

    df = big_one_building()
    
    if (ctx.triggered_id=="reset_table_to_delete" and n>0) or is_open == True :
        
        state_query = ""
        state_hidden = hidden_columns_init
        state_selected = []
        state_ids_selected = []
        state_sorting = []
        data = df.to_dict('records')
        focus_on = False
        row_deletable = True
        row_selectable = "multi"
        page_current = 0
      
    else:
        
        if focus_on == True:
        
            state_query = ""
            state_hidden = hidden_columns_init if state_hidden == hidden_columns_init else state_hidden
            state_selected = state_selected
            state_ids_selected = state_ids_selected
            state_sorting = []
            data = df[df.id.isin(state_ids_selected)].to_dict('records')
            focus_on = focus_on
            row_deletable = False
            row_selectable = False
            page_current = 0
 
        else:

            state_query = "" if state_query is None else state_query
            state_hidden = hidden_columns_init if state_hidden == hidden_columns_init else state_hidden
            state_selected = [] if state_selected is None else state_selected
            state_ids_selected = [] if state_ids_selected is None else state_ids_selected
            state_sorting = [] if state_sorting is None else state_sorting
            data = df.to_dict('records')
            focus_on = focus_on
            row_deletable = True
            row_selectable = "multi"
            page_current = 0

    return state_query, state_hidden, state_selected, state_ids_selected, state_sorting, data, focus_on, row_deletable, row_selectable, page_current


# MàJ du nombre de lignes sélectionnées

@app.callback(
    Output("kpi_rows_selected_to_delete","children"),
    Input("table_to_delete", "selected_row_ids")
)
def kpi_selected_rows_to_remove(ids_selected):
    
    if not ids_selected is None:
        return str(len(ids_selected))
    else:
        return 0


# MàJ du nombre d'experts différents

@app.callback(
    Output("kpi_experts_nb_to_delete","children"),
    Input("table_to_delete", "selected_row_ids"),
)
def kpi_selected_rows_to_remove(ids_selected):
    
    if not ids_selected is None and len(ids_selected)>0:
            
        df = big_one_building()
        df_focus = df[df.id.isin(ids_selected)]
        df_focus = df_focus[["first_name","last_name","compagny_name"]]
        df_focus.drop_duplicates(inplace=True)
        
        return str(len(df_focus))
    
    else:
        return 0


# Gestion du Message de demande de confirmation de suppression

@app.callback(
    Output("removing_modal", "is_open"),
    
    Input("removing_rows_selected_btn","n_clicks"),
    Input("removing_cancel","n_clicks"),
    Input("removing_valid","n_clicks"),
    State("removing_modal", "is_open"),
    )
def removing_modal_management(n1, n2, n3, is_open):
    if n1>0 or n2>0 or n3>0:
        return not is_open
    else:
        return is_open
   
   
   
# Personnalisation du Message de confirmation de suppression

@app.callback(
    Output("removing_modal_body", "children"),
    
    Input("removing_modal","is_open"),
    State("table_to_delete", "selected_row_ids"),
    )
def removing_modal_customization(is_open, ids_selected):
    
    if is_open == False or len(ids_selected)==0:  
        
        return "Cette action ne va rien supprimer."
    
    else:
        
        df = big_one_building()
        df = df.loc[:, ("id","first_name", "last_name", "compagny_name", "field")]
        df = df[df.id.isin(ids_selected)]
        
        df_expert_unique = df.loc[:,("first_name", "last_name", "compagny_name", "field")]
        df_expert_unique.rename(columns={"first_name": "Prénom","last_name": "Nom","compagny_name": "Société", "field":"Domaine"},inplace=True)       
        
        new_body=dbc.Row(
                    dbc.Col(
                        [
                        dbc.Label("Cette action va supprimer la sélection suivante :"),
                        html.Br(),
                        dash_table.DataTable(id='removing_table_to_display',
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
        return new_body
    
    
# Gestion du Message information de suppression effective

@app.callback(
    Output("removing_confirmation_modal","is_open"),
    
    Input("removing_valid", "n_clicks"),
    State("removing_confirmation_modal","is_open"),
    )
def removing_valid_button_management(n3, is_open):
    
    if n3>0:
        return not is_open
    
    else: 
        return is_open   



# Suppression des lignes 

@app.callback(
    Output("selection_module_to_delete", "active_item"),
    Input("removing_confirmation_modal","is_open"),
    State("table_to_delete", "selected_row_ids"),
    )

def expert_removing(is_open, ids_selected):
    
    if is_open == False or len(ids_selected)==0:  
        
        raise PreventUpdate
    
    else:
        
        df = experts_loading()
        
        for i in range(len(ids_selected)):
            
            df.loc[df.id == ids_selected[i], "deleted_at"] = pd.to_datetime(date.today())
        
        file ="data/"+ experts_filename
        ok_to_save(file, df)
        
        return "selection_step_to_delete"
    
    
    
    