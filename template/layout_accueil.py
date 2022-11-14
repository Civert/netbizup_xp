from dash import Dash, dcc, html
import dash_bootstrap_components as dbc


logo_accueil='assets/Logo_complet.svg'

home_content = html.Div(
                        [
                            
                        dbc.Row(
                            [
                            dbc.Col(
                                [
                                
                                html.Img(
                                        src=logo_accueil, 
                                        style={
                                            "height":"30px",
                                            "marginBottom":"50px"
                                        }
                                ),
                                    
                                html.H1(
                                        "Experts métiers",
                                        style={
                                            "textAlign":"center",
                                            "fontWeight":"bold",
                                            "color":"#F35E29",
                                            "marginBottom":"20px"
                                            }
                                ),
                                
                                html.H5(
                                        "Visualisation et Gestion du vivier",
                                        style={
                                            "textAlign":"center",
                                            "fontWeight":"bold",
                                            "color":"black",
                                            "marginBottom":"50px"
                                            }
                                ),
                                
                                html.H6(
                                        "Usage réservé aux membres de Business Compass",
                                        style={
                                            "textAlign":"center",
                                            "fontWeight":"bold",
                                            "color":"red",
                                            "marginBottom":"10px"
                                            }
                                ),
                                    
                                dbc.Row(    
                                    dbc.Card(
                                        [
                                        # dbc.CardHeader(
                                        #     html.Label("Identification"), style={"textAlign":"center", }
                                        # ),
                                        
                                        dbc.CardBody(
                                            [
                                                
                                            dbc.InputGroup(
                                                [
                                                dbc.InputGroupText("Username :", style={"width":"95px"}), 
                                                dbc.Input(placeholder="admin")
                                                ],
                                                className="mb-3",
                                            ),
                                            
                                            dbc.InputGroup(
                                                [
                                                dbc.InputGroupText("Password :", style={"width":"95px"}), 
                                                dbc.Input(placeholder="admin_pwd")
                                                ],
                                                
                                            ),
                                                
                                            ],
                                            style={"margin":"15px"}
                                        ),
                                        ],
                                        style={"border":"1pt solid white",
                                            "width":"400px"}                             
                                        
                                    ),
                                    justify="center"
                                ),  
                                    
                                    
                                ],
                                width=4,
                                style={
                                    "textAlign":"center",
                                    "align":"center",
                                    "margin":"50px",
                                    "marginTop":"100px"
                                }                         
                                
                            )
                            ],
                            justify="center",
                            
                        )
                            
                        ]
                )
