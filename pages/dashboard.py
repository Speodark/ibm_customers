import vaex
from dash import html, dcc
from layout import header, sub_header
from components import (
    card,
    category_switch
)
import uuid
from pprint import pprint
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc

df = vaex.open("assets/data/ibm-customers.hdf5")


def dashboard():
    return html.Div(
        className='dashboard',
        children=[
            html.Div(
                className='dashboard__filter',
                children=[
                    category_switch('Gender',['Male', 'Female'])
                ]
            ),
            html.Div(
                className='dashboard__info',
                children=[

                ]
            )
        ]
    )
