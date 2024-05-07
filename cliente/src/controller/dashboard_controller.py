##!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: dashboard_controller.py
# Capitulo: Flujo de Datos
# Autor(es): Perla Velasco & Yonathan Mtz. & Jorge Solís
# Version: 1.0.0 Noviembre 2022
# Descripción:
#
#   Este archivo define la funcionalidad del componente
#
#-------------------------------------------------------------------------
from src.data.repository import Repository
import json

class DashboardController:
    @staticmethod
    def get_productos_porFecha1y2(start_period, end_period):
        response = Repository.get_productos_porFecha1y2(start_period, end_period)
        if response.status_code != 200:
            return {"cantidad_productos_vendidos": 0}

        json_response = json.loads(response.text)

        assert ('data' in json_response.keys())
        assert ('response' in json_response['data'].keys())
        if json_response["data"]["response"][0]["count"] is None:
            return {"cantidad_productos_vendidos": "0"}

        return {
            "cantidad_productos_vendidos": json_response["data"]["response"][0]["count"]
        }

    @staticmethod
    def load_products():
        response = Repository.get_products()
        if response.status_code != 200:
            return {"products": 0} 
        
        json_response = json.loads(response.text)

        assert('data' in json_response.keys())
        assert('response' in json_response['data'].keys())

        return {
            "products": json_response["data"]["response"][0]["count"]
        }

    @staticmethod
    def load_providers():
        response = Repository.get_providers()
        if response.status_code != 200:
            return {"providers": 0}
        
        json_response = json.loads(response.text)

        assert('data' in json_response.keys())
        assert('response' in json_response['data'].keys())

        return {
            "providers": json_response["data"]["response"][0]["count"]
        }

    @staticmethod
    def load_locations():
        response = Repository.get_locations()
        if response.status_code != 200:
            return {"locations": 0}
        
        json_response = json.loads(response.text)

        assert('data' in json_response.keys())
        assert('response' in json_response['data'].keys())

        return {
            "locations": json_response["data"]["response"][0]["count"]
        }

    @staticmethod
    def load_orders():
        response = Repository.get_orders()
        if response.status_code != 200:
            return {"orders": 0}
        
        json_response = json.loads(response.text)

        assert('data' in json_response.keys())
        assert('response' in json_response['data'].keys())

        return {
            "orders": json_response["data"]["response"][0]["count"]
        }

    @staticmethod
    def load_sales():
        response = Repository.get_sales()
        if response.status_code != 200:
            return {"sales": 0}
        
        json_response = json.loads(response.text)
        
        assert('data' in json_response.keys())
        assert('response' in json_response['data'].keys())

        return {
            "sales": json_response["data"]["response"][0]["total"]
        }

    @staticmethod
    def load_providers_per_location():
        response = Repository.get_providers_by_location()
        if response.status_code != 200:
            return {
                "providers": [],
                "location": []
            }
        result = {
            "providers": [],
            "location": []
        }

        json_response = json.loads(response.text)

        assert('data' in json_response.keys())
        assert('response' in json_response['data'].keys())

        for entry in json_response["data"]["response"]:
            result["providers"].append(entry["providers"][0]["count"])
            result["location"].append(entry["name"])
        return result

    @staticmethod
    def load_sales_per_location():
        response = Repository.get_sales_by_location()
        if response.status_code != 200:
            return {
                "sales": [],
                "location": []
            }
        result = {
            "sales": [],
            "location": []
        }
        json_response = json.loads(response.text)

        assert('data' in json_response.keys())
        assert('response' in json_response['data'].keys())

        for entry in json_response["data"]["response"]:
            result["location"].append(entry["name"])
            total = 0
            for sold in entry["providers"]:
                for order in sold["sold"]:
                    total += (int(order["quantity"]) * float(order["quantity"]))
            result["sales"].append(total)
            
        return result

    @staticmethod
    def load_orders_per_location():
        response = Repository.get_orders_by_location()
        if response.status_code != 200:
            return {
                "orders": [],
                "location": []
            }
        result = {
            "orders": [],
            "location": []
        }
        json_response = json.loads(response.text)

        assert('data' in json_response.keys())
        assert('response' in json_response['data'].keys())

        for entry in json_response["data"]["response"]:
            result["location"].append(entry["name"])
            total = 0
            for sold in entry["providers"]:
                total += int(sold["sold"])
            result["orders"].append(total)
        return result

    @staticmethod
    def load_best_sellers():
        response = Repository.get_best_sellers()
        if response.status_code != 200:
            return []
        result = []
        json_response = json.loads(response.text)

        assert('data' in json_response.keys())
        assert('response' in json_response['data'].keys())

        for product in json_response["data"]["response"][0:5]:
            result.append({
                "invoice": product["times"],
                "total": int(product["times"]) * float(product["price"])
            })
        return result

    @staticmethod
    def load_worst_sales():
        response = Repository.get_worst_sales()
        if response.status_code != 200:
            return []
        result = []
        json_response = json.loads(response.text)

        assert('data' in json_response.keys())
        assert('response' in json_response['data'].keys())

        for product in json_response["data"]["response"][0:5]:
            result.append({
                "invoice": product["times"],
                "total": int(product["times"]) * float(product["price"])
            })
        return result

    @staticmethod
    def load_most_selled_products():
        response = Repository.get_most_selled_products()
        if response.status_code != 200:
            return []
        result = []
        json_response = json.loads(response.text)

        assert('data' in json_response.keys())
        assert('response' in json_response['data'].keys())

        for product in json_response["data"]["response"][0:5]:
            result.append({
                "product": product["description"],
                "times": product["times"]
            })
        return result

    # Se agrega para obtener los productos más vendidos en un rango de fechas y la cantidad de veces que se vendieron, num_productos es el número de productos que se desea mostrar en la lista.
    @staticmethod
    def load_most_selled_products_for_date(fecha_inicio, fecha_fin, num_products):
        response = Repository.get_most_selled_products_for_date(fecha_inicio, fecha_fin)
        if response.status_code != 200:
            return [], 0

        result = []

        json_response = json.loads(response.text)
        print("response: " + str(json_response))

        total_products = 0

        if 'data' in json_response and 'topProduct' in json_response['data']:
            top_products = json_response['data']['topProduct']
            for product in top_products[0:num_products]:
                result.append({
                    "product": product["description"],
                    "times": product["times"]
                })
            total_products = len(top_products)

        return result, total_products



    #obtiene las ventas de las sucursales
    @staticmethod
    def load_sales_indicators(fecha_inicio, fecha_fin):
        response = Repository.get_sales_indicators(fecha_inicio, fecha_fin)
        if response.status_code != 200:
            return []
        result = []
        json_response = json.loads(response.text)
        #print("loaded!\n")
        #print("response: " + str(json_response))
        assert('data' in json_response.keys())
        assert('response' in json_response['data'].keys())
        xd1 = fecha_inicio[0:4]
        xd2 = fecha_fin[0:4]
        if (xd1 == "2024") and (xd2 == "2024"):
            for entry in json_response["data"]["response"]:
                total = 0
                for sold in entry["providers"]:
                    price = float(sold["sold"][0]["price"])
                    quantity = float(sold["sold"][0]["quantity"])
                    totalprice = price * quantity
                    total += totalprice
                result.append({
                        "location": entry["name"],
                        "orders": total
                    })
        return result
    
    #obtiene las ventas para generar el reporte
    @staticmethod
    def load_sales_report(fecha_inicio, fecha_fin):
        print("Query made...")
        response = Repository.get_sales_date(fecha_inicio, fecha_fin)
        if response.status_code != 200:
            return []

        result = []
        json_response = json.loads(response.text)
        print("response: " + str(json_response))

        if 'data' in json_response and 'product' in json_response['data']:
            all_prods = json_response['data']['product']
            for product in all_prods:
                price = float(product["price"])
                quantity = float(product["quantity"])
                total = price*quantity
                result.append({
                    "description": product["description"],
                    "price": product["price"],
                    "quantity": product["quantity"],
                    "total": total
                })
                total = 0
        return result

    #Sales en un periodo específico.
    @staticmethod
    def load_sales_by_date(fecha_inicio, fecha_fin):
        response = Repository.get_sales_date(fecha_inicio, fecha_fin)
        if response.status_code != 200:
            return {"sales": 0}
        
        json_response = json.loads(response.text)
        print("response sales date: " + str(json_response))
        
        assert('data' in json_response.keys())
        assert('response' in json_response['data'].keys())
        if json_response["data"]["response"][0]["total"] is None:
            return {"sales":"0"}

        return {
            "sales": json_response["data"]["response"][0]["total"]
        }
    
    #Orders en un periodo específico.
    @staticmethod
    def load_orders_date(fecha_inicio, fecha_fin):
        response = Repository.get_orders_by_date(fecha_inicio, fecha_fin)
        if response.status_code != 200:
            return {"orders": 0}
        
        json_response = json.loads(response.text)

        assert('data' in json_response.keys())
        assert('response' in json_response['data'].keys())

        return {
            "orders": json_response["data"]["response"][0]["count"]
        }
