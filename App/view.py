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
from prettytable import PrettyTable
import time
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
    print("Req. No. 1. Listar cronológicamente los artistas.")
    print("Req. No. 2. Listar cronológicamente las adquisiciones.")
    print("Req. No. 3. Clasificar las obras de un artista por técnica.")
    print("Req. No. 4. Clasificar las obras por la nacionalidad de sus creadores.")
    print("Req. No. 5. Transportar obras de un departamento.")
    print("Req. No. 6 (Bono). Proponer una nueva exposición en el museo.")
    print("7. Detener la ejecución del programa.")
    
def printloadData():
    print("Cargando información de los archivos ....")
    catalog = initCatalog()
    loadData(catalog)
    artist=controller.sortArtists_BeginDate(catalog)
    artwork=controller.sortArtworks_DateAcquired(catalog)
    nationality=controller.sortNationality(catalog)
    catalog["artists_BeginDate"]=artist[1]
    catalog["artworks_DateAquired"]=artwork[1]
    catalog["nationality"]=nationality[1]
    print('Número de artistas en el catálogo: ',
          str(lt.size(catalog['artists_BeginDate'])))
    print('Número de obras de arte en el catálogo: ',
          str(lt.size(catalog['artworks_DateAquired'])))
    print("Se demoro: ",str(artist[0]))
    print('\nÚltimos tres artistas cargados:\n')
    for i in [-2,-1,0]:
        print(str(lt.getElement(catalog['artists_BeginDate'],i)))
    print("Se demoro: ",str(artwork[0]))
    print('\nÚltimas tres obras de arte cargadas:\n')
    for i in [-2,-1,0]:
        print(str(lt.getElement(catalog['artworks_DateAquired'],i)))
        
        # Toca quitar lo de artists_artworks esto del cargar datos, pero funciona!
    print('\nARTISTS ARTWORKS:\n')
    for i in [12,13,14]:
        print(str(lt.getElement(catalog['artists_artworks'],i)))

    print('\nNationality:\n')
    for i in [-3,-2,-1,0]:
        print(str(lt.getElement(catalog['nationality'],i)["nation"]))
    return catalog
    
def printReq1():
    start_time = time.process_time()
    anio1=int(input("Digite un año inicial: "))
    anio2=int(input("Digite un año final: "))
    result=controller.rangoArtists(catalog, anio1, anio2)
    print("======================== Req No. 1 Inputs ========================")
    print("Artistas nacidos entre ",str(anio1)," y ",str(anio2)),"."
    print("======================== Req No. 1 Respuesta ========================")
    print("Hay ",str(lt.size(result))," artistas nacidos entre ",
          str(anio1)," y ",str(anio2)),"."
    print('\nPrimeros y últimos tres artistas nacidos en el rango de años:\n')
    answ = PrettyTable(['Nombre','Nacimiento','Fallecimiento'
                        ,'Nacionalidad','Género'])
    for i in [1,2,3,-2,-1,0]:        
        answ.add_row([lt.getElement(result,i)['DisplayName'],
                      lt.getElement(result,i)['BeginDate'],
                      lt.getElement(result,i)['EndDate'],
                      lt.getElement(result,i)['Nationality'],
                      lt.getElement(result,i)['Gender']])
    answ._max_width = {'Nombre':40}
    print(answ)    
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    print("Se demoro: ",str(elapsed_time_mseg))

def printReq2():
    start_time = time.process_time()
    fecha1=input("Ingrese una fecha inicial en formato AAAA-MM-DD: ")
    fecha2=input("Ingrese una fecha final en formato AAAA-MM-DD: ")
    result = controller.rangoArtworks(catalog, fecha1, fecha2)
    num_artists = 5 # TODO: FALTA Toca asociar con los artistas para esto
    num_purchased = 5 # TODO: Falta
    print("======================== Req No. 1 Inputs ========================")
    print("Obras adquiridas entre ",fecha1," y ",fecha2)
    print("======================== Req No. 1 Respuesta ========================")
    print("El MoMA adquirió ",str(lt.size(result))," obras entre ",fecha1,
          " y ",fecha2," con ",str(num_artists),
          " artistas, de las cuales compró ",str(num_purchased))
    print('\nPrimeras y últimas tres obras adquiridas en el rango de fechas:\n')
    answ = PrettyTable(['Título','Artista(s)','Fecha','Medio',
                        'Dimensiones'])
    for i in [1,2,3,-2,-1,0]:        
        answ.add_row([lt.getElement(result,i)['Title'],
                      lt.getElement(result,i)['ConstituentID'], # TODO: Artista
                      lt.getElement(result,i)['DateAcquired'],
                      lt.getElement(result,i)['Medium'],
                      lt.getElement(result,i)['Dimensions']])
    answ._max_width = {'Título':40,'Artista(s)':20,'Fecha':20,'Medio':40,
                        'Dimensiones':40}
    print(answ)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    print("Se demoro: ",str(elapsed_time_mseg))

def printReq3():
    start_time = time.process_time()
    artist=input("Ingrese el nombre del artista: ")
    artist,id_, list_,mediums_,mediums_count,pos_most_used=controller.artist_medium(catalog,artist)
    print("======================== Req No. 3 Inputs ========================")
    print("Examinar el trabajo del artista de nombre ",artist)
    print("======================== Req No. 3 Respuesta ========================")
    print("El artista ",str(artist).strip(),' con código ',str(id_),' tiene ',
          str(lt.size(list_)), 'obras en el MoMA.')
    print("Medios: ",mediums_)
# =============================================================================
#     print('Usó ',mediums_count,' medios o técnicas distintas en su trabajo.')
#     print('La técnica que más usó es: ',lt.getElement(mediums_,pos_most_used),'.')
# =============================================================================

def printReq4():
    start_time = time.process_time()
    print("======================== Req No. 4 Inputs ========================")
    print("Ranking de paises por su numero de obras en el MoMa ")
    print("======================== Req No. 4 Respuesta ========================")
    print("Top 10 paises en el MoMa son:")
    answ = PrettyTable(['Nacionalidad','Obras'])
    for i in [0,-1,-2,-3,-4,-5,-6,-7,-8,-9]:
        answ.add_row([lt.getElement(catalog['nationality'],i)['nation'],
                      lt.size(lt.getElement(catalog['nationality'],i)['artworks'])])
    answ._max_width = {'Título':40,'Obras':20}
    print(answ)
    mejor=lt.getElement(catalog['nationality'],0)
    print("La nacionalidad top en el museo es ", mejor["nation"], " con ",lt.size(mejor["artworks"]))
    print("Las primeras y ultimos 3 objetos para las obras de ",mejor["nation"]," son:")
    answ = PrettyTable(['ID','Titulo',"Nombre del artista","Medium","Fecha",
                        "Dimensiones","Departamento","Clasificacion","URL"])
    for i in [1,2,3,-2,-1,0]:
        answ.add_row([lt.getElement(mejor["artworks"],i)['ObjectID'],
                      lt.getElement(mejor["artworks"],i)['Title'],
                      lt.getElement(mejor["artworks"],i)['ConstituentID'],
                      lt.getElement(mejor["artworks"],i)['Medium'],
                      lt.getElement(mejor["artworks"],i)['Date'],
                      lt.getElement(mejor["artworks"],i)['Dimensions'],
                      lt.getElement(mejor["artworks"],i)['Department'],
                      lt.getElement(mejor["artworks"],i)['Classification'],
                      lt.getElement(mejor["artworks"],i)['URL']])
    answ._max_width = {'ID':20,'Titulo':40,"Nombre del artista":20,"Medium":20,
                    "Fecha":20,"Dimensiones":20,"Departamento":20,"Clasificacion":20,"URL":40}
    print(answ)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    print("Se demoro: ",str(elapsed_time_mseg))

def printReq5():
    print("Este requerimiento aún no se ha implementado.")
    
def printReq6():
    print("Este requerimiento aún no se ha implementado.")
    
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
    error = "\nError: Por favor ingrese un número entero entre 0 y 7.\n"
    error_cargar= "\nError: Se deben cargar los datos antes de usar los requisitos.\n"
    printMenu()
    try:
        inputs = int(input('Seleccione una opción para continuar: \n'))
    except:
        print(error)
        continue
    if inputs == 0:
        catalog=printloadData()
    elif inputs>0 and inputs<7:
        if type(catalog)!=dict:
            print(error_cargar)
        elif inputs==1:
            printReq1()
        elif inputs==2:
            printReq2()
        elif inputs==3:
            printReq3()
        elif inputs==4:
            printReq4()
        elif inputs==5:
            printReq5()
        elif inputs==6:
            printReq6()
    elif inputs >= 8:
        print(error)
    else:
        sys.exit(0)
sys.exit(0)