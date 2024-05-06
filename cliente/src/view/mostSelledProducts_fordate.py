##!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: mostSelledProducts_fordate.py
# Capitulo: Flujo de Datos
# Autor(es): Andres Contreras Sanchez
# Version: 1.0.0 Abril 2024
# Descripción:
#
#   Este archivo mostrara una lista de los productos mas
#   vendidos en un rango de fechas
#
#-------------------------------------------------------------------------

import dash_bootstrap_components as dbc
import plotly.express as px
from dash import dcc, html, Input, Output, State
from datetime import datetime
from src.controller.dashboard_controller import DashboardController

class MostSelledProductsForDate:
    def __init__(self):
            pass

    def document(self):
        return dbc.Container(
            fluid=True,
            children=[
                html.Br(),
                self._header_title("Top Selling Products For Date Range"),
                html.Div(html.Hr()),
                self._date_picker(),
                html.Br(),
                html.Br(),
                html.Label("Number of products: "),
                dcc.Input(
                    id='num-products-input',
                    type='number',
                    value=10
                ),
                html.Button("Consult", id="consult-button", n_clicks=0),
                html.Br(),
                self._top_selling_products(),
            ]
        )

    def _header_title(self, title):
        return dbc.Row(
            [
                dbc.Col(html.H2(title, className="display-4"))
            ]
        )

    def _date_picker(self):
        return dcc.DatePickerRange(
            id='date-picker',
            start_date=datetime(2024, 1, 1),
            end_date=datetime(2024, 10, 30),
            display_format='YYYY-MM-DD'
        )

    def _top_selling_products(self):
        print("si")
        return html.Div(id='product-list')

    def _update_product_list(self, start_date, end_date, num_products):
        most_selled = DashboardController.load_most_selled_products_for_date(start_date, end_date, num_products)

        if not most_selled:
            return html.Div("No products available.")

        product_list = [
            dbc.Row(
                [
                    html.H5(f"- {product['product']} [{product['times']} time(s) sold]", style={"font-weight": "bold"}),
                ]
            )
            for product in most_selled
        ]
        return dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H3("Most sold products For Date Range", className="card-title"),
                        html.Br(),
                        html.Div(product_list)
                    ]
                )
            ]
        )