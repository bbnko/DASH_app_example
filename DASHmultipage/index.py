# Import DASH modules
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import server
from app import app

# Import all pages from the apps folder
from apps import  home, page1, page2

# Create a top ribbon Menu with page navigation
dropdown = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("Home", href="/home"),
        dbc.DropdownMenuItem("Page 1: Scatter", href="/page1"),
        dbc.DropdownMenuItem("Page 2: Data Table", href="/page2")
        
    ],
    nav = True,
    in_navbar = True,
    label = "Menu",
)

# Add logo to the navigation bar
navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="/assets/logo.png", height="30px")),
                        dbc.Col(dbc.NavbarBrand("DASHboard", className="ml-2")),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="/home",
            ),
            dbc.NavbarToggler(id="navbar-toggler2"),
            dbc.Collapse(
                dbc.Nav(
                    # right align dropdown menu with ml-auto className
                    [dropdown], className="ml-auto", navbar=True
                ),
                id="navbar-collapse2",
                navbar=True,
            ),
        ]
    ),
    color="dark",
    dark=True,
    className="mb-4",
)

def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

for i in [2]:
    app.callback(
        Output(f"navbar-collapse{i}", "is_open"),
        [Input(f"navbar-toggler{i}", "n_clicks")],
        [State(f"navbar-collapse{i}", "is_open")],
    )(toggle_navbar_collapse)

# Embedding the navigation bar
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content')
])

# Adding callbacks for menu buttons
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/home':
        return home.layout
    elif pathname == '/page1':
        return page1.layout
    elif pathname == '/page2':
        return page2.layout
    else:
        return home.layout

# Running the app
if __name__ == '__main__':
    app.run_server(debug=True)