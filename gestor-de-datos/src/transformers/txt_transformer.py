##!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: txt_transformer.py
# Autor(es): Andres Contreras, Gerardo Rivas, Omar Alejandro de la Cruz y Fernando Manuel
# Version: 1.0.0 Abril del 2024
# Descripción:
#
#   Este archivo define un procesador de datos que se encarga de transformar
#   y formatear el contenido de un archivo TXT, que estaran divididos los campos por comas.
#-------------------------------------------------------------------------
from src.extractors.txt_extractor import TXTExtractor
from os.path import join
import luigi, os, json

class TXTTransformer(luigi.Task):

    def requires(self):
        return TXTExtractor()

    def run(self):
        result = []
        for file in self.input():
            with file.open() as txt_file:
                next(txt_file)  # Saltar los encabezados
                for line in txt_file:
                    purchases = line.strip().split(';')
                    for purchase in purchases:
                        fields = purchase.split(',')
                        if len(fields) < 8:
                            continue
                        invoice_num = fields[0]
                        inventory_code = fields[1]
                        description = fields[2]
                        amount = int(fields[3])
                        invoice_date = fields[4]
                        unit_price = float(fields[5])
                        customer_id = fields[6]
                        country = fields[7]

                        result.append(
                            {
                                "description": description,
                                "quantity": amount,
                                "price": unit_price,
                                "total": amount * unit_price,
                                "invoice": invoice_num,
                                "date": invoice_date,
                                "provider": customer_id,
                                "country": country
                            }
                        )

        with self.output().open('w') as out:
            out.write(json.dumps(result, indent=4))

    def output(self):
        project_dir = os.path.dirname(os.path.abspath("loader.py"))
        result_dir = os.path.join(project_dir, "result")
        return luigi.LocalTarget(os.path.join(result_dir, "txt.json"))