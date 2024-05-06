##!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: salesIndicatorsReport.py
# Capitulo: Flujo de Datos
# Autor(es): Gerardo Rivas Delgado
# Version: 1.0.0 Abril 2024
# Descripción:
#
#   Este archivo mostrara a los indicadores de ventas 
#   de todas las sucursales mostrando las ventas por periodo.
#-------------------------------------------------------------------------

import dash_bootstrap_components as dbc
import plotly.express as px
from dash import dcc, html, Input, Output, State
import dash
from datetime import datetime
from src.controller.dashboard_controller import DashboardController

app = dash.Dash(
    external_stylesheets=[dbc.themes.LUX],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ],
    suppress_callback_exceptions=True
)

class SalesIndicators():
    def __init__(self):
            pass

    def document(self):
        return dbc.Container(
            fluid=True,
            children=[
                html.Br(),
                self._header_title("Sales Indicators Report"),
                html.Div(html.Hr()),
                 html.H5("Please select a period of time:"),
                html.Br(),
                self._date_picker(),
                html.Br(),
                html.Button("Search", id="search-button", n_clicks=0),
                html.Br(),
                self._sales_indicator_list(),
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
    
    
    def _sales_indicator_list(self):
        print("sales list created!\n")
        return html.Div(id='sales-list')

    def _update_sales_list(self, start_date, end_date):
        print("updating...\n")
        indicators = DashboardController.load_sales_indicators(start_date, end_date)

        if not indicators:
            print("not found..\n")
            return html.Div("No sales were found.")

        sales_list = [
            dbc.Row(
                [
                    html.H5(f"- Located on {sale['location']} [Having ${sale['orders']} on sales]", style={"font-weight": "bold"}),
                ]
            )
            for sale in indicators
        ]
        print("rendered!\n")

        return dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H3("Sales Indicators For Date Range", className="card-title"),
                        html.Br(),
                        html.Div(sales_list)
                    ]
                )
            ]
        )
    
    