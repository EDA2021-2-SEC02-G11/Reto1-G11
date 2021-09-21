"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
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
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf

"""
La vista se encarga de la interacción con el usuario
Presenta el menú de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    """
    Imprime las opciones del menú.
    """
    print("\nMenú de opciones:\n")
    print("0. Cargar información en el catálogo.")
    print("Requisito 1. Listar cronológicamente las artistas.")
    print("Requisito 2. Listar cronológicamente los adquisiciones.")
    print("Requisito 3. Clasificar las obras de un artista por técnica.")
    print("Requisito 4. Clasificar las obras por la nacionalidad de sus creadores.")
    print("Requisito 5. Transportar obras de un departamento.")
    print("Requisito 6 (Bono). Proponer una nueva exposición en el museo.")
    print("7. Detener la ejecución del programa.")

def initCatalog():
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog()

def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)

catalog = None

"""
Menú principal
"""
while True:
    error = "Por favor ingrese un número entero entre 0 y 7."
    printMenu()
    try:
        inputs = int(input('Seleccione una opción para continuar: \n'))
    except:
        print(error)
        continue
    if inputs == 0:
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)
        print('Número de artistas en el catálogo: ',str(lt.size(catalog['artists'])))
        print('Número de obras de arte en el catálogo: ',str(lt.size(catalog['artworks'])))
        print('\nÚltimos tres artistas cargados:\n')
        for i in [-3,-2,-1]:
            print(str(lt.getElement(catalog['artists'],i)))
        print('\nÚltimas tres obras de arte cargadas:\n')
        for i in [-3,-2,-1]:
            print(str(lt.getElement(catalog['artworks'],i)))  
    elif inputs==1:
        ano_inicial = input("Indique un año inicial: ")
        ano_final = input("Indique un año final: ")
# =============================================================================
#         En este momento, los artistas se ordenan cuando se cargan los datos
#         al catálogo, que creo yo es lo más eficiente. Me toca hacer una función
#         que, de esa lista ordenada, coja solo los artistas en el rango
#         cronológico dado (en este momento coge todos los cargados). Antes se 
#         estaba usando un tamaño de muestra, que era más fácil, pero toca
#         hacerlo con rangos.
# =============================================================================
        print('\nPrimeros tres artistas del rango cronológico:\n')
        for i in [1,2,3]:
            print(str(lt.getElement(catalog['artists_chronologically'],i)))
        print('\nÚltimos tres artistas del rango cronológico:\n')
        for i in [-3,-2,-1]:
            print(str(lt.getElement(catalog['artists_chronologically'],i)))
    elif inputs==2:
        fecha_inicial = input("Indique una fecha inicial con el formato (AAAA-MM-DD): ")
        fecha_final = input("Indique una fecha final con el formato (AAAA-MM-DD): ")
# =============================================================================
#         Al igual que la anterior, las obras de arte se ordenan cuando se 
#         cargan al catálogo y se están tomando todas, no se está respetando el 
#         rango. Toca hacer esa función.
# =============================================================================
        print('\nPrimeras tres obras de arte adquiridas en el rango cronológico:\n')
        for i in [1,2,3]:
            print(str(lt.getElement(catalog['artworks_chronologically'],i)))
        print('\nÚltimas tres obras de arte adquiridas en el rango cronológico:\n')
        for i in [-3,-2,-1]:
            print(str(lt.getElement(catalog['artworks_chronologically'],i)))
    elif (inputs==1) or ((inputs>2) and (inputs<7)):
        print("Este requerimiento aún no se ha implementado.")
    elif inputs >= 8:
        print(error)
    else:
        sys.exit(0)
sys.exit(0)
