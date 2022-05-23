'''
24. Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
necesarias para resolver las siguientes actividades:
a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición
uno la cima de la pila;
b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar
la cantidad de películas en la que aparece;
c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.
'''
#from random import randint
from pila import Pila
class Personaje():
    nombre, cantidad_de_participaciones_en_peliculas_de_la_saga = None, None

def cargar_personaje(personaje):
    personaje.nombre = input("Cúal es el nombre del personaje? ")
    personaje.cantidad_de_participaciones_en_peliculas_de_la_saga = input("En cuantas peliculas participó? ")

def return_posicion_de_un_personaje(pila, nombre):
    pila_aux= Pila()
    posicion_actual = 0
    posicion_personaje = 0
    while(not pila.pila_vacia()):
        personanje = pila.desapilar()
        posicion_actual += 1
        if(personanje.nombre == nombre):
            posicion_personaje = posicion_actual
        pila_aux.apilar(personanje)
    while(not pila_aux.pila_vacia()):
        pila.apilar(pila_aux.desapilar())
    return(posicion_personaje)

def personajes_con_participacion_en_mas_de_x_peliculas(pila, x):
    pila_aux= Pila()
    while(not pila.pila_vacia()):
        personanje = pila.desapilar()
        if(personanje.cantidad_de_participaciones_en_peliculas_de_la_saga > x):
            print('El personaje', personanje.nombre,'participo en mas de',x,'peliculas (participo en',personanje.cantidad_de_participaciones_en_peliculas_de_la_saga,'peliculas)')
        pila_aux.apilar(personanje)
    while(not pila_aux.pila_vacia()):
        pila.apilar(pila_aux.desapilar())

def return_cuantas_peliculas_participo_x_personaje(pila, x):
    pila_aux= Pila()
    cantidad_de_participaciones = -1
    while(not pila.pila_vacia()):
        personanje = pila.desapilar()
        if(personanje.nombre == x):
            cantidad_de_participaciones = personanje.cantidad_de_participaciones_en_peliculas_de_la_saga
        pila_aux.apilar(personanje)
    while(not pila_aux.pila_vacia()):
        pila.apilar(pila_aux.desapilar())
    return cantidad_de_participaciones

def mostrar_todos_los_personajes_cuyos_nombre_empiezan_con_x_letras(pila, x):
    pila_aux= Pila()
    while(not pila.pila_vacia()):
        personanje = pila.desapilar()
        if (personanje.nombre[0] in x):
            print(personanje.nombre)
        pila_aux.apilar(personanje)
    while(not pila_aux.pila_vacia()):
        pila.apilar(pila_aux.desapilar())


pila_personajes = Pila()
'''
for i in range(3): #Se carga la pila con 3 pesonajes
    personaje_aux = Personaje()
    cargar_personaje(personaje_aux)
    pila_personajes.apilar(personaje_aux)
personaje_aux = Personaje()
'''

personaje_aux = Personaje()
personaje_aux.nombre = 'Black Widow'
personaje_aux.cantidad_de_participaciones_en_peliculas_de_la_saga = 2
pila_personajes.apilar(personaje_aux)

personaje_aux = Personaje()
personaje_aux.nombre = 'Rocket Raccoon'
personaje_aux.cantidad_de_participaciones_en_peliculas_de_la_saga = 2
pila_personajes.apilar(personaje_aux)

personaje_aux = Personaje()
personaje_aux.nombre = 'Capitan America'
personaje_aux.cantidad_de_participaciones_en_peliculas_de_la_saga = 5
pila_personajes.apilar(personaje_aux)

personaje_aux = Personaje()
personaje_aux.nombre = 'Groot'
personaje_aux.cantidad_de_participaciones_en_peliculas_de_la_saga = 7
pila_personajes.apilar(personaje_aux)

#a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición
#uno la cima de la pila;
nombre_personaje = 'Rocket Raccoon'
print('a.')
print('El personaje', nombre_personaje,'se encuentra en la posicion', return_posicion_de_un_personaje(pila_personajes, nombre_personaje))
nombre_personaje = 'Groot'
print('El personaje', nombre_personaje,'se encuentra en la posicion', return_posicion_de_un_personaje(pila_personajes, nombre_personaje))
#b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar
#la cantidad de películas en la que aparece;
print('b.')
x= 5
personajes_con_participacion_en_mas_de_x_peliculas(pila_personajes,x)
#c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
print('c.')
personaje = 'Black Widow'
print('El personaje ', personaje,' participo en',return_cuantas_peliculas_participo_x_personaje(pila_personajes, personaje),'peliculas de la saga')
#d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.
print('d. Los personajes cuyos nombres empiezan con C, D o G son:')
x = ['C','D', 'G']
mostrar_todos_los_personajes_cuyos_nombre_empiezan_con_x_letras(pila_personajes, x)