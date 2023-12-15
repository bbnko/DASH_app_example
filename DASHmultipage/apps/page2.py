# Import DASH modules
from dash import html
import dash_bootstrap_components as dbc
from dash import dcc, dash_table
from dash.dependencies import Input, Output

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
            dbc.Col(html.H1("Example of Data Table & Export", className="text-center")
                    , className="mb-5 mt-5")
        ]),

        dbc.Row([
            dbc.Col(html.H5(children='Select number of rows to display:'
                                     )
                    , className="mb-4")
            ]),

        dcc.Dropdown(
            id="nrows",
            options=[5, 10, 20, 50],             
            value = 5,
        ),


        dbc.Row([
            dbc.Col(html.H5(children='Data Table:'
                                     )
                    , className="mb-4")
            ]),

        dash_table.DataTable(id ='table',export_format="csv", columns=[
    {'name': 'sepal length (cm)', 'id': 'sepal length (cm)'},    
    {'name': 'sepal width (cm)', 'id': 'sepal width (cm)'},
    {'name': 'petal length (cm)', 'id': 'petal length (cm)'},  
    {'name': 'petal width (cm)', 'id': 'petal width (cm)'},
    {'name': 'target', 'id': 'target'}]      , style_header={'backgroundColor': '#00040a'
                                                                                      , 'color': '#737578'
                                                                                      , 'fontWeight': 'bold'}
                                                                      , style_cell={'padding': '1px'
                                                                                    , 'fontSize': '10'
                                                                                    , 'font-family': 'sans-serif'
                                                                                    , 'textAlign': 'center'
                                                                                    , 'font-color': 'grey'}
                                                                      , style_data={'backgroundColor': '#00040a'
                                                                                    , 'color': '#9c9ea1'}),

    ])

])

#Callback function - use the dropdown to return the table of nrows length
@app.callback(
    Output(component_id = 'table', component_property = 'data'),
    [Input(component_id='nrows', component_property='value')]
)
def update_graph(nrows):
    df2 = df.head(nrows) 
    return df2.to_dict('records')