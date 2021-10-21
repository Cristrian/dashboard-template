from dash import html, dcc
import dash_bootstrap_components as dbc

#Local Imports
from layouts import dash_local_components as dlc
from data import data

def gen_layout(appname):

    
    #Components,Here You will create the components that are
    #going to be included in the layout.

    example_component = [
        dbc.Row([
            dbc.Col(dbc.Card('This is a card in column 1')),
            dbc.Col(dbc.Card('This is a card in column 2')),
        ])
    ]

    #graphics, here are the graphics 

    graphics = html.Div(id=f'{appname}-graphics')

    #General layout

    layout = dbc.Container(
        [
            html.Div(example_component),
            html.Div(graphics)
        ]

    )
    return layout

def gen_graphics_layout(page: int, appname: str):
    """Generates graphics layout.
    Based on the dashboard page it generates the graphics layout
    
    Args:
        page: The number of the page.
        appname: the name of the app for the id's

    Returns:
        A list containing the graphics, ready to be pass as a children 
        of a html component.
    """
    if page == 1:
        graphics = []
    elif page ==2: 
        graphics = []
    return graphics