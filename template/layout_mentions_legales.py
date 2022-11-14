from dash import Dash, dcc, html
import dash_bootstrap_components as dbc



legal_content = html.Div(

                    dbc.Row(
                        dbc.Col(
                            [
                            html.H3(
                                "Mentions légales",
                                style={
                                    "textAlign":"center",
                                    "fontWeight":"bold",
                                    "color":"black",
                                    "marginBottom":"40px"
                                    }
                            ),
                            
                            html.P(
                                "Conformément aux dispositions de la loi n° 2004-575 du 21 juin 2004 pour la confiance en l'économie numérique, il est précisé aux utilisateurs du site 'NetBizUp_xp' l'identité des différents intervenants dans le cadre de sa réalisation et de son suivi."
                            ),
 
                            html.H5(
                                "Edition du site",
                                style={
                                    "textAlign":"left",
                                    "fontWeight":"bold",
                                    "color":"black",
                                    "marginTop":"30px",
                                    }
                            ),
 
                            html.P(
                                "Le présent site, accessible à l’URL www.netbizup_xp.fr (le « Site »), est édité par :"
                            ),
                            html.P(
                                "BUSINESS COMPASS, société par actions simplifiée à associé unique (SASU) au capital de 20 000 euros, inscrite au R.C.S. de Chartres sous le numéro 899 014 195, dont le siège social est situé au 7 rue Auguste Rodin 28630 Le Coudray, représentée par Marie Sarafian dûment habilitée"
                            ),
                            html.P(
                                "Le numéro individuel TVA de l’éditeur est : FR 83 899014195."    
                            ),

                            html.H5(
                                "Hébergement",
                                style={
                                    "textAlign":"left",
                                    "fontWeight":"bold",
                                    "color":"black",
                                    "marginTop":"30px",
                                    
                                    }
                            ),
                            html.P(
                                "Le Site est hébergé par la société OVH SAS, situé 2 rue Kellermann - BP 80157 - 59053 Roubaix Cedex 1, (contact téléphonique ou email : 1007)."
                            ),

                            html.H5(
                                "Directeur de publication",
                                style={
                                    "textAlign":"left",
                                    "fontWeight":"bold",
                                    "color":"black",
                                    "marginTop":"30px",
                                    }
                            ),
                            html.P(
                                "La Directrice de la publication du Site est Marie Sarafian."
                            ),

                            html.H5(
                                "Nous contacter",
                                style={
                                    "textAlign":"left",
                                    "fontWeight":"bold",
                                    "color":"black",
                                    "marginTop":"30px",
                                    }
                            ),
                            html.P(
                                "Par téléphone : +33 X XX XX XX XX"
                            ),
                            html.P(
                                "Par email : contact@netbizup.fr"
                            ),
                            html.P(
                                "Par courrier : 7 rue Auguste Rodin 28630 Le Coudray"
                            ),

                            ],
                            width=8
                        ),
                        justify="center"
                        
                        
                        
                    )

                )

