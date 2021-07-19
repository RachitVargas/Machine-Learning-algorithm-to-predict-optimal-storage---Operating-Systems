#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 10:55:06 2021

@author: antony.vargasulead.ac.cr
"""

import matplotlib.pyplot as plt
import numpy as np

class Memoria():
    
    def consumo_memoria():
        megas_inicial = int(input("Ingrese la cantidad de megas inicial: "))
        n_dias = int(input("Ingrese la cantidad de dias: "))
        promedio_megas = int(input("Ingrese la cantidad de megas de consumo de usuario: "))
        dias = []
        memoria = []
        for i in range(n_dias):
            print("dia " + str(i+1) + ", cantidad de almacenamiento disponible: " +\
                         str(megas_inicial) + " megas")
    
            if megas_inicial < 28000:
                megas_agregado = megas_inicial*0.4
                megas_inicial = megas_inicial + (megas_agregado) - promedio_megas
                print("Se agrego " + str(megas_agregado) + " mas a la memoria y se resto " + str(promedio_megas) +\
                      " entonces ahora tenemos " + str(megas_inicial) + " memoria en el dia " + str(i+1))
                dias.append(i+1)
                memoria.append(megas_inicial)
            else:
                megas_agregado = megas_inicial*0.31
                megas_inicial = megas_inicial + (megas_agregado) - promedio_megas
                print("Se agrego " + str(megas_agregado) + " mas a la memoria y se resto " + str(promedio_megas) +\
                      " entonces ahora tenemos " + str(megas_inicial) + " memoria en el dia " + str(i+1))
                dias.append(i+1)
                memoria.append(megas_inicial)
        
        return dias, memoria
    
    def graficar(historial_dias, historial_memoria, annot=False):
        fig, ax = plt.subplots(figsize=(10,5), dpi=100)
        ax.set_title('Historia de dias vs memoria disponible')
        ax.set_xlabel('Cantidad de dias')
        ax.set_ylabel('Memoria disponible')
        ax = plt.scatter(historial_dias, historial_memoria, s=100)
        if annot:
            for i, txt in enumerate(historial_memoria):
                plt.annotate(txt, (historial_dias[i], historial_memoria[i]))
        plt.show()
    
    def modelo():
        megas = int(input("Ingrese la cantidad de megas de consumo: "))
        memoria = 1
        valor_porcentaje = 1
        
        while valor_porcentaje < megas:
            if memoria < 28000:
                valor_porcentaje = memoria*0.4
                memoria += 1

            else:
                valor_porcentaje = memoria*0.31
                memoria += 1        
        return memoria
    
    def X_y(n):
        megas = np.random.randint(3000, 10000, n)
        y = []
        
        for i in range(len(megas)):
            memoria = 1
            valor_porcentaje = 1
        
            while valor_porcentaje < megas[i]:
                if memoria < 28000:
                    valor_porcentaje = memoria*0.4
                    memoria += 1

                else:
                    valor_porcentaje = memoria*0.31
                    memoria += 1
            
            y.append(memoria)
            
        
        return megas, y
    
            