# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 23:37:41 2024

@author: Fernando Xicot
"""

x1=1 #"Punto inicial"
x2=4 #"Punto final"
x=x1  #"Punto a evaluar para encontrar la altura "
dx= (x2-x1)/100 #"El paso, para tener 100 rectángulos"
area=0 #"Variable para ir guardando el área acumulada"
base=dx  
    
for i in range (100):
    
    altura=(x**2) #"Calculamos la altura"
    area= area + (base*altura) #"Calculamos el área"
    x=x+dx #"Cambiamos la x para el siguiente rectángulo"
        
print('El área aproximada es:', area)    