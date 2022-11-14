from dash import Dash, dcc, html
import dash_bootstrap_components as dbc

from datetime import date

# Functions
from components.functions import plot_map, geo_loading, fields_loading


# Data

geo = geo_loading()
fields = fields_loading()

fields_list = sorted(list(fields.title.unique()))
counties_list = sorted(list(geo.county_name.unique()))
regions_list = sorted(list(geo.region_name.unique()))



creating_content = dbc.Card(
                    [

                    dbc.CardHeader(
                            html.H1(
                                    "Création",
                                    style={
                                        "textAlign":"center",
                                        "fontWeight":"bold",
                                        "color":"#F35E29"
                                        }
                            ),
                            style={"backgroundColor":"white"},
                    ),

                    dbc.Row([
                        dbc.Col([

                            dbc.Accordion(
                                    [
                                    dbc.AccordionItem(
                                            [
                                                
                                            dbc.InputGroup(
                                                    [
                                                    dbc.InputGroupText("Société *", style={"width":"85px"}), 
                                                    dbc.Input(
                                                        value='', 
                                                        placeholder="Conseil SA.", 
                                                        id="input_compagny_name", 
                                                        type="text", 
                                                        valid=False
                                                    ),
                                                    ],
                                                    className="mb-3",
                                            ), 
                                                
                                            dbc.Row(
                                                [
                                                dbc.Col(
                                                    [
                                                    dbc.InputGroup(
                                                            [
                                                            dbc.InputGroupText("Nom *", style={"width":"85px"}), 
                                                            dbc.Input(
                                                                value='',
                                                                placeholder="Dupont",
                                                                id="input_last_name",
                                                                type="text",
                                                                valid=False
                                                            ),
                                                            ],
                                                            className="mb-3",
                                                    ),
                                                    ],
                                                ), 
                                                
                                                dbc.Col(
                                                    [
                                                    dbc.InputGroup(
                                                            [
                                                            dbc.InputGroupText("Prénom", style={"width":"85px"}),
                                                            dbc.Input(
                                                                value='', 
                                                                placeholder="Jean", 
                                                                id="input_first_name", 
                                                                type="text"
                                                            ),
                                                            ],
                                                            className="mb-3",
                                                    ),
                                                    ],
                                                ), 
                                                    
                                                ]
                                            ),
                                            
                                            dbc.Label(
                                                "* Au moins une personne morale ou physique doit être identifiée.", 
                                                style={"font-size":"11px"}
                                            ),
                                                
                                            ],
                                            item_id="form_identity",
                                            title="Identité",
                                    ),   
                                    
                                    
                                    dbc.AccordionItem(
                                            [
                                                
                                            dbc.InputGroup(
                                                    [
                                                    dbc.InputGroupText("Courriel *", style={"width":"85px"}),
                                                    dbc.Input(
                                                        value='', 
                                                        placeholder="jdupont@conseil.eu", 
                                                        id="input_email", 
                                                        type="email", 
                                                        valid=False
                                                    ),
                                                    ],
                                                    className="mb-3",
                                            ), 

                                            dbc.Row(
                                                [
                                                dbc.Col(
                                                    [
                                                    dbc.InputGroup(
                                                            [
                                                            dbc.InputGroupText("Tél. n°1 *", style={"width":"85px"}),
                                                            dbc.Input(
                                                                value='', 
                                                                placeholder="06 07 08 09 10", 
                                                                id="input_phone_1", 
                                                                type="tel", 
                                                                valid=False
                                                            ),
                                                            
                                                            dbc.Popover(
                                                                [
                                                                dbc.PopoverHeader("Conseil !", style={"backgroundColor":"green", "color":"white"}),
                                                                dbc.PopoverBody("Le numéro peut comporter des espaces, mais pas de caractères spéciaux."),
                                                                ],
                                                                target="input_phone_1",
                                                                trigger="legacy",
                                                                placement="top",
                                                            ),
                                                        
                                                            ],
                                                            className="mb-3",
                                                    ),
                                                    ],
                                                ), 
                                                
                                                dbc.Col(
                                                    [
                                                    dbc.InputGroup(
                                                            [
                                                            dbc.InputGroupText("Tél. n°2 *", style={"width":"85px"}),
                                                            dbc.Input(
                                                                value='', 
                                                                placeholder="01 02 03 04 05", 
                                                                id="input_phone_2", 
                                                                type="tel", 
                                                                valid=False
                                                            ),
                                                            
                                                            dbc.Popover(
                                                                [
                                                                dbc.PopoverHeader("Conseil !", style={"backgroundColor":"green", "color":"white"}),
                                                                dbc.PopoverBody("Le numéro peut comporter des espaces, mais pas de caractères spéciaux."),
                                                                ],
                                                                target="input_phone_2",
                                                                trigger="legacy",
                                                                placement="top",
                                                            ),
                                                            
                                                            
                                                            ],
                                                            className="mb-3",
                                                    ),
                                                    ],
                                                ), 
                                                    
                                                ]
                                            ),   
                                                
                                            dbc.InputGroup(
                                                    [
                                                    dbc.InputGroupText("Lien", style={"width":"85px"}), 
                                                    dbc.Input(
                                                        value='', 
                                                        placeholder="www.conseil.eu", 
                                                        id="input_website", 
                                                        type="text"
                                                    ),
                                                    ],
                                                    className="mb-3",
                                            ), 

                                            dbc.Label(
                                                "* Au moins un courriel ou un numéro de téléphone doit être précisé.", 
                                                style={"font-size":"11px"}
                                            ),
                                                
                                            ],
                                            item_id="form_contact",
                                            title="Moyens de contact",
                                    ),  

                                    
                                    dbc.AccordionItem(
                                            [                                      
                                            
                                            dbc.InputGroup(
                                                    [
                                                    dbc.InputGroupText("Région", style={"width":"120px"}),
                                                    dbc.Select(
                                                            options=[{"label":n, "value":n} for n in regions_list],
                                                            id="input_region_name",
                                                    ),
                                                    ],
                                                    className="mb-3",
                                            ), 
                                            
                                            dbc.InputGroup(
                                                    [
                                                    dbc.InputGroupText("Département", style={"width":"120px"}),
                                                    dbc.Select(
                                                            options=[{"label":n, "value":n} for n in counties_list],
                                                            id="input_county_name",
                                                            #disabled=True,
                                                    ),
                                                    ],
                                                    className="mb-3",
                                            ), 
                                            
                                            dbc.Row(
                                                [
                                                dbc.Col(
                                                    [
                                                    dbc.InputGroup(
                                                            [
                                                            dbc.InputGroupText("Code postal", style={"width":"120px"}), 
                                                            dbc.Input(
                                                                placeholder="28000",
                                                                debounce=True, 
                                                                id="input_city_zip_code",
                                                            ),
                                                            
                                                            dbc.Popover(
                                                                [
                                                                dbc.PopoverHeader("Conseil !", style={"backgroundColor":"green", "color":"white"}),
                                                                dbc.PopoverBody("Le code peut comporter un espace."),
                                                                ],
                                                                target="input_city_zip_code",
                                                                trigger="legacy",
                                                                placement="top",
                                                            ),
                                                            
                                                            ],
                                                            className="mb-3",
                                                    ),
                                                    ],
                                                ), 
                                                
                                                dbc.Col(
                                                    [
                                                    dbc.InputGroup(
                                                            [
                                                            dbc.InputGroupText("Commune *", style={"width":"120px"}), 
                                                            dbc.Select(
                                                                options="", # [{"label":n, "value":n} for n in cities_list],
                                                                id="input_city_name",
                                                                valid=False
                                                            ),
                                                            ],
                                                            className="mb-3",
                                                    ),
                                                    ],
                                                ), 
                                                    
                                                ]
                                            ),

                                            dbc.Label(
                                                "* La personne morale ou physique doit être associée à une commune principale.", 
                                                style={"font-size":"11px"}
                                            ),
                                                
                                            dbc.Row([
                                                dbc.Col([
                                                    dcc.Graph(
                                                        id="form_graph_location",
                                                        figure=plot_map(geo.loc[geo.city_name == "Rivière-Salée"])     ## Don't look up !
                                                    ),
                                                ]),
                                            ],justify='center'), 
                                                
                                            ],
                                            item_id="form_location",
                                            title="Localisation",
                                    ),  
                                      
                                    dbc.AccordionItem(
                                            [
                                            
                                            dbc.InputGroup(
                                                    [
                                                    dbc.InputGroupText("Domaines d'expertise *", style={"width":"180px"}),
                                                    dbc.Col(
                                                        [                                     
                                                        dbc.Checklist(
                                                            options=[{"label":n, "value":n} for n in fields_list],
                                                            value="",
                                                            id="input_activity_field",                                                    
                                                        ),
                                                        ],
                                                        style={'padding' : '10px'},
                                                    ),
                                                    ],
                                                    style={'paddingBottom' : '20px'},
                                            ),

                                            dbc.Label(
                                                "* Au moins un domaine doit être sélectionné.", 
                                                style={"font-size":"11px"}
                                            ),
                                            

                                            dbc.Col(
                                                [  
                                                dbc.InputGroup(
                                                        [
                                                        dbc.InputGroupText("Rayon d'action (km)", style={"width":"180px"}),
                                                        dbc.Input(
                                                            id="input_activity_reach",
                                                            value="10",
                                                            placeholder="10", 
                                                            type="number",
                                                            min=0, 
                                                            max=500,
                                                            step=10
                                                        ),
                                                        ],
                                                        className="mb-3",
                                                ),
                                                ],width=6, 
                                            ),
                                            
                                        
                                            dbc.Checklist(
                                                    options=[{"label": "Télétravail", "value": 1}],
                                                    value="",
                                                    id="input_activity_remote",
                                                    switch=True,
                                            ),
                                                
                                            ],
                                            item_id="form_activity",
                                            title="Activité",
                                    ),
                                    
                                    dbc.AccordionItem(
                                            [
                                                
                                            dbc.Checklist(
                                                    options=[{"label": "Expert vérifié", "value": 1}],
                                                    value="",
                                                    id="input_check",
                                                    switch=True,
                                            ),
                                                
                                            html.Div(
                                                [  
                                                 
                                                dbc.InputGroup(
                                                        [
                                                        dbc.InputGroupText("Dernier contact", style={"width":"180px"}),
                                                        dcc.DatePickerSingle(
                                                                id='input_last_contact',
                                                                min_date_allowed=date(2022, 1, 1),
                                                                initial_visible_month=date.today(),
                                                                #date=date(2017, 8, 25)
                                                                month_format='MMMM Y',
                                                                display_format='DD / MM / YY',
                                                                clearable=True,
                                                                with_portal=True,
                                                                disabled =True,
                                                        ),
                                                        ],
                                                ),
                                                ],
                                                style={"marginTop":"20px"}
                                            ),    
                                                
                                                
                                            ],
                                            item_id="form_verification",
                                            title="Vérification",
                                    ),
                                    
                                    
                                    
                                    ],
                                    id="form_provider",
                                    start_collapsed=True, 
                            )
                            
                        ],width=6
                        ),
                        
                        
                        
                        dbc.Col(
                            [                           
                            
                            dbc.Card(
                                [
                                dbc.CardHeader("Résumé", style={"backgroundColor":"#fcb636", "color":"white", "textAlign":"center", "fontSize":"20px","height": "50px"}),
                                

                                dbc.CardBody(
                                        [
                                        dbc.Table([
                                            html.Tbody([
                                                html.Tr([
                                                    html.Td(html.H6("Identité", className="card-title")),
                                                    html.Td(
                                                        html.P(
                                                            "",
                                                            id = "abstract_identity",
                                                            className="card-text",
                                                        ),
                                                    ),
                                                ]),
                                                
                                                html.Tr([
                                                    html.Td(html.H6("Moyens de contact", className="card-title")),
                                                    html.Td(
                                                        html.P(
                                                            "",
                                                            id = "abstract_contact",
                                                            className="card-text",
                                                        ),
                                                    ),
                                                ]),
                                                
                                                html.Tr([
                                                    html.Td(html.H6("Localisation", className="card-title")),
                                                    html.Td(
                                                        html.P(
                                                            "",
                                                            id = "abstract_location",
                                                            className="card-text",
                                                        ),
                                                    ),
                                                ]),
                                                
                                                html.Tr([
                                                    html.Td(html.H6("Activité", className="card-title")),
                                                    html.Td(
                                                        html.P(
                                                            "",
                                                            id = "abstract_activity",
                                                            className="card-text",
                                                        ),
                                                    ),
                                                ]),
                                                
                                                html.Tr([
                                                    html.Td(html.H6("Vérification", className="card-title")),
                                                    html.Td(
                                                        html.P(
                                                            "",
                                                            id = "abstract_verification",
                                                            className="card-text",
                                                        ),
                                                    ),
                                                ]),
                                                
                                            ],
                                            style={"textAlign":"left"}
                                            ), 
                                        ],
                                        responsive=True,
                                        
                                        ),
                                        
                                        ],
                                        className="mb-3",

                                ),

                                 
                                dbc.Row(
                                    [
                                    dbc.Col(html.H6("Remplissage :"), width=3, style={"paddingLeft":"30px"}),
                                    dbc.Col(dbc.Progress(id="form_progress", label="", value=0, color = "green", animated=True, striped=True, style={"height": "20px"}), width=8),
                                    ], 
                                    style={"paddingTop":"20px"}
                                ),
                                

                                dbc.Row(
                                    [
                                    html.Div(
                                        [    
                                        dbc.Button(
                                            "Création", 
                                            id="creation_form_valid_btn", 
                                            color="success", 
                                            n_clicks=0, 
                                            disabled=True
                                        ),
                                        ],
                                        className="d-grid gap-2 col-4",
                                    ),
                                
                                    html.Div(
                                        [  
                                        dbc.Button(
                                            "Effacer", 
                                            id="creation_form_delete_btn", 
                                            color="danger", 
                                            n_clicks=0
                                        ),
                                        ],
                                        className="d-grid gap-2 col-4",
                                    ),
                                    
                                    dbc.Modal(
                                        [
                                        dbc.ModalHeader(
                                            dbc.ModalTitle("Effacer"), 
                                            close_button=False
                                        ),
                                        dbc.ModalBody("Cette action va effacer tout le contenu du formulaire."),
                                        dbc.ModalFooter(
                                                [
                                                html.Div(
                                                    [
                                                    dbc.Button(
                                                        "Annuler", 
                                                        id="cleaning_cancel", 
                                                        n_clicks=0,
                                                        color="success"
                                                    ),
                                                    ],
                                                    className="d-grid gap-2 col-4"
                                                ),
                                                html.Div(
                                                    [
                                                    dbc.Button(
                                                        "Confirmer", 
                                                        id="cleaning_valid", 
                                                        n_clicks=0,
                                                        color="danger"
                                                    ),
                                                    ],
                                                    className="d-grid gap-2 col-4"
                                                ),
                                                ],
                                                className="mb-3",                                        
                                                    ## TO DO : centrer les deux boutons.
                                        ),
                                        ],
                                        id="cleaning_modal",
                                        keyboard=False,
                                        backdrop="static",
                                        centered=True,
                                        is_open=False,
                                        
                                    ),
                                    
                                    dbc.Modal(
                                        [
                                            dbc.ModalHeader(dbc.ModalTitle("Confirmation !")),
                                            dbc.ModalBody("Le formulaire est bien réinitialisé."),
                                        ],
                                        id="cleaning_confirmation_modal",
                                        keyboard=False,
                                        backdrop="static",
                                        centered=True,
                                        is_open=False,
                                    ),
                                    
                                    dbc.Modal(
                                        [
                                            dbc.ModalHeader(
                                                dbc.ModalTitle("Création"), 
                                                close_button=False
                                            ),
                                            dbc.ModalBody("Cette action va créer des lignes au sein de la base de données."),
                                            dbc.ModalFooter(
                                                    [
                                                    html.Div(
                                                        [
                                                        dbc.Button(
                                                            "Annuler", 
                                                            id="creation_cancel", 
                                                            n_clicks=0,
                                                            color="success"
                                                        ),
                                                        ],
                                                        className="d-grid gap-2 col-4",
                                                    ),
                                                    html.Div(
                                                        [
                                                        dbc.Button(
                                                            "Confirmer", 
                                                            id="creation_valid", 
                                                            n_clicks=0,
                                                            color="danger"
                                                        ),
                                                        ],
                                                        className="d-grid gap-2 col-4",
                                                    ),
                                                    ],
                                                    className="mb-3",
                                                    
                                                    ## TO DO : centrer les deux boutons.
                                                
                                                
                                            ),
                                        ],
                                        id="creation_modal",
                                        keyboard=False,
                                        backdrop="static",
                                        centered=True,
                                        is_open=False,
                                        
                                    ),
                                    
                                    dbc.Modal(
                                        [
                                            dbc.ModalHeader(dbc.ModalTitle("Confirmation !")),
                                            dbc.ModalBody("L'expert a bien été créé dans la base de données."),
                                        ],
                                        id="creating_confirmation_modal",
                                        keyboard=False,
                                        backdrop="static",
                                        centered=True,
                                        is_open=False,
                                    ),
                                    
                                    
                                    ],
                                    justify='center',
                                    style={"padding":"20px"}
                                
                                ), 
                                        

                                ],
                            ),
                            
                            ],
                            width=6, 
                        ),
                                                   
                        ],
                    ),
                    
                        
                    ],
                    style={
                        "paddingLeft": "20px",
                        "paddingRight": "20px",
                        }
                    ),









