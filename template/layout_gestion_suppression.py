from dash import Dash, dcc, html, dash_table
import dash_daq as daq

import dash_bootstrap_components as dbc

# Functions
from components.functions import big_one_building


removing_content = dbc.Card(
                [
                    
                dbc.CardHeader(
                        html.H1(
                                "Suppression",
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
                                                    id= "reset_table_to_delete",
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
                                                    id="kpi_rows_selected_to_delete", 
                                                    style={"fontWeight":"bold", "color":"red", "fontSize":"30px"}
                                                ),
                                                html.Br(),
                                                html.H6("Nombre d'experts sélectionnés différents", style={"fontWeight":"bold"}),
                                                html.H6(
                                                    "...", 
                                                    id="kpi_experts_nb_to_delete", 
                                                    style={"fontWeight":"bold", "color":"red", "fontSize":"30px"}
                                                ),
                                                html.Br(),
                                                
                                                
                                                ],
                                                style={"textAlign":"center"}
                                            ),            
                                        ),


                                        dbc.Row(
                                            [                               
                                            html.H6("Zoom sur la sélection", style={"fontWeight":"bold"}),
                                            daq.BooleanSwitch(id='switch_focus_to_delete', color="#fcb636", on=False),
                                            ],
                                            style={"textAlign":"center", "paddingBottom":"20px"}
                                        ), 
                                    
                                    
                                        dbc.Row(
                                            dbc.Col(
                                                [
                                                dbc.Button(
                                                    children="Suppression",
                                                    id= "removing_rows_selected_btn",
                                                    color="danger",
                                                    style={"width": "150px",
                                                            "paddingTop":"10px",
                                                            "paddingBottom":"10px",
                                                            "borderRadius":"10px",
                                                            "fontSize":"17px",
                                                            "color": "white",
                                                            #"backgroundColor":"#FFB401",
                                                            #"border":"2px solid #555555"
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
                                                dbc.ModalTitle("Supprimer"), 
                                                close_button=False
                                            ),
                                            dbc.ModalBody(
                                                    "Cette action ne va rien supprimer.",
                                                    id="removing_modal_body"
                                            ),
                                            dbc.ModalFooter(
                                                    [
                                                    html.Div(
                                                        [
                                                        dbc.Button(
                                                            "Annuler", 
                                                            id="removing_cancel", 
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
                                                            id="removing_valid", 
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
                                            id="removing_modal",
                                            keyboard=False,
                                            backdrop="static",
                                            centered=True,
                                            is_open=False,
                                            
                                        ),
                                    
                                    
                                        dbc.Modal(
                                            [
                                                dbc.ModalHeader(dbc.ModalTitle("Confirmation !")),
                                                dbc.ModalBody("La sélection a bien été supprimée. Elle restera dans la table, mais ne sera plus considérée comme active."),
                                            ],
                                            id="removing_confirmation_modal",
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
                                                id='table_to_delete',
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
                                                        #"hideable": True,
                                                    }, 
                                                    {"name": ["Localisation","Département"], 
                                                        "id": "county_name", 
                                                        #"deletable": True,
                                                        #"hideable": True,
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
                                                row_selectable="multi",
                                                
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
                                                            'backgroundColor':"#fcb636",
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
                                                
                                                # style_data_conditional=[
                                                #                 {
                                                #                     'if': {
                                                #                         'state': 'selected '  # 'active' | 'selected'
                                                #                     },
                                                #                     'backgroundColor': 'yellow',
                                                #                 }
                                                # ],
                                                
                                               
                                                        
                                    ),
                                    ],
                                    width=10
                                
                                ),
                                ],
                            ),
                            ],
                            item_id="selection_step_to_delete",
                            title="Sélection des données",
                        ),
                        ],
                        id="selection_module_to_delete",
                        start_collapsed=False,
                        flush=True, 
                ),
                                  
                  
                    
                ],
                style={
                    "paddingLeft": "20px",
                    "paddingRight": "20px",
                    }
            )
                    