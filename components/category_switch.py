from dash import html, dcc
from dash import Input, Output, ALL, State, MATCH, ctx
import dash_bootstrap_components as dbc
import dash
import uuid
from filter_manager import filter_manager
import ast

def category_switch(column_name, categories, disable_btn=False, id=None, className = ''):
    assert isinstance(column_name, str), "In category_switch component, the column_name variable need to be string"
    assert isinstance(categories, list) or isinstance(categories, tuple), "In category_switch component, the categories variable need to be a list or a tuple"
    assert len(categories) == 2, "In category_switch component, the categories variable need to have 2 exactly categories"
    assert isinstance(categories[0], str) or isinstance(categories[1], str), "In category_switch component, the categories variable the values need to be of type string"
    
    id = str(uuid.uuid4()) if not id else id
    return html.Div(
        className='category-switch ' + className,
        children=[
            # The disable/enable button
            dbc.Checkbox(
                className='category-switch__btn',
                label="Disable",
            ),
            # The switch
            html.Div(
                className='category-switch__switch',
                children=[
                    html.Div(
                        className='switch',
                        children=[
                            dbc.Checkbox(),
                            html.Span(className='switch__slider switch__round')
                        ]
                    )
                ]
            ),
            # The first category element
            html.Span(
                className='category-switch__category category-switch__category--1',
                children=categories[0]
            ),
            # The second category element
            html.Span(
                className='category-switch__category category-switch__category--2',
                children=categories[1]
            ),
            html.Span(
                className='category-switch__title',
                children=column_name
            )
        ]
    )

