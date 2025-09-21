#Importar todos los elementos de la biblioteca gráfica 'turtle'
from turtle import *
from freegames import vector
import math

#Importar vectores para movimiento de la bibliotec 'freegames'
from freegames import vector

#Función para generar una línea desde el punto inicial hasta el final
def line(start, end):

    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

#Función para generar un cuadrado desde el punto inicial hasta el final
def square(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

#Función para generar un círculo usando los puntos de inicio y fin como radio
def circ(start, end):
    """Draw circle from start to end."""

    up()
    #calcula el radio como la distancia entre start y end
    radius = math.hypot(end.x - start.x, end.y - start.y)
    #ir al borde derecho del círculo
    goto(start.x + radius, start.y)
    down()
    begin_fill()
    turtle.circle(radius)
    #aquí sí recibe un número real 
    end_fill()

#Función para generar un rectángulo con las coordenadas x de inicio y fin como ancho y las coordenadas de y como alto
def rectangle(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range (2):
        forward(end.x - start.x)
        left(90)
        forward(end.y - start.y)
        left(90)

    end_fill()

#Función para generar un triángulo con la diferencia entre las coordenadas x de inicio y fin como el largo de cada lado
def triangle(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range (3):
        forward(end.x - start.x)
        left(120)

    end_fill



def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('purple'), 'P') #nuevo color agregado
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()

