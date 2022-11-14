from dash import Input, Output, State, ctx

from app import app,server

import pandas as pd

# Functions
from components.functions import plot_map, big_one_building



# Gestion de l'affichage du tableau dynamique (contrôles : Reset et Zoom)

@app.callback(
    Output("table_exploration", "filter_query"),
    Output("table_exploration", "hidden_columns"),
    Output("table_exploration", "selected_rows"),
    Output("table_exploration", "selected_row_ids"),
    Output("table_exploration", "sort_by"),
    Output("table_exploration", "data"),
    
    Output("switch_focus_exploration","on"),
    Output("table_exploration", "row_deletable"),
    Output("table_exploration", "row_selectable"),
    
    Output("table_exploration", "page_current"),
    
    Input('reset_table_exploration','n_clicks'),
    Input("switch_focus_exploration","on"),
    
    State("table_exploration", "filter_query"),
    State("table_exploration", "hidden_columns"),
    State("table_exploration", "selected_rows"),
    State("table_exploration", "selected_row_ids"),
    State("table_exploration", "sort_by"),
    State("table_exploration", "data"),
    State("table_exploration", "page_current")
    )

def table_exploration_management(n, focus_on, state_query, state_hidden, state_selected, state_ids_selected, state_sorting, data, page_current):
    
    hidden_columns_init=["id","created_at", "updated_at", "deleted_at", "city_zip_code", "region_name", "reach", "remote_work", "check", "last_contact", "lat", "lon"]
    
    df = big_one_building()
     
    if ctx.triggered_id=="reset_table_exploration" and n>0:
        
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
    Output("kpi_rows_selected_exploration","children"),
    Input("table_exploration", "selected_row_ids")
)
def kpi_selected_rows_exploration(ids_selected):
    
    if not ids_selected is None:
        return str(len(ids_selected))
    else:
        return 0


# MàJ du nombre d'experts différents

@app.callback(
    Output("kpi_experts_nb_exploration","children"),
    Input("table_exploration", "selected_row_ids")
)
def kpi_selected_rows_exploration(ids_selected):
    
    if not ids_selected is None and len(ids_selected)>0:
        
        df = big_one_building()
        df_focus = df[df.id.isin(ids_selected)]
        df_focus = df_focus[["first_name","last_name","compagny_name"]]
        df_focus.drop_duplicates(inplace=True)
        
        return str(len(df_focus))
    
    else:
        return 0


# MàJ de la Carto d'exploration

@app.callback(
    Output("map_explo", "figure"),
    Input("table_exploration", "selected_row_ids")
    )
def show_exploration(ids_selected):

    df = big_one_building()
    
    df = df.loc[:,("id","city_name", "lat", 'lon')]

    if not ids_selected is None and len(ids_selected)>0:
        
        selection = []
        
        for i in range(len(ids_selected)):
            if i == 0:
                selection = df.loc[df.id == ids_selected[i]]
            else:
                selection = pd.concat([selection, df.loc[df.id == ids_selected[i]]], axis=0)

        selection = selection.drop_duplicates()
        return plot_map(selection)

    else:
        
        return plot_map(df)





