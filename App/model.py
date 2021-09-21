"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from datetime import datetime
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort
from DISClib.Algorithms.Sorting import insertionsort
from DISClib.Algorithms.Sorting import mergesort
from DISClib.Algorithms.Sorting import quicksort
from DISClib.Algorithms.Sorting import selectionsort
assert cf

# Construcción de modelos

def newCatalog():
    """
    Inicializa el catálogo de obras de arte.
    """
    catalog = {'artists': None,
               'artworks': None,
               'artists_chronologically': None,
               'artworks_chronologically': None}
    
    artists = lt.newList('ARRAY_LIST', cmpfunction=compare_artists)
    catalog['artists'] = artists
    artworks = lt.newList('ARRAY_LIST', cmpfunction=compare_artworks)
    catalog['artworks'] = artworks
    catalog['artworks_chronologically'] = sortArtworks(artworks)[1]
    catalog['artists_chronologically'] = sortArtists(artists)[1]
    return catalog

# Funciones para agregar informacion al catálogo

def addArtist(catalog, artist):
    # Se añade el artista al final de la lista de artistas en el catálogo.
    lt.addLast(catalog['artists'], artist)

def addArtwork(catalog, artwork):
    # Se añade la obra de arte al final de la lista de obras de arte en el catálogo.
    lt.addLast(catalog['artworks'], artwork)

# Funciones para creacion de datos

# Funciones de consulta

def artists_chronologically_interval(ano_inicial, ano_final):
    pass

def artworks_chronologically_interval(fecha_inicial, fecha_final):
    pass

# Funciones utilizadas para comparar elementos dentro de una lista

def compare_artists():
    pass

def compare_artworks():
    pass

def compare_artworks_DateAcquired(artwork1:dict , artwork2:dict)->int:
    """
    Compara dos obras de arte por la fecha en la que fueron adquiridas, 
    'DateAcquired'.
    
    Si el 'DateAcquired' de una obra de arte es vacío, la obra se toma como 
    la más antigua.

    Parámetros
    ----------
    artwork1 : dict
        Informacion de la primera obra que incluye su valor 'DateAcquired'.
    artwork2 : dict
        Informacion de la segunda obra que incluye su valor 'DateAcquired'.

    Retorno
    -------
    int
        0 si artwork1 fue adquirido más recientemente que artwork2.
        -1 si artwork2 fue adquirido más recientemente que artwork1.
    """
    if artwork1["DateAcquired"]=="" or artwork2["DateAcquired"]=="":
        if artwork1["DateAcquired"]=="":
            return -1
        else:
            return 0
    elif datetime.strptime(artwork1["DateAcquired"], '%Y-%m-%d').date()<datetime.strptime(artwork2["DateAcquired"], '%Y-%m-%d').date():
        return -1
    return 0

def compare_artists_BeginDate(artist1:dict , artist2:dict)->int:
    """
    Compara dos artistas por su fecha de nacimiento,'BeginDate'.
    
    Si el 'BeginDate' de un artista vacío, la fecha de nacimiento se toma como 
    anterior a todas las demás.

    Parámetros
    ----------
    artist1 : dict
        Informacion del primer artista que incluye su valor 'BeginDate'.
    artist2 : dict
        Informacion del segundo artista que incluye su valor 'DateAcquired'.

    Retorno
    -------
    int
        0 si artwork1 fue adquirido más recientemente que artwork2.
        -1 si artwork2 fue adquirido más recientemente que artwork1.
    """
    if artist1["BeginDate"]=="" or artist2["BeginDate"]=="":
        if artist1["DateAcquired"]=="":
            return -1
        else:
            return 0
    elif artist1["BeginDate"]<artist2["BeginDate"]:
        return -1
    return 0

# Funciones de ordenamiento

def sortArtworks(artworks, algorithm=mergesort):
    """
    Ordena las obras de arte por la fecha en la que fueron adquiridas, 
    'DateAcquired', haciendo uso del algoritmo dado. 
    Informa cuánto tiempo demoró en ordenarlas.    

    Parameters
    ----------
    artworks : 
        Lista de obras de arte.
    algorithm : 
        Algoritmo que será usado para ordenar.

    Returns
    -------
    elapsed_time_mseg : float
        Tiempo que tardó el ordenamiento en milisegundos.
    sorted_list : 
        Lista de obras de arte ordenadas por la fecha en la que fueron 
        adquiridas.
    """    
    start_time = time.process_time()
    sorted_list = algorithm.sort(artworks, compare_artworks_DateAcquired)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list

def sortArtists(artists, algorithm=mergesort):
    """
    Ordena los artistas por su fecha de nacimiento, 'BeginDate', haciendo 
    uso del algoritmo dado. 
    
    Informa cuánto tiempo demoró en ordenarlos.    

    Parameters
    ----------
    artists : 
        Lista de artistas.
    algorithm : 
        Algoritmo que será usado para ordenar.

    Returns
    -------
    elapsed_time_mseg : float
        Tiempo que tardó el ordenamiento en milisegundos.
    sorted_list : 
        Lista de artistas ordenados por su fecha de nacimiento.
    """    
    start_time = time.process_time()
    sorted_list = algorithm.sort(artists, compare_artists_BeginDate)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list