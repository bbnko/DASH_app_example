# Import DASH modules
import dash
import dash_bootstrap_components as dbc

# Applying a custom theme
# https://bootswatch.com/cyborg/
external_stylesheets = [dbc.themes.CYBORG]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Adding the title to the app
app.title = 'DASHboard'

# Applying the custom template to figures (charts, tables etc)
from dash_bootstrap_templates import load_figure_template
load_figure_template("cyborg")

server = app.server
app.config.suppress_callback_exceptions = True