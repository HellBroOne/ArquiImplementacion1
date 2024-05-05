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

    """@staticmethod
    def load_most_selled_products_for_date(date_from, date_to):
        response = Repository.get_most_selled_products_for_date(date_from, date_to)
        if response is None or response.status_code != 200:
            return []

        json_response = json.loads(response.text)
        if not isinstance(json_response, dict) or 'data' not in json_response or not isinstance(json_response['data'], dict) or 'response' not in json_response['data'] or json_response['data']['response'] is None:
            return []

        result = []

        assert('data' in json_response.keys())
        assert('response' in json_response['data'].keys())

        for product in json_response["data"]["response"][0:5]:
            result.append({
                "product": product["description"],
                "times": product["times"]
            })
        return result"""

    @staticmethod
    def load_most_selled_products_for_date(fecha_inicio, fecha_fin, num_products):
        response = Repository.get_most_selled_products_for_date(fecha_inicio, fecha_fin)
        if response.status_code != 200:
            return []

        result = []

        json_response = json.loads(response.text)
        print("response: " + str(json_response))

        if 'data' in json_response and 'topProduct' in json_response['data']:
            top_products = json_response['data']['topProduct']
            for product in top_products[0:num_products]:
                result.append({
                    "product": product["description"],
                    "times": product["times"]
                })

        return result


    """@staticmethod
    def load_most_selled_products(fecha_inicio, fecha_fin):
        all_products = Repository.get_all_products()
        if all_products.status_code != 200:
            return []

        result = []
        json_response = json.loads(all_products.text)
        print("response: " + str(json_response))
        
        assert 'data' in json_response.keys()
        assert 'response' in json_response['data'].keys()

        for product in json_response["data"]["response"]:
            if fecha_inicio <= product["date"] <= fecha_fin:
                result.append({
                    "product": product["description"],
                    "times": product["times"]
                })

        return result"""
