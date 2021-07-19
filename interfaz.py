#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 10:47:19 2021

@author: antony.vargasulead.ac.cr
"""

class Interfaz():
    
    def menu():
        print("Bienvenido a la simulacion")
        print("seleccione:")
        print("1. Correr la simulacion")
        print("2. Graficar los resultados")
        print("3. Obtener resultados del modelo")
        print("4. Generar modelo de Regresion Lineal")
        print("5. Salir de la simulacion")
        return int(input())