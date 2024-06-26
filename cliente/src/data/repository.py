##!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: repository.py
# Capitulo: Flujo de Datos
# Autor(es): Perla Velasco & Yonathan Mtz. & Jorge Solís
# Version: 1.0.0 Noviembre 2022
# Descripción:
#
#   Este archivo define el acceso e interacción entre el componente
#   y el API
#
#-------------------------------------------------------------------------
from src.data.provider import Provider
from src.data.queries import Queries

class Repository:

    # obtener la respuesta de la consulta de cantidad de productos vendidos
    @staticmethod
    def get_productos_porFecha1y2(start_period, end_period):
        response = Provider.execute(Queries.get_productos_porFecha1y2(start_period, end_period))
        return response

    @staticmethod
    def get_products():
        response = Provider.execute(Queries.get_total_products())
        return response

    @staticmethod
    def get_providers():
        response = Provider.execute(Queries.get_total_providers())
        return response

    @staticmethod
    def get_locations():
        response = Provider.execute(Queries.get_total_locations())
        return response

    @staticmethod
    def get_orders():
        response = Provider.execute(Queries.get_total_orders())
        return response

    @staticmethod
    def get_sales():
        response = Provider.execute(Queries.get_total_sales())
        return response

    @staticmethod
    def get_providers_by_location():
        response = Provider.execute(Queries.get_providers_per_location())
        return response

    @staticmethod
    def get_sales_by_location():
        response = Provider.execute(Queries.get_sales_per_location())
        return response

    @staticmethod
    def get_orders_by_location():
        response = Provider.execute(Queries.get_orders_per_location())
        return response

    @staticmethod
    def get_best_sellers():
        response = Provider.execute(Queries.get_best_sellers())
        return response

    @staticmethod
    def get_worst_sales():
        response = Provider.execute(Queries.get_worst_sales())
        return response
    
    @staticmethod
    def get_most_selled_products():
        response = Provider.execute(Queries.get_most_selled_products())
        return response

    # obtener el resultado de la consulta para los productos vendidos en un rango de fechas
    @staticmethod
    def get_most_selled_products_for_date(fecha_inicio, fecha_fin):
        response = Provider.execute(Queries.get_most_selled_products_for_date(fecha_inicio, fecha_fin))
        print(response)
        return response
    
    #manda a llamar a la consulta de los indicadores de ventas desde el Provider.
    #haciendola mediante la consulta dada.
    @staticmethod
    def get_sales_indicators(fecha_inicio, fecha_fin):
        print("Trying to execute the query")
        response = Provider.execute(Queries.get_sales_indicators(fecha_inicio, fecha_fin))
        print(response)
        return response
    
    #Sales en un periodo específico 
    @staticmethod
    def get_sales_date(fecha_inicio, fecha_fin):
        print("made: ")
        response = Provider.execute(Queries.get_sales_by_date(fecha_inicio, fecha_fin))
        print(response)
        return response

    #Orders en un periodo específico 
    @staticmethod
    def get_orders_by_date(fecha_inicio, fecha_fin):
        response = Provider.execute(Queries.get_total_orders_date(fecha_inicio, fecha_fin))
        print(response)
        return response
