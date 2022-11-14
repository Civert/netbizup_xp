#from cProfile import label
from dash import Dash, dcc, html, dash_table
import dash_bootstrap_components as dbc

from datetime import date

# Functions
from components.functions import big_one_building, geo_loading, fields_loading

# Data

geo = geo_loading()
fields = fields_loading()

fields_list = sorted(list(fields.title.unique()))
counties_list = sorted(list(geo.county_name.unique()))
regions_list = sorted(list(geo.region_name.unique()))



expert_profile = dbc.Card(
                    [
                
                    dbc.Row(
                        [
                        dbc.Col(
                            [

                                
                            dbc.InputGroup(
                                    [
                                    dbc.InputGroupText("Société *", style={"width":"85px"}), 
                                    dbc.Input(
                                        value='', 
                                        id="compagny_name_to_modify", 
                                        type="text",
                                        valid=False
                                    ),
                                    ],
                                    className="mb-3",
                            ), 

                            dbc.InputGroup(
                                    [
                                    dbc.InputGroupText("Nom *", style={"width":"85px"}), 
                                    dbc.Input(
                                        value='',
                                        id="last_name_to_modify",
                                        type="text",
                                        valid=False
                                    ),
                                    ],
                                    className="mb-3",
                            ),

                            dbc.InputGroup(
                                    [
                                    dbc.InputGroupText("Prénom", style={"width":"85px"}),
                                    dbc.Input(
                                        value='', 
                                        id="first_name_to_modify", 
                                        type="text"
                                    ),
                                    ],
                                    className="mb-3",
                            ),

                                
                            dbc.InputGroup(
                                    [
                                    dbc.InputGroupText("Courriel *", style={"width":"85px"}),
                                    dbc.Input(
                                        value='', 
                                        id="email_to_modify", 
                                        type="email",
                                        valid=False
                                    ),
                                    ],
                                    className="mb-3",
                            ), 


                            dbc.InputGroup(
                                    [
                                    dbc.InputGroupText("Tél. n°1 *", style={"width":"85px"}),
                                    dbc.Input(
                                        value='', 
                                        id="phone_1_to_modify", 
                                        type="tel", 
                                        valid=False
                                    ),
                                
                                    ],
                                    className="mb-3",
                            ),


                            dbc.InputGroup(
                                    [
                                    dbc.InputGroupText("Tél. n°2 *", style={"width":"85px"}),
                                    dbc.Input(
                                        value='', 
                                        id="phone_2_to_modify", 
                                        type="tel", 
                                        valid=False
                                    ),
                                    
                                    ],
                                    className="mb-3",
                            ),

                            dbc.InputGroup(
                                    [
                                    dbc.InputGroupText("Lien", style={"width":"85px"}), 
                                    dbc.Input(
                                        value='', 
                                        id="website_to_modify", 
                                        type="text"
                                    ),
                                    ],
                                    className="mb-3",
                            ),
                                

                            ],
                            width=4
                        ),
                        
                        dbc.Col(
                            [
                                
                            dbc.InputGroup(
                                    [
                                    dbc.InputGroupText("Région", style={"width":"120px"}),
                                    dbc.Select(
                                            options=[{"label":n, "value":n} for n in regions_list],
                                            id="region_name_to_modify",
                                    ),
                                    ],
                                    className="mb-3",
                            ), 
                            
                            dbc.InputGroup(
                                    [
                                    dbc.InputGroupText("Département", style={"width":"120px"}),
                                    dbc.Select(
                                            options=[{"label":n, "value":n} for n in counties_list],
                                            id="county_name_to_modify",
                                    ),
                                    ],
                                    className="mb-3",
                            ), 
                            

                            dbc.InputGroup(
                                    [
                                    dbc.InputGroupText("Commune *", style={"width":"120px"}),                                     
                                    dbc.Select(
                                        value="",
                                        options=[], #[{"label":n, "value":n} for n in cities_list],
                                        id="city_name_to_modify",
                                    ),
                                    
                                    
                                    
                                    ],
                                    className="mb-3",
                            ),
                            
                            dbc.InputGroup(
                                    [
                                    dbc.InputGroupText("Code postal", style={"width":"120px"}), 
                                    dbc.Input(
                                        value="",
                                        id="city_zip_code_to_modify",
                                        disabled=True,
                                        #style={"backgroundColor":"lightgrey"}
                                    ),

                                    ],
                                    className="mb-3",
                            ), 
                            
                                
                            ],
                            width=4
                        ),
                        
                        dbc.Col(
                            [
                                
                            dbc.InputGroup(
                                    [
                                    dbc.InputGroupText("Domaines d'expertise *", style={"width":"180px"}),
                                    dbc.Col(
                                        [                                     
                                        dbc.Checklist(
                                            options=[{"label":n, "value":n} for n in fields_list],
                                            value="",
                                            id="activity_field_to_modify",                                                    
                                        ),
                                        ],
                                        style={'padding' : '10px'},
                                    ),
                                    ],
                                    style={'paddingBottom' : '20px'},
                            ), 
                                
                            
                            dbc.InputGroup(
                                    [
                                    dbc.InputGroupText("Rayon d'action", style={"width":"180px"}),
                                    dbc.Input(
                                        id="activity_reach_to_modify",
                                        value="",
                                        type="number",
                                        min=0, 
                                        max=1000,
                                        step=10
                                    ),
                                    ],
                                    className="mb-3",
                            ), 
                                
                            dbc.Col(
                                [
                                dbc.Checklist(
                                        options=[{"label": "Télétravail", "value": 1}],
                                        value="",
                                        id="activity_remote_to_modify",
                                        switch=True,
                                ),
                                ],
                                width=4,                        
                            ), 
                                
                                
                            dbc.Col(
                                [ 
                                dbc.Checklist(
                                        options=[{"label": "Expert vérifié", "value": 1}],
                                        value=[],
                                        id="check_to_modify",
                                        switch=True,
                                ),
                                ],
                                width=4,
                                style={"marginBottom":"10px"}                             
                            ), 
                                
                                
                            dbc.InputGroup(
                                    [
                                    dbc.InputGroupText("Dernier contact", style={"width":"180px"}),
                                    dcc.DatePickerSingle(
                                            id='last_contact_to_modify',
                                            min_date_allowed=date(2022, 1, 1),
                                            initial_visible_month=date.today(),
                                            # date="", #date.today(),
                                            month_format='MMMM Y',
                                            display_format='DD / MM / YY',
                                            clearable=True,
                                            with_portal=True,
                                            disabled =True
                                    ),
                                    ],
                            ),
  
                            
                            ],
                            width=4
                        ),
                        ],
                    ),
                    
                    ],
                    color="light",
                    outline=True,
                    
                )






change_content = dbc.Card(
                [
                                       
                    

                dbc.CardHeader(
                        html.H1(
                                "Modification",
                                style={
                                    "textAlign":"center",
                                    "fontWeight":"bold",
                                    "color":"#F35E29"
                                    }
                        ),
                        style={"backgroundColor":"white"},
                ),
                 
                 
                dbc.Accordion(
                        [
                            dbc.AccordionItem(
                                [
                                dbc.Row(
                                    [
                                    
                                    dbc.Col(
                                        [
                                        
                                        dbc.Card(
                                            [
                                                
                                            dbc.Row(
                                                dbc.Col(
                                                    [
                                                    dbc.Button(
                                                        children="Reset",
                                                        id= "reset_table_to_modify",
                                                        style={"width": "150px",
                                                               "paddingTop":"10px",
                                                               "paddingBottom":"10px",
                                                               "borderRadius":"10px",
                                                               "fontSize":"17px",
                                                               "color": "#585858",
                                                               "backgroundColor":"#FFB401",
                                                               "border":"2px solid #555555"
                                                               }, 
                                                        n_clicks=0
                                                    ),
                                                    ],
                                                    style={"textAlign":"center",
                                                        "paddingBottom":"50px"
                                                        },
                                                ),
                                            ),
                                            
                                            
                                            dbc.Row(
                                                dbc.Col(
                                                    [
                                                    html.H6("Lignes sélectionnées", style={"fontWeight":"bold"}),
                                                    html.H6(
                                                        "...", 
                                                        id="kpi_rows_selected_to_modify", 
                                                        style={"fontWeight":"bold", "color":"red", "fontSize":"30px"}
                                                    ),
                                                    # html.Br(),
                                                    # html.H6("Nombre d'experts sélectionnés différents", style={"fontWeight":"bold"}),
                                                    # html.H6(
                                                    #     "...", 
                                                    #     id="kpi_experts_nb_to_modify", 
                                                    #     style={"fontWeight":"bold", "color":"red", "fontSize":"30px"}
                                                    # ),
                                                    # html.Br(),
                                                    
                                                    ],
                                                    style={"textAlign":"center",
                                                        "paddingBottom":"50px"}
                                                ),            
                                            ),
                                            
                                            dbc.Row(
                                                dbc.Col(
                                                    [
                                                    dbc.Button(
                                                        children="Selectionner",
                                                        id= "select_one_to_modify",
                                                        color="success",
                                                        style={"width": "150px",
                                                               "paddingTop":"10px",
                                                               "paddingBottom":"10px",
                                                               "borderRadius":"10px",
                                                               "fontSize":"17px",
                                                               "color": "white",
                                                            #    "backgroundColor":"#FFB401",
                                                            #    "border":"2px solid #555555"
                                                               }, 
                                                        n_clicks=0
                                                    ),
                                                   
                                                    
                                                    ],
                                                    style={"textAlign":"center",
                                                        },
                                                ),
                                            ),  
                                            
                                            
                                            dbc.Modal(
                                                [
                                                dbc.ModalHeader(
                                                    dbc.ModalTitle("Vérification de la sélection"), 
                                                    close_button=False
                                                ),
                                                dbc.ModalBody(
                                                        "Cette action ne va rien modifier ! La sélection d'un expert est recquise.",
                                                        id="change_selection_verification_modal_body"
                                                ),
                                                dbc.ModalFooter(
                                                        [
                                                        html.Div(
                                                            [
                                                            dbc.Button(
                                                                "Annuler", 
                                                                id="change_selection_cancel_btn", 
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
                                                                id="change_selection_valid_btn", 
                                                                n_clicks=0,
                                                                disabled=True,
                                                                color="danger"
                                                            ),
                                                            ],
                                                            className="d-grid gap-2 col-4"
                                                        ),
                                                        ],
                                                        className="mb-3",
                                                    
                                                ),
                                                ],
                                                id="change_selection_modal",
                                                keyboard=False,
                                                backdrop="static",
                                                centered=True,
                                                is_open=False,
                                                
                                            ),
                                            
                                            
                                        dbc.Modal(
                                            [
                                                dbc.ModalHeader(dbc.ModalTitle("Confirmation !")),
                                                dbc.ModalBody("Chargement du profil."),
                                            ],
                                            id="change_selection_confirmation_modal",
                                            keyboard=False,
                                            backdrop="static",
                                            centered=True,
                                            is_open=False,
                                        ),
                                            
                                            
                                            
                                            ],
                                            style={"padding":"20px"}
                                        ),
                                        
                                        
                                        
                                        ],
                                        width=2
                                    ),
                                    
                                    
                                    dbc.Col(
                                        [

                                        dash_table.DataTable(
                                                    id='table_to_modify',
                                                    data=big_one_building().to_dict('records'),

                                                    columns=[
                                                        {"name": ["","id"], 
                                                            "id": "id", 
                                                            #"deletable": True,
                                                            "hideable": True,
                                                        },
                                                        
                                                        
                                                        {"name": ["Historique","Créé le"], 
                                                            "id": "created_at", 
                                                            #"deletable": True,
                                                            "hideable": True,
                                                        },
                                                        {"name": ["Historique","Modifié le"], 
                                                            "id": "updated_at", 
                                                            #"deletable": True,
                                                            "hideable": True,
                                                        },
                                                        {"name": ["Historique","Supprimé le"], 
                                                            "id": "deleted_at", 
                                                            #"deletable": True,
                                                            "hideable": True,
                                                        },
                                                        
                                                        
                                                        {"name": ["Identité","Prénom"], 
                                                            "id": "first_name", 
                                                            #"deletable": True,
                                                            #"hideable": True,
                                                        },
                                                        {"name": ["Identité","Nom"], 
                                                            "id": "last_name", 
                                                            #"deletable": True,
                                                            #"hideable": True,
                                                        },
                                                        {"name": ["Identité","Société"], 
                                                            "id": "compagny_name", 
                                                            #"deletable": True,
                                                            #"hideable": True,
                                                        },

                                                        
                                                        {"name": ["Contacts","Courriel"], 
                                                            "id": "email", 
                                                            #"deletable": True,
                                                            "hideable": True,
                                                        },
                                                        {"name": ["Contacts","Tél. 1"], 
                                                            "id": "phone_1", 
                                                            #"deletable": True,
                                                            "hideable": True,
                                                        },
                                                        {"name": ["Contacts","Tél. 2"], 
                                                            "id": "phone_2", 
                                                            #"deletable": True,
                                                            "hideable": True,
                                                        },
                                                        {"name": ["Contacts","Lien"], 
                                                            "id": "website", 
                                                            #"deletable": True,
                                                            "hideable": True,
                                                        }, 
                                                        
                                                        
                                                        {"name": ["Localisation","Code postal"], 
                                                            "id": "city_zip_code", 
                                                            #"deletable": True,
                                                            "hideable": True,
                                                        }, 
                                                        {"name": ["Localisation","Commune"], 
                                                            "id": "city_name", 
                                                            #"deletable": True,
                                                            "hideable": True,
                                                        }, 
                                                        {"name": ["Localisation","Département"], 
                                                            "id": "county_name", 
                                                            #"deletable": True,
                                                            "hideable": True,
                                                        }, 
                                                        {"name": ["Localisation","Région"], 
                                                            "id": "region_name", 
                                                            #"deletable": True,
                                                            "hideable": True,
                                                        }, 
                                                        {"name": ["Localisation","Latitude"], 
                                                            "id": "lat", 
                                                            #"deletable": True,
                                                            "hideable": True,
                                                        }, 
                                                        {"name": ["Localisation","Longitude"], 
                                                            "id": "lon", 
                                                            #"deletable": True,
                                                            "hideable": True,
                                                        }, 
                                                        
                                                        
                                                        {"name": ["Activité","Domaine"], 
                                                            "id": "field", 
                                                            #"deletable": True,
                                                            #"hideable": True,
                                                        }, 
                                                        {"name": ["Activité","Rayon d'action"], 
                                                            "id": "reach", 
                                                            #"deletable": True,
                                                            "hideable": True,
                                                        }, 
                                                        {"name": ["Activité","Télétravail"], 
                                                            "id": "remote_work", 
                                                            #"deletable": True,
                                                            "hideable": True,
                                                        }, 

                                                        
                                                        {"name": ["Vérification","check"], 
                                                            "id": "check", 
                                                            #"deletable": True,
                                                            "hideable": True,
                                                        }, 
                                                        {"name": ["Vérification","last_contact"], 
                                                            "id": "last_contact", 
                                                            #"deletable": True,
                                                            "hideable": True,
                                                        }, 
                                                    ],
                                                    
                                                    hidden_columns=["id","created_at", "updated_at", "deleted_at", "city_zip_code", "region_name", "reach", "remote_work", "check", "last_contact", "lat", "lon"],
 
                                                    page_size=10,
                                                    
                                                    merge_duplicate_headers=True,
                                                    
                                                    fixed_rows={'headers': True},
                                                    
                                                    filter_action="native",
                                                    
                                                    sort_action='native',
                                                    sort_mode="multi",
                                                    
                                                    row_deletable=True,
                                                    row_selectable="single",
                                                    
                                                    tooltip_data=[
                                                        {"website" : {"value": str(row["website"]) if str(row["website"])!="nan" else "", "type":"markdown"},} for row in big_one_building().to_dict("records")
                                                        ],
                                                    tooltip_delay=0,
                                                    tooltip_duration=None,
                                                    
                                                    style_table={
                                                            #'border': 'thin lightgrey solid',
                                                            'border': 'thin black solid',
                                                            'height': '400px', 
                                                            'overflowY': 'auto'
                                                    },
                                                    
                                                    style_header={
                                                                'backgroundColor':"#FFB401",
                                                                'color' : "black",
                                                                'border': 'thin black solid',
                                                                'fontWeight':'bold',
                                                                'textAlign':'center',
                                                                'font-size': '16px',
                                                    },
                                                    
                                                    style_cell={'textAlign':'left',
                                                                #'font_family': 'cursive',
                                                                'font-size': '14px',
                                                                'width':'10%',
                                                                                                                
                                                                #'backgroundColor':"lightgrey",
                                                                #'border': 'thin white solid',
                                                                #'color' : "black",
                                                                
                                                                'overflow': 'hidden',
                                                                'textOverflow': 'ellipsis',
                                                                'minWidth': 150,
                                                                'maxWidth': 300
                                                                
                                                    },
                                                    
                                                    style_cell_conditional=[
                                                                {'if': {'column_id': 'id'},
                                                                'minWidth': 50,
                                                                'maxWidth': 50,
                                                                'textAlign':'right',
                                                                'paddingRight':'10px',
                                                                },
                                                                
                                                                {'if': {'column_id': 'phone_1'},
                                                                'textAlign':'center',
                                                                'minWidth': 100,
                                                                'maxWidth': 100,
                                                                },

                                                                {'if': {'column_id': 'phone_2'},
                                                                'textAlign':'center',
                                                                'minWidth': 100,
                                                                'maxWidth': 100,
                                                                },

                                                                {'if': {'column_id': 'city_zip_code'},
                                                                'textAlign':'center',
                                                                'minWidth': 120,
                                                                'maxWidth': 120,
                                                                },


                                                                {'if': {'column_id': 'reach'},
                                                                'textAlign':'center',
                                                                },

                                                                {'if': {'column_id': 'remote_work'},
                                                                'textAlign':'center',
                                                                },
                                                                
                                                                {'if': {'column_id': 'check'},
                                                                'textAlign':'center',
                                                                },          
                                                                

                                                    ],
                                                        
                                        ),
                                        ],
                                        width=10
                                    
                                    ),

                                    ],
                                ),
                    
                                    
                                ],
                                item_id="selection_step_to_modify",
                                title="Sélection de l'expert",
                                
                            ),
                            dbc.AccordionItem(
                                [
                                expert_profile,
                                    
                                dbc.Row(
                                    [
                                    dbc.Col(
                                        [
                                        dbc.Button(
                                            "Annuler", 
                                            id="modification_cancellation_btn", 
                                            n_clicks=0,
                                            color="success"
                                        ),
                                        
                                        
                                        dbc.Modal(
                                            [
                                            dbc.ModalHeader(
                                                dbc.ModalTitle("Suppression des modifications"), 
                                                close_button=False
                                            ),
                                            dbc.ModalBody(
                                                    "Cette action va supprimer les éventuelles propositions de modification. Le profil va revenir à son état initial.",
                                                    id="change_cancel_modal_body"
                                            ),
                                            dbc.ModalFooter(
                                                    [
                                                    html.Div(
                                                        [
                                                        dbc.Button(
                                                            "Annuler", 
                                                            id="modification_cancellation_cancel_btn", 
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
                                                            id="modification_cancellation_valid_btn", 
                                                            n_clicks=0,
                                                            color="danger"
                                                        ),
                                                        ],
                                                        className="d-grid gap-2 col-4"
                                                    ),
                                                    ],
                                                    className="mb-3",
                                                
                                            ),
                                            ],
                                            id="modification_cancellation_modal",
                                            keyboard=False,
                                            backdrop="static",
                                            centered=True,
                                            is_open=False,
                                            
                                        ),
                                        
                                        
                                        dbc.Modal(
                                            [
                                                dbc.ModalHeader(dbc.ModalTitle("Confirmation !")),
                                                dbc.ModalBody("Le profil en cours est rechargé."),
                                            ],
                                            id="modification_cancellation_confirmation_modal",
                                            keyboard=False,
                                            backdrop="static",
                                            centered=True,
                                            is_open=False,
                                        ),
                                        
                                        
                                        
                                        ],
                                        className="d-grid gap-2 col-2"
                                    ),
                                    dbc.Col(
                                        [
                                        dbc.Button(
                                            "Modifier", 
                                            id="modification_validation_btn", 
                                            n_clicks=0,
                                            disabled=True,
                                            color="danger"
                                        ),
                                        
                                        
                                        dbc.Modal(
                                            [
                                            dbc.ModalHeader(
                                                dbc.ModalTitle("Validation des modifications"), 
                                                close_button=False
                                            ),
                                            dbc.ModalBody(
                                                    "Cette action va modifier le profil en cours. Souhait à confirmer.",
                                                    id="change_cancel_modal_body"
                                            ),
                                            dbc.ModalFooter(
                                                    [
                                                    html.Div(
                                                        [
                                                        dbc.Button(
                                                            "Annuler", 
                                                            id="modification_validation_cancel_btn", 
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
                                                            id="modification_validation_valid_btn", 
                                                            n_clicks=0,
                                                            color="danger"
                                                        ),
                                                        ],
                                                        className="d-grid gap-2 col-4"
                                                    ),
                                                    ],
                                                    className="mb-3",
                                                
                                            ),
                                            ],
                                            id="modification_validation_modal",
                                            keyboard=False,
                                            backdrop="static",
                                            centered=True,
                                            is_open=False,
                                            
                                        ),
                                        
                                        dbc.Modal(
                                            [
                                                dbc.ModalHeader(dbc.ModalTitle("Confirmation !")),
                                                dbc.ModalBody("Le profil en cours a bien été modifié."),
                                            ],
                                            id="modification_confirmation_modal",
                                            keyboard=False,
                                            backdrop="static",
                                            centered=True,
                                            is_open=False,
                                        ),
                                        
                                        ],
                                        className="d-grid gap-2 col-2"
                                    ),
                                    ],
                                ), 
                                    
                                ],
                                item_id="expert_profile_to_modify",
                                title="Profil expert",
                            ),

                        ],
                        id="modification_steps",
                        flush=True,
                        always_open=True,               # A Laisser le temps du dév et des tests
                        
                        style={"textAlign":"center"}
                    ),
                 
                
                
                
                
                
                ],
                style={
                    "paddingLeft": "20px",
                    "paddingRight": "20px",
                    }
            )