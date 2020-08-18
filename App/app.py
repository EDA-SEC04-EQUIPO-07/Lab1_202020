
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
  Este módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, y hacer búsquedas sobre una lista.
"""

#Imports

import config as cf
import sys
import csv
from time import process_time 

#Funciones

def loadCSVFile (file:str, lst:list, sep=";")->list:
    """
    Carga un archivo csv a una lista
    Args:
        file 
            Archivo de texto del cual se cargaran los datos requeridos.
        lst :: []
            Lista a la cual quedaran cargados los elementos despues de la lectura del archivo.
        sep :: str
            Separador escodigo para diferenciar a los distintos elementos dentro del archivo.
    Try:
        Intenta cargar el archivo CSV a la lista que se le pasa por parametro, si encuentra algun error
        Borra la lista e informa al usuario
    Returns: None   
    """
    del lst[:]
    print("Cargando archivo ....")
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=sep
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lst.append(row)
    except:
        del lst[:]
        print("Se presento un error en la carga del archivo")
    
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    
def loadCSFile2(file:str, lst2:list, sep=';')->list:
    del lst2[:]
    print("Cargando archivo ....")
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=sep
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lst2.append(row)
    except:
        del lst2[:]
        print("Se presento un error en la carga del archivo")
    
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")

def countElementsFilteredByColumn(criteria:str, column:str, lst:list)->int:
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
    if len(lst)==0:
        print("La lista esta vacía")  
        return 0
    else:
        t1_start = process_time() #tiempo inicial
        counter=0 #Cantidad de repeticiones
        for element in lst:
            if criteria.lower() in element[column].lower(): #filtrar por palabra clave 
                counter+=1
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return counter

def countElementsByCriteria(criteria:str, column:str, lst:list, lst2:list)->int:
    """
    Retorna la cantidad de elementos que cumplen con un criterio para una columna dada
    """
    t1_start=process_time()
    contador=0
    if len(lst)==0 or len(lst2)==0:
        print("\nUna de las listas esta vacia.")
    else:
        for diccionario in lst:
            for key in diccionario:
                if key.lower() == column.lower() and diccionario[key].lower() ==criteria.lower():
                    contador+=1
        for diccionario in lst2:
            for key in diccionario:
                if key.lower() == column.lower() and diccionario[key].lower() ==criteria.lower():
                    contador+=1
    t1_stop=process_time()
    print("Tiempo de ejecucion de: ",t1_stop-t1_start," segundos")
    return contador

def findmovies(director:str, lst:list, lst2:list)->dict:
    ans={}
    meter=0
    average=0
    for element in lst:
        drt=element["director_name"].lower()
        vote=int(element["vote_average"])
        if director == drt:
            i_d=element["id"]
            for movie in lst2:
                if movie["id"]==i_d:
                    vote=int(movie["vote_average"])
                    if vote >=6:
                        meter+=1
                        average+=vote
    average=(average/meter)
    ans["contador"]==meter
    ans["promedio"]=average
    return ans

def printMenu():
    """
    Imprime el menu de opciones
    """
    print("-"*50)
    print("Bienvenido")
    print("-"*50)
    print("1- Cargar Datos lista #1.")
    print("2- cargar Datos lista #2.")
    print("3- Contar los elementos de la Lista.")
    print("4- Contar elementos filtrados por palabra clave.")
    print("5- Consultar elementos a partir de dos listas.")
    print("6- Consultar peliculas buenas de un director.")
    print("0- Salir")

def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """
    lista = [] #instanciar una lista vacia
    lista2= [] 
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar:\n') #leer opción ingresada
        if len(inputs)>0:
            if int(inputs[0])==1: #opcion 1
                file=input("Escriba la direcion del archivo:\n")
                loadCSVFile(file, lista) #llamar funcion cargar datos
                print("Datos cargados, "+str(len(lista))+" elementos cargados")
            elif int(inputs[0])==2: #opcion 2 (nueva funcion de carga)
                file=input("Ingrese la ruta del archivo a cargar:\n")
                loadCSFile2(file,lista2)
                print("Datos cargados, "+str(len(lista2))+" elementos cargados")
            elif int(inputs[0])==3: #opcion 3
                if len(lista)==0: #obtener la longitud de la lista
                    print("La lista esta vacía")    
                else: print("La lista tiene "+str(len(lista))+" elementos")
            elif int(inputs[0])==4: #opcion 4
                criteria =input('Ingrese el criterio de búsqueda\n')
                counter=countElementsFilteredByColumn(criteria, "nombre", lista) #filtrar una columna por criterio  
                print("Coinciden ",counter," elementos con el crtierio: ", criteria  )
            elif int(inputs[0])==5: #opcion 5
                criteria =input('Ingrese el criterio de búsqueda\n')
                columna=input('Ingrese la Columna que desea filtar: ')
                counter=countElementsByCriteria(criteria,columna,lista,lista2)
                print("Coinciden ",counter," elementos con el crtierio: '", criteria ,"' (en construcción ...)")
            elif int(inputs[0])==6:
                name=input("Escriba el nombre del director del cual desea saber buenas peliculas:\n")
                ans=findmovies(name,lista,lista2)
                print("\nLa cantidad de peliculas buenas de ese dierector son: ",ans["meter"])
                print("\nLa votacion promedio fue: ",ans["average"])
            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)

if __name__ == "__main__":
    main()