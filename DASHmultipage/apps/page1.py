# Import DASH modules
from dash import html
import dash_bootstrap_components as dbc
from dash import dcc
from dash.dependencies import Input, Output

# Import visualization library
import plotly.express as px

# Import data handling libraries
import pandas as pd
import numpy as np
from sklearn import datasets

# Import the DASH app
from app import app

# Using an existing dataset as an example
iris = datasets.load_iris()
df = pd.DataFrame(data= np.c_[iris['data'], iris['target']], columns= iris['feature_names'] + ['target'])

# Creating Page layout
# Note: IDs of objects are later used in the callback functions to make buttons lead to an action
layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("Scatter Plot for 2 selected features", className="text-center")
                    , className="mb-5 mt-5")
        ]),
        dbc.Row([
            dbc.Col(html.H5(children='Select 1st feature:'
                                     )
                    , className="mb-4")
            ]),

        dcc.Dropdown(
            id="feature1",
            options=df.drop(columns='target').columns,             
            value = df.drop(columns='target').columns[0],
        ),

        dbc.Row([
            dbc.Col(html.H5(children='Select 2nd feature:'
                                     )
                    , className="mb-4")
            ]),

        dcc.Dropdown(
            id="feature2",
            options=df.drop(columns='target').columns,             
            value = df.drop(columns='target').columns[1],
        ),

        dbc.Row([
            dbc.Col(html.H5(children='Features scatter:'
                                     )
                    , className="mb-4")
            ]),
        
        # Adding Spinner - spinning animation while the data/figure is loading
        dbc.Spinner(children=[dcc.Graph(id="features")],  color="#2e6df6", type="border", fullscreen=True, spinner_style={"width": "10rem", "height": "10rem"})

    ])

])

#Callback function - use dropdowns to build a plot
@app.callback(
    Output(component_id = 'features', component_property = 'figure'),
    [Input(component_id='feature1', component_property='value'),
     Input(component_id='feature2', component_property='value')]
)
def update_graph(feature1, feature2):
    line_fig = px.scatter(df, y=feature1, x=feature2)    
    return line_fig