from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from dash.html.Col import Col
import dash_bootstrap_components as dbc

#Local Imports
import callbacks
from layouts import board_layout
from layouts import dash_local_components as dlc
from data import data


app = Dash(__name__, suppress_callback_exceptions=True)

#Here we generate both, live and picture layouts

#number of pages for the pagination
n_pages = 3

#Layouts definition
live_layout = [
    html.Div(board_layout.gen_layout('live')),
    html.Div(dlc.gen_download_button('live-down-btn', 'live-download-dataframe')),
    html.Div(dbc.Pagination(id='live-pagination', max_value=n_pages, active_page=1))
    ]

picture_layout = [
    html.Div(board_layout.gen_layout('pic')),
    html.Div(dlc.gen_download_button('pic-down-btn', 'pic-download-dataframe')),
    html.Div(dbc.Pagination(id='pic-pagination', max_value=n_pages, active_page=1))
    ]

app.layout = html.Div([
    dbc.Row(
        dbc.Col(html.H1('Nombre Del Tablero'))
    ),
    dcc.Tabs(
        [dcc.Tab(label='En vivo', value='live-tab'),
         dcc.Tab(label='Fotografía', value='pic-tab')
        ]
    )
])

#Down Here you will import and create the callbacks

if __name__ == '__main__':
    app.run_server(debug=True)
