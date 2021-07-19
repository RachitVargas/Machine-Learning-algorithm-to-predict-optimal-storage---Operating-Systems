#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 10:44:47 2021

@author: antony.vargasulead.ac.cr
"""
from interfaz import Interfaz
from memoria import Memoria
from Regresion_Lineal import Regresion_lineal

def main():
    
    opcion = 0
    interfaz = Interfaz
    memoria = Memoria
    historial_dias = []
    historial_memoria = []
    
    
  
    while opcion != 5:
        #try:
            opcion = interfaz.menu()   
        
            if opcion == 1:
                historial_dias, historial_memoria = memoria.consumo_memoria()
        
            elif opcion == 2:
                memoria.graficar(historial_dias, historial_memoria, annot=False)
        
            elif opcion == 3:
                valor_minimo_memoria = memoria.modelo()
                print("La cantidad minima de memoria necesaria para que siempre siga creciendo es: " +\
                      str(valor_minimo_memoria))

            elif opcion == 4:
                x, y = memoria.X_y(50)
                x_test, y_test = memoria.X_y(10)
                regresion_lineal = Regresion_lineal(x, y)
                regresion_lineal.plot_line()
                regresion_lineal.plot_test(x_test, y_test)
                print("Ecuacion lineal: " + regresion_lineal.ecuacion)
                print("Coeficiente de correlacion: " + str(regresion_lineal.r))
                
            elif opcion == 5:
                print("Muchas gracias por usar el simulador.")
            
            
            else: 
                print("Opcion invalida. Por favor vuelva a intarlo")
                
       # except:
           # print("Asegurese de haber digitado una opcion correcto")
            
if __name__ == '__main__':
    main()
    