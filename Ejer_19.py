'''
19. Dada una pila de películas de las que se conoce su título, estudio cinematográfico y año de estreno,
desarrollar las funciones necesarias para resolver las siguientes actividades:
a. mostrar los nombre películas estrenadas en el año 2014;
b. indicar cuántas películas se estrenaron en el año 2018;
c. mostrar las películas de Marvel Studios estrenadas en el año 2016.
'''

#from random import randint
from pila import Pila
class Pelicula():
    titulo, estudio_cinematografico, anio_de_estreno = None, None, None

def cargar_pelicula(pelicula):
    #pelicula = Pelicula()
    pelicula.titulo = input("Cúal es el titulo de la pelicula? ")
    pelicula.estudio_cinematografico = input("Cúal es el estudio cinematografico? ")
    pelicula.anio_de_estreno = input("Cúal es el anio de estreno? ")

def mostrar_nombres_peliculas_de_x_anio(pila, anio):
    pila_aux= Pila()
    while(not pila.pila_vacia()):
        pelicula = pila.desapilar()
        #print(pelicula.anio_de_estreno)
        if(pelicula.anio_de_estreno == anio):
            #print('Titulo de la pelicula: ', pelicula.titulo)
            #print('La pelicula "', pelicula.titulo,'" fue estrenada en el anio', anio)
            print('-',pelicula.titulo)
        pila_aux.apilar(pelicula)
    while(not pila_aux.pila_vacia()):
        pila.apilar(pila_aux.desapilar())

def mostrar_peliculas_de_x_estudio_y_de_x_anio(pila, estudio, anio):
    pila_aux= Pila()
    while(not pila.pila_vacia()):
        pelicula = pila.desapilar()
        #print(pelicula.anio_de_estreno)
        if(pelicula.estudio_cinematografico == estudio) and (pelicula.anio_de_estreno == anio):
            print('- Titulo: ',pelicula.titulo)
            print('  Estudio cinematografico: ',pelicula.estudio_cinematografico)
            print('  Anio: ',pelicula.anio_de_estreno)
        pila_aux.apilar(pelicula)
    while(not pila_aux.pila_vacia()):
        pila.apilar(pila_aux.desapilar())

def return_cantidad_peliculas_de_x_anio(pila, anio):
    cantidad = 0
    pila_aux= Pila()
    while(not pila.pila_vacia()):
        pelicula = pila.desapilar()
        #print(pelicula.anio_de_estreno)
        if(pelicula.anio_de_estreno == anio):
            #print('Titulo de la pelicula: ', pelicula.titulo)
            cantidad+= 1
        pila_aux.apilar(pelicula)
    while(not pila_aux.pila_vacia()):
        pila.apilar(pila_aux.desapilar())
    return cantidad



pila_peliculas = Pila()
'''
for i in range(3):#Se carga la pila con 3 peliculas
    pelicula_aux = Pelicula()
    cargar_pelicula(pelicula_aux)
    pila_peliculas.apilar(pelicula_aux)
pelicula_aux = Pelicula()
'''

pelicula_aux = Pelicula()
pelicula_aux.titulo = 'Pelicula 1'
pelicula_aux.estudio_cinematografico = 'Paramount'
pelicula_aux.anio_de_estreno = 2014
pila_peliculas.apilar(pelicula_aux)

pelicula_aux = Pelicula()
pelicula_aux.titulo = 'Pelicula 2'
pelicula_aux.estudio_cinematografico = 'Marvel Studios'
pelicula_aux.anio_de_estreno = 2014
pila_peliculas.apilar(pelicula_aux)

pelicula_aux = Pelicula()
pelicula_aux.titulo = 'Pelicula 3'
pelicula_aux.estudio_cinematografico = 'Marvel Studios'
pelicula_aux.anio_de_estreno = 2016
pila_peliculas.apilar(pelicula_aux)

pelicula_aux = Pelicula()
pelicula_aux.titulo = 'Pelicula 4'
pelicula_aux.estudio_cinematografico = 'Paramount'
pelicula_aux.anio_de_estreno = 2018
pila_peliculas.apilar(pelicula_aux)

#a. mostrar los nombre películas estrenadas en el anio 2014;
print('a.En el anio 2014 se estrenaron las siguientes peliculas:')
anio = 2014
mostrar_nombres_peliculas_de_x_anio(pila_peliculas, anio)

#b. indicar cuántas películas se estrenaron en el anio 2018;
anio = 2018
print('b.En el anio 2018 se estrenaron', return_cantidad_peliculas_de_x_anio(pila_peliculas, anio),'peliculas')

#c. mostrar las películas de Marvel Studios estrenadas en el anio 2016.
estudio = 'Marvel Studios'
anio = 2016
print('c.Las películas de',estudio,'estrenadas en el anio',anio,'son:')
mostrar_peliculas_de_x_estudio_y_de_x_anio(pila_peliculas, estudio, anio)