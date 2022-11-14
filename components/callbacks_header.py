from dash.dependencies import Input, Output

from app import app,server

from template.layout_accueil import home_content
from template.layout_visualisation_dashboard import dashboard_content
from template.layout_visualisation_exploration import exploration_content
from template.layout_gestion_creation import creating_content
from template.layout_gestion_modification import change_content
from template.layout_gestion_suppression import removing_content
from template.layout_mentions_legales import legal_content


# MàJ des pages de l'application

@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
    )
def display_page(pathname):
    
    if pathname=='/accueil' or pathname=='/':
        return home_content
    
    elif pathname=='/visualisation_dashboard' :
        return dashboard_content
    elif pathname=='/visualisation_exploration':
        return exploration_content
    
    elif pathname=='/gestion_creation':
        return creating_content
    elif pathname=='/gestion_modification':
        return change_content
    elif pathname=='/gestion_suppression':
        return removing_content
    
    elif pathname=='/mentions_legales':
        return legal_content

