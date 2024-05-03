##!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: application.py
# Capitulo: Flujo de Datos
# Autor(es): Perla Velasco & Yonathan Mtz. & Jorge Solís
# Version: 1.0.0 Noviembre 2022
# Descripción:
#
#   Este archivo define la aplicación que sirve la UI y la lógica 
#   del componente
#
#-------------------------------------------------------------------------
from src.view.dashboard import Dashboard
from src.view.mostSelledProducts_fordate import MostSelledProductsForDate
import dash_bootstrap_components as dbc
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State

app = dash.Dash(
    external_stylesheets=[dbc.themes.LUX],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ],
)

app.title = "ETL"

dashboard = Dashboard()

app.layout = dashboard.document()

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    if pathname == '/most-selled-products':
        most_selled_products_for_date_instance = MostSelledProductsForDate()
        return most_selled_products_for_date_instance.document()
    else:
        return dashboard.document()


@app.callback(
    Output('product-list', 'children'),
    [Input('consult-button', 'n_clicks')],
    [State('date-picker', 'start_date'),
     State('date-picker', 'end_date'),
     State('num-products-input', 'value')]
)
def update_product_list(n_clicks, start_date, end_date, num_products):
    if n_clicks > 0:
        most_selled_products = MostSelledProductsForDate()
        return most_selled_products._update_product_list(start_date, end_date, num_products)
    else:
        return None
