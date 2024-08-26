# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 19:28:46 2024

@author: Fernando Xicot
"""
import turtle
import math
import time

# Configuración de la pantalla
screen = turtle.Screen() #Definimos el objeto pantalla para la ventana de turtle
screen.title("Reloj") #Nombramos la ventana 
screen.setup(width=600, height=600) #Definimos las dimensiones de la pantalla para que podamos dibujar en escalas cómodas

# Crear la tortuga para dibujar
clock_turtle = turtle.Turtle() #Definimos el puntero tortuga para regular la velocidad
clock_turtle.speed(0)  # Velocidad máxima para el dibujo, cero sería un paso inmediato
clock_turtle.hideturtle() #Ocultamos el puntero tortuga

# Crear una tortuga separada para las manecillas
hands_turtle = turtle.Turtle() # Se define otra tortuga para la manecilla
hands_turtle.speed(0) #velocidad
hands_turtle.hideturtle() # ocultamos la tortuga

# Dibujar el círculo del reloj
clock_turtle.penup() #Levantamos la pluma para crear un círculo con centro en el         
clock_turtle.goto(0, -250)  #Posicionamos la tortuga en la parte inferior del círculo
clock_turtle.pendown() #Volvemos a bajar la pluma para esribir
clock_turtle.circle(250) #hacemos un círculo con radio de 250 unidades

# Función para posicionar la tortuga y escribir un número
def draw_number(number, angle):
    radius = 200  # Definimos el lugar en donde estarán los números
    x = radius * math.cos(math.radians(angle)) # Definimos la coordenada en X para los números según el ángulo
    y = radius * math.sin(math.radians(angle)) # Definimos la coordenada en Y para los números según el ángulo 
    clock_turtle.penup() # Levantamos la pluma
    clock_turtle.goto(x, y - 20)  # Ajustamos las coordenadas para centrar el número
    clock_turtle.pendown() # Bajamos la pluma
    clock_turtle.write(str(number), align="center", font=("Times", 24, "normal")) #Usamos la función write para escribir el número 

# Dibujar los números del reloj
for hour in range(1, 13):
    angle = 90 - (hour * 30)  # Definimos el ángulo para cada número y ajustamos -90 grados para el marco de referencia
    draw_number(hour, angle) # Escribimos el número en el lugar correcto 

# Función para dibujar una manecilla del reloj
def draw_hand(length, angle, color):
    hands_turtle.penup() # Inicializamos la manecilla arriba
    hands_turtle.goto(0, 0) # Vamos a la posición 0,0
    hands_turtle.setheading(angle) #Le damos el ángulo hacia el cual se va a dirigir
    hands_turtle.pendown() #Bajamos la pluma para dibujar
    hands_turtle.color(color) #Definimos unn color para la manecilla
    hands_turtle.forward(length) # Hacemos avanzar la manecilla la distancia necesaria

# Función para dibujar la hora actual y que se esté refrescando constantemente
def draw_current_time():
    while True:
        # Limpiamos la tortuga de las manecillas antes de redibujar
        hands_turtle.clear()
        
        
        current_time = time.localtime() # Obtenemos la hora actual
        hours = current_time.tm_hour % 12 # Se usa el residuo para obtener el formato de doce horas
        minutes = current_time.tm_min # Se obtienen los minutos

        # Calcular los ángulos de las manecillas
        hour_angle = 90 - (hours * 30 + minutes * 0.5) # Se calcula el lugar exacto de la manecilla para las horas
        minute_angle = 90 - (minutes * 6) #Se calculal el lugar para la manecilla de los minutos 

        # Dibujar las manecillas
        draw_hand(150, hour_angle, "black")  # Manecilla de la hora
        draw_hand(200, minute_angle, "blue")  # Manecilla de los minutos
        
        # Calcular el tiempo restante hasta el próximo minuto
        current_seconds = current_time.tm_sec #Se calculan los segundos actuales
        wait_time = 60 - current_seconds # Se calculan los segundos restantes de el minuto actual
        
        
        time.sleep(wait_time) # Se espera el tiempo calculado para volver a iterar el while

# Iniciar el dibujo de la hora actual en un bucle
draw_current_time()

# Mantener la ventana abierta
turtle.done()