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

from os.path import join
import luigi
import os
import json

class TXTTransformer(luigi.Task):

    def requires(self):
        return TXTExtractor()

    def run(self):
        result = []
        for file in self.input():
            with file.open() as txt_file:
                lines = txt_file.readlines()
                for line in lines:

                    fields = line.strip().split(',')
                    description = fields[0]
                    quantity = fields[1]
                    price = fields[2]
                    total = float(quantity) * float(price)
                    invoice = fields[3]
                    provider = fields[4]
                    country = fields[5]

                    result.append(
                        {
                            "description": description,
                            "quantity": quantity,
                            "price": price,
                            "total": total,
                            "invoice": invoice,
                            "provider": provider,
                            "country": country
                        }
                    )

        with self.output().open('w') as out:
            out.write(json.dumps(result, indent=4))

    def output(self):
        project_dir = os.path.dirname(os.path.abspath("loader.py"))
        result_dir = join(project_dir, "result")
        return luigi.LocalTarget(join(result_dir, "txt.json"))
