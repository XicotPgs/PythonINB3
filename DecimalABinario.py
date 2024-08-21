# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 23:35:52 2024

@author: Fernando Xicot
"""

import math 
nd=87 #Número decimal a convertir 
nb='' #Número binario en tipo char
cab=nd #Variable int para la división 

while cab >= 2: 
    
    nb=str(cab%2)+nb #Tomamos el residuo de la divición del nd/2
    #lo convertimos en str, y lo añadimos al inicio de la cadena final
    cab= math.floor(cab/2) #Dividimos el numero decimal entre dos 
    #y aplicamos función floor para continuar con ese nuevo número en la 
    #secuencia

nb=str(cab%2)+nb   #sumamos el último número que ya no entró en el while
print('El número',nd,'a binario, es:',nb) # imprimimos