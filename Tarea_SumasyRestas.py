# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 15:58:12 2024

@author: Fernando Xicot
"""

n=0 #Inicializamos la variable de la suma algebráica

for i in range(1,100): #Hacemos que el contador vaya de 1-100
    
    if i%2 == 0: #Si el residuo de dividir el número es 0
        n=n-i**(-1) #Restarle el inverso al número acumulado 
    else: #Si no es cero
        n=n+i**(-1) #Sumarle el inverso al número acumulado

print('El resultado de la suma es: ',n) #Imprimimos resultado 