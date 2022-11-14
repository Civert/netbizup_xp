from dash import Dash, dcc, html

import dash_bootstrap_components as dbc


# Functions
from components.functions import plot_map, carte_choropleth, focus_to_plot, plot_treemap, experts_loading, kpi_to_dashboard

# Data

kpi_nb_experts, kpi_nb_cities, kpi_nb_fields_by_expert = kpi_to_dashboard()
focus = focus_to_plot()


dashboard_content = dbc.Card(
                        [
                            
                        dbc.CardHeader(
                                html.H1(
                                        "Synthèse",
                                        style={
                                            "textAlign":"center",
                                            "fontWeight":"bold",
                                            "color":"#F35E29"
                                            }
                                ),
                                style={"backgroundColor":"white"},
                        ),
                            
                            
                        dbc.Row(
                            
                            dbc.Col(
                                

                                html.Table(
                                        [
                                        
                                        html.Tr(
                                            [
                                            
                                            html.Td(
                                                [
                                                html.H5("Nb d'experts", style={"color":"white","fontWeight":"bold"}),
                                                ],
                                                style={
                                                    "width":"25%",
                                                    "paddingTop":"10px",
                                                    "paddingBottom":"5px",
                                                    "border":"15px solid white"
                                                }   
                                            ),
                                            
                                            html.Td(
                                                [
                                                html.H5("Nb moyen de domaines", style={"color":"white","fontWeight":"bold"}),
                                                ],
                                                style={
                                                    "width":"25%",
                                                    "paddingTop":"10px",
                                                    "paddingBottom":"5px",
                                                    "border":"15px solid white"
                                                }   
                                            ),
                                            
                                            html.Td(
                                                [
                                                html.H5("Nb de communes", style={"color":"white","fontWeight":"bold"}),
                                                ],
                                                style={
                                                    "width":"25%",
                                                    "paddingTop":"10px",
                                                    "paddingBottom":"5px",
                                                    "border":"15px solid white"
                                                }   
                                            ),
                                            
                                            html.Td(
                                                [
                                                html.H5("Taux de couverture (Fr)", style={"color":"white","fontWeight":"bold"}),
                                                ],
                                                style={
                                                    "width":"25%",
                                                    "paddingTop":"10px",
                                                    "paddingBottom":"5px",
                                                    "border":"15px solid white"
                                                }   
                                            ),
                                            
                                            ],
                                            style={
                                                "textAlign":"center",
                                                "backgroundColor":"#585858",
                                                "padding":"20px" 
                                            }
                                        ),
                                        
                                        
                                        html.Tr(
                                            [
                                            
                                            html.Td(
                                                [
                                                html.H3(kpi_nb_experts, id="kpi_nb_experts", style={"color":"#585858","fontWeight":"bold"}),
                                                ],
                                                style={
                                                    "paddingTop":"10px",
                                                } 
                                            ),
                                            
                                            html.Td(
                                                [
                                                html.H3(kpi_nb_fields_by_expert, id="kpi_nb_fields_by_expert", style={"color":"#585858","fontWeight":"bold"}),
                                                ],
                                                style={
                                                    "paddingTop":"10px",
                                                } 
                                            ),
                                            
                                            html.Td(
                                                [
                                                html.H3(kpi_nb_cities, id="kpi_nb_cities", style={"color":"#585858","fontWeight":"bold"}),
                                                ],
                                                style={
                                                    "paddingTop":"10px",
                                                } 
                                            ),
                                            
                                            html.Td(
                                                
                                                        ### A completer !!!
                                                
                                                
                                            ),
                                            
                                            ],
                                            style={
                                                "textAlign":"center",
                                                "padding":"20px" 
                                            }
                                            
                                        ),
                                    
                                        
                                        ],
                                        style={
                                            "marginBottom" :"20px",
                                            "width":"100%"
                                            }
                                ),   
                                
                                
                            ),    
                        ),        
                          
                            
                        dbc.Row(
                            [ 

                            dbc.Col(
                                [
                                html.Div(
                                    html.H5("Régions", style={"color":"white", "textAlign":"center", "fontWeight":"bold"}),
                                    style={
                                        "backgroundColor":"#585858", 
                                        "paddingTop":"10px",
                                        "paddingBottom":"5px",
                                        "border":"15px solid white"
                                    }
                                ),
                                dcc.Graph(
                                    id="graph_reg",
                                    figure=carte_choropleth("region_code", "region_name"),
                                    style={"paddingLeft":"20px", "paddingRight":"20px"}
                                    )
                                ],
                                width=4,
                                style={"align":"center"}
                                
                            ),

                            dbc.Col(
                                [
                                html.Div(
                                    html.H5("Départements", style={"color":"white", "textAlign":"center", "fontWeight":"bold"}),
                                    style={
                                        "backgroundColor":"#585858", 
                                        "paddingTop":"10px",
                                        "paddingBottom":"5px",
                                        "border":"15px solid white"
                                    }
                                ),
                                dcc.Graph(
                                    id="graph_dep",
                                    figure=carte_choropleth("county_code", "county_name"),
                                    style={"paddingLeft":"20px", "paddingRight":"20px"}
                                    )
                                ],
                                width=4,
                                style={"align":"center"}
                            ),
                            
                            dbc.Col(
                                [
                                html.Div(
                                    html.H5("Communes", style={"color":"white", "textAlign":"center", "fontWeight":"bold"}),
                                    style={
                                        "backgroundColor":"#585858", 
                                        "paddingTop":"10px",
                                        "paddingBottom":"5px",
                                        "border":"15px solid white"
                                    }
                                ),
                                dcc.Graph(
                                    id="graph_ville",
                                    figure=plot_map(focus),
                                    style={"paddingLeft":"20px", "paddingRight":"20px", "marginTop":"40px"}
                                    )
                                ],
                                width=4,
                                style={"align":"bottom"}
                            ),
                                                        
                            
                            ],
                            style={
                                "marginBottom" :"30px",
                                }

                        ), 
                            
                            
                            
                            
                            
                        dbc.Row(
                            [
                                
                            dbc.Col(
                                [
                                html.Div(
                                    html.H5("Couverture des communes par domaine", style={"color":"white", "textAlign":"center", "fontWeight":"bold"}),
                                    style={"backgroundColor":"#585858", "paddingTop":"10px","paddingBottom":"5px" }
                                ),
                                
                                dcc.Graph(
                                    
                                    id="treemap_field_geo",
                                    figure = plot_treemap(),                                   
                                    
                                ),
                                
                                ],
                            ),    
                              
                            ],
                        ),    
                            

                            
                            
                        ],
                    ),



