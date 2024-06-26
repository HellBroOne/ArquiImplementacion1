##!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: queries.py
# Capitulo: Flujo de Datos
# Autor(es): Perla Velasco & Yonathan Mtz. & Jorge Solís
# Version: 1.0.0 Noviembre 2022
# Descripción:
#
#   Este archivo define las consultas que permiten obtener información
#   y realizar el llenado de datos del tablero
#
#-------------------------------------------------------------------------

from datetime import datetime


class Queries:

    @staticmethod
    def get_productos_porFecha1y2(start_period, end_period):
        return """
                {
                    var(func: has(invoice)) @filter(between(date, "%s", "%s")) {
                        t as quantity
                    }
                    response() {
                        count: sum(val(t))
                    }
                }
            """ % (start_period, end_period)

    @staticmethod
    def get_total_products():
        return """
            {
                response(func: has(description)) {
                    count(uid)
                }
            }
        """

    @staticmethod
    def get_total_providers():
        return """
            {
                response(func: has(pid)) {
                    count(uid)
                }
            }
        """

    @staticmethod
    def get_total_locations():
        return """
            {
                response(func: has(name)) {
                    count(uid)
                }
            }
        """

    @staticmethod
    def get_total_orders():
        return """
            {
                response(func: has(invoice)) {
                    count(uid)
                }
            }
        """

    @staticmethod
    def get_total_sales():
        return """
            {
                var(func: has(invoice)) {
                    t as total
                }

                response() {
                    total: sum(val(t))
                }
            }
        """

    @staticmethod
    def get_providers_per_location():
        return """
            {
                response(func: has(name)) {
                    name
                    providers: ~belongs {
                        count(uid)
                    }
                }
            }
        """

    @staticmethod
    def get_sales_per_location():
        return """
            {
                response(func: has(name)){
                    name
                    providers: ~belongs {
                        sold: ~sold {
                            price
                            quantity: count(bought)
                        }
                    }
                }
            }
        """

    @staticmethod
    def get_orders_per_location():
        return """
            {
                response(func: has(name)){
                    name
                    providers: ~belongs {
                        sold: count(~sold)
                    }
                }
            }
        """

    @staticmethod
    def get_best_sellers():
        return """
            {
                var(func: has(description)) {
                    c as count(bought) 
                }
                    
                response(func: has(description), orderdesc: val(c)){
                    description
                    times: val(c)
                    price
                }
            }
        """

    @staticmethod
    def get_worst_sales():
        return """
            {
                var(func: has(description)) {
                    c as count(bought) 
                }
                    
                response(func: has(description), orderasc: val(c)){
                    description
                    times: val(c)
                    price
                }
            }
        """

    @staticmethod
    def get_most_selled_products():
        return """
            {
                var(func: has(description)) {
                    c as count(bought) 
                }

                response(func: has(description), orderdesc: val(c)){
                    description
                    times: val(c)
                }
            }
        """

    #Querry para obtener los productos y la cantidad de ellos más vendidos en un rango de fechas.
    def get_most_selled_products_for_date(start_date, end_date):
        query = '''
            {
                var(func: has(invoice)) @filter(ge(date, "%s") AND le(date, "%s")) {
                    product as ~bought
                }

                var(func: uid(product)) {
                    purchasedProduct as uid
                }

                var(func: has(description)) {
                    c as count(bought)
                }

                topProduct(func: uid(purchasedProduct), orderdesc: val(c)) @cascade {
                    description
                    times: val(c)
                }
            }
            ''' % (start_date, end_date)
        return query


    #query que filtra los datos de las ventas para que se muestren solamente
    #los que estan entre dos fechas o periodos especificados 
    #@staticmethod
    #def get_sales_by_date(fecha_inicio, fecha_fin):
        #return """
            #{
                #var(func: has(date)) @filter(ge(date, "{fecha_inicio}") AND le(date, "{fecha_fin}")) {
                   # t as total
               # }
             #   response() {
                  #  total: sum(val(t))
               # }
         #   }
      #  """
    #query que filtra los datos de las ventas para que se muestren solamente
    #los que estan entre dos fechas o periodos especificados 
    @staticmethod
    def get_total_orders_date(fecha_inicio, fecha_fin):
        return """
            {
                response(func: has(invoice)) @filter(between(date, "{fecha_inicio}", "{fecha_fin}")) {
                    count(uid)
                }
            }
        """
    
    #query que permite obtener las ventas por region
    #filtrandolas por fecha 
    @staticmethod
    def get_sales_indicators(start_date,end_date):
        query = '''
        {
            response(func: has(name)) {
            name
            providers: ~belongs {
                sold: ~sold {
                    price
                    quantity: count(bought)
                }
            }
        }
        }
        '''
        return query
    

    #obtiene las ventas por fecha
    def get_sales_by_date(start_date, end_date):
        query = '''
            {
                var(func: has(invoice)) @filter(ge(date, "%s") AND le(date, "%s")) {
                    product as ~bought
                }

                var(func: uid(product)) {
                    purchasedProduct as uid
                }

                product(func: uid(purchasedProduct)){
					description
                    price
                    quantity: count(bought)
                }
            }
            ''' % (start_date, end_date)
        return query
    
    #2024-01-30
    #2024-10-30











