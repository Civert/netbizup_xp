import dash_bootstrap_components as dbc
from dash import dcc, html
from dash import html

logo='assets/android-chrome-192x192.png'

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "10rem",
    "padding": "1rem 0.5rem",
    "background-color": "#585858",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "10rem",
    #"margin-right": "1rem",
    "padding": "1rem 1rem",
}

sidebar = html.Div(
    [
        html.Div([
            html.Img(src=logo, alt="NetBizUp", height="100px"),
            ],style={"textAlign":"center", "marginBottom":"20px"}
        ),

        dbc.Nav(
            [              

            dbc.NavItem(dbc.NavLink("Accueil", href="/accueil", active="exact",  style={"fontSize":"17px","color":"white", "fontWeight":"bold"})),
            
            dbc.NavItem(dbc.NavLink("Visualisation", style={"fontSize":"17px","color":"#FFB401", "fontWeight":"bold"})),
            dbc.NavItem(dbc.NavLink("Dashboard", href="/visualisation_dashboard", active="exact", style={"fontSize":"15px","color":"white", "fontWeight":"bold", "paddingLeft":"2rem"})),
            dbc.NavItem(dbc.NavLink("Exploration", href="/visualisation_exploration", active="exact", style={"fontSize":"15px","color":"white", "fontWeight":"bold", "paddingLeft":"2rem"})),
            
            dbc.NavItem(dbc.NavLink("Gestion", style={"fontSize":"17px","color":"#FFB401", "fontWeight":"bold"})),
            dbc.NavItem(dbc.NavLink("Création", href="/gestion_creation", active="exact", style={"fontSize":"15px","color":"white", "fontWeight":"bold", "paddingLeft":"2rem"})),
            dbc.NavItem(dbc.NavLink("Modification", href="/gestion_modification", active="exact", style={"fontSize":"15px","color":"white", "fontWeight":"bold", "paddingLeft":"2rem"})),
            dbc.NavItem(dbc.NavLink("Suppression", href="/gestion_suppression", active="exact", style={"fontSize":"15px","color":"white", "fontWeight":"bold", "paddingLeft":"2rem"})),

            ],
            vertical=True,
            pills=True,
            
        ),
                    
        dbc.Nav(
            [
            dbc.NavItem(dbc.NavLink("Mentions légales", href="/mentions_legales", active="exact", style={"fontSize":"10px","color":"white", "fontWeight":"bold"})),
            dbc.NavItem(dbc.NavLink("RGPD", style={"fontSize":"10px","color":"#FFB401", "fontWeight":"bold"})),
            dbc.NavItem(dbc.NavLink("Crédits", style={"fontSize":"10px","color":"#FFB401", "fontWeight":"bold", "paddingBottom":"1rem"})),
            ],
            vertical=True,
            pills=True,
            className="position-absolute bottom-0"
        )
        
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

layout = html.Div([dcc.Location(id="url"), sidebar, content])
