##!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: dashboard.py
# Capitulo: Flujo de Datos
# Autor(es): Perla Velasco & Yonathan Mtz. & Jorge Solís
# Version: 1.0.0 Noviembre 2022
# Descripción:
#
#   Este archivo define los elementos visuales de la pantalla
#   del tablero
#
#-------------------------------------------------------------------------
from src.controller.dashboard_controller import DashboardController
import dash_bootstrap_components as dbc
import plotly.express as px
from dash import Dash, dcc, html, Input, Output, State
from datetime import datetime, date

class Dashboard:

    def __init__(self):
        pass

    def document(self):
        return dbc.Container(
            fluid = True,
            children = [
                self._navbar(),
                html.Br(),
                html.Div(html.Hr()),
                self._header_subtitle("Sales summary financial report"),
                html.Br(),
                self._highlights_cards(),
                html.Br(),
                self._header_subtitle2("Sales for date range", 'id-titulo2'),
                html.Div(html.Hr()),
                self._date_picker(),
                self.sales_for_date_range(),
                html.Br(),
                html.Div(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    self._bar_chart_providers_by_location(),
                                    width=12
                                ),
                            ]
                        )
                    ]
                ),
                html.Br(),
                html.Div(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    self._bar_chart_sales_per_location(),
                                    width=12
                                ),
                            ]
                        )
                    ]
                ),
                html.Br(),
                html.Div(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    self._bar_chart_orders_per_location(),
                                    width=12
                                ),
                            ]
                        )
                    ]
                ),
                html.Br(),
                html.Div(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    self._panel_best_sellers(),
                                    width=6
                                ),
                                dbc.Col(
                                    self._panel_worst_sales(),
                                    width=6
                                ),
                            ]
                        )
                    ]
                ),
                html.Br(),
                html.Div(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    self._panel_most_selled_products(),
                                    width=12
                                ),
                            ]
                        )
                    ]
                ),
                html.Br(),
            ]
        )

    def _navbar(self):
        return dbc.NavbarSimple(
            children=[
                dbc.NavItem(dbc.NavLink("Home", href="/")),
                dbc.NavItem(dbc.NavLink("Most Selled Products by Date", href="/most-selled-products")), #Reporte de productos más vendidos
                dbc.NavItem(dbc.NavLink("Sales Indicators by Date", href="/sales-indicators")), #reporte de indicadores de ventas
                dbc.NavItem(dbc.NavLink("Number of Selled Products by Date", href="/num-selled-products")), #reporte de cantidad de productos vendidos
            ],
            brand="Sales Report",
            brand_href="#",
            color="ligth",
            dark=False,
        )

    def _header_subtitle2(self, subtitle,id):
        return html.Div(
            [
                html.P(
                    subtitle,
                    className="lead",
                ),
            ],
            id=id,
        )

    def _date_picker(self):
        return dcc.DatePickerRange(
            id='date-picker',
            start_date=datetime(2024, 1, 1),
            end_date=datetime(2024, 10, 30),
            display_format='YYYY-MM-DD'
        )
    
    def sales_for_date_range(self):
        return html.Div(id='sales-list')

    def sales_by_date(self, fecha_inicio, fecha_fin):
        #orders = DashboardController.load_orders_date(fecha_inicio, fecha_fin)
        sales_by_date = DashboardController.load_sales_date(fecha_inicio, fecha_fin)

        if not sales_by_date:
            return html.Div("No orders available.")

        sales_list = [
            dbc.Row(
                [
                    html.H5(f"- {sales['sales']} [{sales['times']} time(s) sold]", style={"font-weight": "bold"}),
                ]
            )
            for sales in sales_by_date
        ]
    
    def _header_title(self, title):
        return dbc.Row(
            [
                dbc.Col(html.H2(title, className="display-4"))
            ]
        )

    def _header_subtitle(self, subtitle):
        return html.Div(
            [
                html.P(
                    subtitle,
                    className="lead",
                ),
            ],
            id="blurb",
        )

    def _card_value(self, label, value):
        return dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H2(value, className="card-title"),
                    ]
                ),
                dbc.CardFooter(label),
            ]
        )

    def _highlights_cards(self):
        products = DashboardController.load_products()
        orders = DashboardController.load_orders()
        providers = DashboardController.load_providers()
        locations = DashboardController.load_locations()
        sales = DashboardController.load_sales()
        return html.Div(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            self._card_value("Products", products["products"])
                        ),
                        dbc.Col(
                            self._card_value("Orders", orders["orders"])
                        ),
                        dbc.Col(
                            self._card_value("Providers", providers["providers"])
                        ),
                        dbc.Col(
                            self._card_value("Locations", locations["locations"])
                        ),
                        dbc.Col(
                            self._card_value("Sales", "$ {:,.2f}".format(float(sales['sales'])))
                        ),
                    ]
                ),
            ]
        )

    def _bar_chart_providers_by_location(self):
        data = DashboardController.load_providers_per_location()
        bar_char_fig = px.bar(data, x="location", y="providers")
        return dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H3("Providers per location", className="card-title"),
                        dcc.Graph(
                            id='providers-per-location',
                            figure=bar_char_fig
                        ),
                    ]
                ),
            ]
        )

    def _bar_chart_sales_per_location(self):
        data = DashboardController.load_sales_per_location()
        bar_char_fig = px.bar(data, x="location", y="sales")
        return dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H3("Sales per location", className="card-title"),
                        dcc.Graph(
                            id='sales-per-location',
                            figure=bar_char_fig
                        ),
                    ]
                ),
            ]
        )

    def _bar_chart_orders_per_location(self):
        data = DashboardController.load_orders_per_location()
        bar_char_fig = px.bar(data, x="location", y="orders")
        return dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H3("Orders per location", className="card-title"),
                        dcc.Graph(
                            id='orders-per-location',
                            figure=bar_char_fig
                        ),
                    ]
                ),
            ]
        )

    def _panel_best_sellers(self):
        best_sellers = DashboardController.load_best_sellers()
        return html.Div(
            [
                dbc.Card(
                    [
                        dbc.CardBody(
                            [
                                html.H3("Best sellers", className="card-title"),
                                html.Br(),
                                html.Div(
                                    [
                                        html.Div(
                                            [
                                                dbc.Row(
                                                    [
                                                        html.H5(f"- [{sale['invoice']}] $ {sale['total']:,.2f}", style={"font-weight":"bold"}),
                                                    ]
                                                ),
                                            ]
                                        )

                                        for sale in best_sellers
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        )

    def _panel_worst_sales(self):
        worst_sales = DashboardController.load_worst_sales()
        return html.Div(
            [
                dbc.Card(
                    [
                        dbc.CardBody(
                            [
                                html.H3("Worst sales", className="card-title"),
                                html.Br(),
                                html.Div(
                                    [
                                        html.Div(
                                            [
                                                dbc.Row(
                                                    [
                                                        html.H5(f"- [{sale['invoice']}] $ {sale['total']:,.2f}", style={"font-weight":"bold"}),
                                                    ]
                                                ),
                                            ]
                                        )

                                        for sale in worst_sales
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        )

    def _panel_most_selled_products(self):
        most_selled = DashboardController.load_most_selled_products()
        return html.Div(
            [
                dbc.Card(
                    [
                        dbc.CardBody(
                            [
                                html.H3("Most selled", className="card-title"),
                                html.Br(),
                                html.Div(
                                    [
                                        html.Div(
                                            [
                                                dbc.Row(
                                                    [
                                                        html.H5(f"- {product['product']} [{product['times']} time(s) sold]", style={"font-weight":"bold"}),
                                                    ]
                                                ),
                                            ]
                                        )

                                        for product in most_selled
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        )

