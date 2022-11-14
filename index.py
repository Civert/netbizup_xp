import components.functions
import components.callbacks_header
import components.callbacks_visualisation_exploration
import components.callbacks_gestion_creation
import components.callbacks_gestion_modification
import components.callbacks_gestion_suppression

from template.header import layout

from app import app,server

#layout rendu par l'application
app.layout = layout

if __name__ == '__main__':
    app.run_server(debug=True)