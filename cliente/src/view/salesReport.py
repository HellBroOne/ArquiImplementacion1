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

class SalesByDate:
    def __init__(self):
            pass

    def document(self):
        return dbc.Container(
            fluid=True,
            children=[
                html.Br(),
                self._header_title("Sales Report by Date Range"),
                html.Div(html.Hr()),
                self._date_picker(),
                html.Br(),
                html.Br(),
                html.Button("Consult", id="get-sale-button", n_clicks=0),
                html.Br(),
                self._show_sales_report(),
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

    def _show_sales_report(self):
        return html.Div(id='sales-date-list')

    def _update_salesdate_list(self, start_date, end_date):
        print("updating sales date...")
        sales_result = DashboardController.load_sales_report(start_date, end_date)

        if not sales_result:
            return html.Div("No products available.")

        sales_list = [
            dbc.Row(
                [
                    html.H5(f"- Product {eachSale['description']} was sold at the price ${eachSale['price']} {eachSale['quantity']} times, making a total of ${eachSale['total']} ", style={"font-weight": "bold"}),
                ]
            )
            for eachSale in sales_result
        ]
        return dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H3("Sales by Date Range", className="card-title"),
                        html.Br(),
                        html.Div(sales_list)
                    ]
                )
            ]
        )