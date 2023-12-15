from dash import html
import dash_bootstrap_components as dbc

layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("Welcome to the DASHboard example", className="text-center")
                    , className="mb-5 mt-5")
        ]),
        dbc.Row([
            dbc.Col(html.H5(children='Please use the MENU button to navigate though pages'
                                     )
                    , className="mb-4")
            ]),

        dbc.Row([
            dbc.Col(html.H5(children='In case of questions / issues / bugs reach out to https://github.com/bbnko')
                    , className="mb-5")
        ])
    ])

])