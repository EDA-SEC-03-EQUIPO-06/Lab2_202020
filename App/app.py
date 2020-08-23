"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Este módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, y hacer búsquedas sobre una lista .
"""

import config as cf
import sys
import csv
from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt
from Sorting import insertionsort as ins
from Sorting import selectionsort as ss
from Sorting import shellsort as shell




from time import process_time 


def loadCSVFile (file, sep=";"):
    """
    Carga un archivo csv a una lista
    Args:
        file
            Archivo csv del cual se importaran los datos
        sep = ";"
            Separador utilizado para determinar cada objeto dentro del archivo
        Try:
        Intenta cargar el archivo CSV a la lista que se le pasa por parametro, si encuentra algun error
        Borra la lista e informa al usuario
    Returns: None  
    """
    #lst = lt.newList("ARRAY_LIST") #Usando implementacion arraylist
    lst = lt.newList() #Usando implementacion linkedlist
    print("Cargando archivo ....")
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=sep
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lt.addLast(lst,row)
    except:
        print("Hubo un error con la carga del archivo")
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return lst


def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Contar los elementos de la Lista")
    print("3- Contar elementos filtrados por palabra clave")
    print("4- Consultar elementos a partir de dos listas")
    print("5- Consultar ranking de películas")
    print("0- Salir")

def printMenuRanking():
    print("Elija el tipo de Ranking que desee")
    print("1- Ranking de las mejores películas por calificación")
    print("2- Ranking de las peores películas por calificación")
    print("3- Ranking de la películas más votadas")
    print("4- Ranking de las películas menos votadas")

def printMenuOrdenamiento():
    print("Especifique con qué método quiere ordenar su ranking: ")
    print("1- Insertion Sort")
    print("2- Selection Sort")
    print("3- Shell Sort")

def greater_function(element1,element2,column):
    if element1[column] > element2[column]:
        return True
    else:
        return False
def less_function(element1,element2,column):
    if element1[column] < element2[column]:
        return True
    else:
        return False

def countElementsFilteredByColumn(criteria, column, lst):
    """
    Retorna cuantos elementos coinciden con un criterio para una columna dada  
    Args:
        criteria:: str
            Critero sobre el cual se va a contar la cantidad de apariciones
        column
            Columna del arreglo sobre la cual se debe realizar el conteo
        list
            Lista en la cual se realizará el conteo, debe estar inicializada
    Return:
        counter :: int
            la cantidad de veces ue aparece un elemento con el criterio definido
    """
    if lst['size']==0:
        print("La lista esta vacía")  
        return 0
    else:
        t1_start = process_time() #tiempo inicial
        counter=0
        iterator = it.newIterator(lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            if criteria.lower() in element[column].lower(): #filtrar por palabra clave 
                counter+=1           
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return counter

def countElementsByCriteria(criteria, column, lst):
    """
    Retorna la cantidad de elementos que cumplen con un criterio para una columna dada
    """
    return 0


def orderElementsByCriteria(orderfunction, column, lista,compfunction, elements):
    """
    Retorna una lista con cierta cantidad de elementos ordenados por el criterio
    """
    t1_start = process_time() #tiempo inicial
    if orderfunction==1:
        ins.insertionSort(lista,compfunction,column)
    elif orderfunction==2:
        ss.selectionSort(lista,compfunction,column)
    elif orderfunction==3:
        shell.shellSort(lista,compfunction,column)
        ins.insertionSort(lista,compfunction,column)
    if 
    iterator=it.newIterator(lista)
    ranking=[]
    x=1
    while it.hasNext(iterator) and x<=elements:
        element=it.next(iterator)
        ranking.append(element.get("original_title"))
        x+=1
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    
    return ranking

def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """
    lista = lt.newList()   # se require usar lista definida
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:
            if int(inputs[0])==1: #opcion 1
                lista = loadCSVFile("Data/theMoviesdb/SmallMoviesDetailsCleaned.csv") #llamar funcion cargar datos
                print("Datos cargados, ",lista['size']," elementos cargados")
            elif int(inputs[0])==2: #opcion 2
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")    
                else: print("La lista tiene ",lista['size']," elementos")
            elif int(inputs[0])==3: #opcion 3
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:   
                    criteria =input('Ingrese el criterio de búsqueda\n')
                    counter=countElementsFilteredByColumn(criteria, "nombre", lista) #filtrar una columna por criterio  
                    print("Coinciden ",counter," elementos con el crtierio: ", criteria  )
            elif int(inputs[0])==4: #opcion 4
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    criteria =input('Ingrese el criterio de búsqueda\n')
                    counter=countElementsByCriteria(criteria,0,lista)
                    print("Coinciden ",counter," elementos con el crtierio: '", criteria ,"' (en construcción ...)")
            elif int(inputs[0])==5: #opcion 4
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    printMenuRanking()
                    tiporanking= int(input("Dígite su opción: "))
                    elements=int(input("Dígite el número de películas que desea ver en el ranking: "))
                    if tiporanking==1:
                        column="vote_average"
                        cmpfunction=greater_function
                    elif tiporanking==2:
                        column="vote_average"
                        cmpfunction=less_function
                    elif tiporanking==3:
                        column="vote_count"
                        cmpfunction=greater_function
                    elif tiporanking==4:
                        column="vote_count"
                        cmpfunction=less_function
                    printMenuOrdenamiento()
                    function=int(input("Digite su opción: "))
                    ranking=orderElementsByCriteria(function, column, lista,cmpfunction,elements)
                    print("El ranking es:  ",ranking)
            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()