﻿"""
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
from DISClib.Algorithms.Sorting import mergesort as mer
assert cf

"""
Se define la estructura de un catálogo de obras de arte. 
El catálogo tendrá dos listas, una para las obras de arte, 
otra para los artistas de estas.
"""

# Construccion de modelos

def newCatalog():
    """
    Inicializa el catálogo de obras de arte. 
    Crea listas vacías con los siguientes própositos:
    Para guardar las obras de arte
    Para guardar los autores
    Quizá luego se añaden más listas con los autores ordenados o lo que se necesite.
    """
    catalog = {'artists_BeginDate': None,
               'artworks_DateAcquired': None,
               'artists_artworks':None,
               'nationality':None}
    
    catalog['artists_BeginDate'] = lt.newList('ARRAY_LIST', cmpfunction=compareArtists_BeginDate)
    catalog['artworks_DateAcquired'] = lt.newList('ARRAY_LIST', cmpfunction=compareArtists_BeginDate)
    catalog['artists_artworks'] = lt.newList('ARRAY_LIST', cmpfunction=compareartists_artworks)
    catalog['nationality'] = lt.newList('ARRAY_LIST', cmpfunction=compareNationality)

    return catalog

# Funciones para agregar informacion al catalogo

def addArtist(catalog, artist):
    lt.addLast(catalog['artists_BeginDate'], artist)
    ids=artist["Nationality"]


def addArtwork(catalog, artwork):
    lt.addLast(catalog['artworks_DateAcquired'], artwork)
    ids = artwork['ConstituentID']
    ids = ids[1:-1].split(",")
    for id_ in ids:
        id_ = int(id_.strip())
        addArtworkArtist(catalog, id_, artwork)
        addNationality(catalog,id_,artwork)
    
def addArtworkArtist(catalog, id_:int, artwork):
    artist_artwork = catalog['artists_artworks']
    posartist = lt.isPresent(artist_artwork, id_)
    if posartist > 0:
        artist_id = lt.getElement(artist_artwork, posartist)
    else:
        artist_id = newArtworkArtist(id_)
        lt.addLast(artist_artwork, artist_id)
    lt.addLast(artist_id['artworks'],artwork )

def addNationality(catalog, id_:int, artwork):
    nationality = catalog['nationality']
    posartist=lt.isPresent(catalog["artists_BeginDate"], id_)
    nation = lt.getElement(catalog["artists_BeginDate"], posartist)["Nationality"]
    posnationality = lt.isPresent(nationality, nation)
    if posnationality > 0:
        nation_id = lt.getElement(nationality, posnationality)
    else:
        nation_id = newNationality(nation)
        lt.addLast(nationality, nation_id)
    lt.addLast(nation_id['artworks'],artwork )

# Funciones para creacion de datos

# =============================================================================
# def match_ids(catalog):
#     for i in lt.iterator(catalog['artists_BeginDate']):
#     ids = {'artist_id': artist_id, 'artwork_id': artwork_id}
#     return ids
# =============================================================================
def newArtworkArtist(artist_id):
    """
    Crea una nueva estructura para modelar los autores de cada obra
    """
    nationality = {'nation':"",'artworks':None}
    nationality['nation'] = artist_id
    nationality['artworks'] = lt.newList('ARRAY_LIST')
    return nationality

def newNationality(nation):
    """
    Crea una nueva estructura para modelar los autores de cada obra
    """
    artwork_artist = {'artist':"",'artworks':None}
    artwork_artist['artist'] = nation
    artwork_artist['artworks'] = lt.newList('ARRAY_LIST')
    return artwork_artist
# Funciones de consulta

def rangoArtists(catalog, anio1, anio2):
    artists = catalog["artists_BeginDate"].copy()
    start_time = time.process_time()
    start=float("inf")
    pos=1
    while pos<=lt.size(artists):
        if int(lt.getElement(artists,pos)["BeginDate"])>=anio1:
            start=pos
            break
        pos+=1
    initial=start
    num=0
    while start<=lt.size(artists):
        if int(lt.getElement(artists,start)["BeginDate"])<=anio2:
            num+=1
        else:
            break
        start+=1
    answ = lt.subList(artists,initial,num)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return answ
    
def rangoArtworks(catalog, fecha1, fecha2):
    artworks = catalog["artworks_DateAcquired"].copy()
    start_time = time.process_time()
    start=float("inf")
    pos=1
    while pos<=lt.size(artworks):
        if lt.getElement(artworks,pos)["DateAcquired"] != "":
            if datetime.strptime(lt.getElement(artworks,pos)["DateAcquired"], '%Y-%m-%d').date()>=datetime.strptime(fecha1, '%Y-%m-%d').date():
                start=pos
                break
        pos+=1
    initial=start
    num=0
    while start<=lt.size(artworks):
        if datetime.strptime(lt.getElement(artworks,start)["DateAcquired"], '%Y-%m-%d').date()<=datetime.strptime(fecha2, '%Y-%m-%d').date():
            num+=1
        else:
            break
        start+=1
    answ = lt.subList(artworks,initial,num)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return answ

def id_artist(catalog, artist):
    """
    reorna el id de un artista. O(n)
    """
    id_=0
    for i in lt.iterator(catalog['artists_BeginDate']):
        if i['DisplayName']==artist:
            id_ = i['ConstituentID']
            break
    return id_

def artist_artworks(catalog, artist):
    """
    Nombre, ID y lista de las obras de un artista determinado. O(n)
    """
    id_=id_artist(catalog, artist)
    list_=lt.newList('ARRAY_LIST')
    for i in lt.iterator(catalog['artworks_DateAcquired']):
        if id_ in i['ConstituentID']:                
            lt.addLast(list_, i)
    return artist, id_, list_

def artist_medium(catalog, artist):
    mediums_= lt.newList('ARRAY_LIST')
    mediums_count = lt.newList('ARRAY_LIST')
    artist, id_, list_ = artist_artworks(catalog, artist)
    for i in lt.iterator(list_):
        posmedium = lt.isPresent(mediums_, i['Medium'])
        if posmedium == 0:
            medium = lt.addLast(mediums_, i['Medium'])
            lt.addLast(mediums_count, 1)
        else:
            lt.changeInfo(mediums_count, posmedium, lt.getElement(mediums_count, posmedium))
    greatest=0
    count=0
    for num in lt.iterator(mediums_count):
        count+=1
        if num > greatest:
            greatest=num
            pos_most_used=count
    return artist,id_, list_,mediums_,mediums_count,pos_most_used

# Funciones utilizadas para comparar elementos dentro de una lista

def compareArtworks_DateAcquired(artwork1:dict , artwork2:dict)->int:
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

def compareArtists_BeginDate(artist1,artist2):
    if artist1["BeginDate"]<=artist2["BeginDate"]:
        return -1
    else:
        return 0

def compareartists_artworks(artist_id, artist):
    if artist_id == artist['artist']:
        return 0
    return -1
    
def compareNationality(artist_id, artist):
    if artist_id == artist['artist']:
        return 0
    return -1

# =============================================================================
# def compareArtists__ConstituentID(artist1,artist2):
#     if artist1["ConstituentID"]<=artist2["ConstituentID"]:
#         return -1
#     else:
#         return 0
# =============================================================================

# Funciones de ordenamiento

def sortArtworks_DateAcquired(catalog):
    sub_list = catalog["artworks_DateAcquired"].copy()
    start_time = time.process_time()
    sorted_list= mer.sort(sub_list, compareArtworks_DateAcquired)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list

def sortArtists_BeginDate(catalog):
    sub_list = catalog["artists_BeginDate"].copy()
    start_time = time.process_time()
    sorted_list= mer.sort(sub_list, compareArtists_BeginDate)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list

# =============================================================================
# def sortArtists_ConstituentID(catalog):
#     sub_list = catalog["artists_ConstituentID"].copy()
#     start_time = time.process_time()
#     sorted_list= mer.sort(sub_list, compareArtists__ConstituentID)
#     stop_time = time.process_time()
#     elapsed_time_mseg = (stop_time - start_time)*1000
#     return elapsed_time_mseg, sorted_list
# =============================================================================
