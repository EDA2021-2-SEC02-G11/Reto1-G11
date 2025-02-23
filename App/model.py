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
               'artworks_Date': None,
               'artworks_Artist':None,
               'nationality':None}
    
    catalog['artists_BeginDate'] = lt.newList('ARRAY_LIST', cmpfunction=compareArtists_BeginDate)
    catalog['artworks_DateAcquired'] = lt.newList('ARRAY_LIST', cmpfunction=compareArtworks_DateAcquired)
    catalog['artworks_Date'] = lt.newList('ARRAY_LIST', cmpfunction=compareArtworks_Date)
    catalog['artworks_Artist'] = lt.newList('ARRAY_LIST', cmpfunction=compareArtworks_Artist)
    catalog['nationality'] = lt.newList('ARRAY_LIST', cmpfunction=compareNationality)

    return catalog

# Funciones para agregar informacion al catalogo

def addArtist(catalog, artist):
    lt.addLast(catalog['artists_BeginDate'], artist)
    ids=artist["Nationality"]

def addArtwork(catalog, artwork):
    lt.addLast(catalog['artworks_DateAcquired'], artwork)
    lt.addLast(catalog['artworks_Date'], artwork)
    ids = artwork['ConstituentID']
    ids = ids[1:-1].split(",")
    for id_ in ids:
        id_ = int(id_.strip())
        addArtworks_Artist(catalog, id_, artwork)
        addNationality(catalog,id_,artwork)

def addArtworks_Artist(catalog, id_:int, artwork):
    artist_artwork = catalog['artworks_Artist']
    posartist = lt.isPresent(artist_artwork, id_)
    if posartist > 0:
        artist_id = lt.getElement(artist_artwork, posartist)
    else:
        artist_id = newArtworks_Artist(id_)
        lt.addLast(artist_artwork, artist_id)
    lt.addLast(artist_id['artworks'],artwork )

def addNationality(catalog, id_, artwork):
    nationality = catalog['nationality']
    nation=id_nation(catalog,id_)
    posnationality = lt.isPresent(nationality, nation)
    if posnationality > 0:
        nation_id = lt.getElement(nationality, posnationality)
    else:
        nation_id = newNationality(nation)
        lt.addLast(nationality, nation_id)
    lt.addLast(nation_id['artworks'],artwork )

# Funciones para creacion de datos

def newArtworks_Artist(id_):
    """
    Crea una nueva estructura para modelar las obras por autor.
    """
    answ = {'artist':"",'artworks':None}
    answ['artist'] = id_
    answ['artworks'] = lt.newList('ARRAY_LIST')
    return answ

def newNationality(nation):
    """
    Crea una nueva estructura para modelar los autores de cada obra
    """
    nationality = {'nation':"",'artworks':None}
    nationality['nation'] = nation
    nationality['artworks'] = lt.newList('ARRAY_LIST')
    return nationality

# Funciones de consulta

# Req. 1
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

# Req. 2
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

# Req. 3
def id_artist(catalog, artist):
    """
    reorna el id de un artista. O(n)
    """
    id_=0
    for i in lt.iterator(catalog['artists_BeginDate']):
        if i['DisplayName']==artist:
            id_ = i['ConstituentID']
            break
    return id_,artist

def artist_artworks(catalog, artist):
    """
    Nombre, ID y lista de las obras de un artista determinado. O(n)
    """
    id_=id_artist(catalog, artist) # ID del artista
    artworks_by_artist=lt.newList('ARRAY_LIST',key='ObjectID')
    for i in lt.iterator(catalog['artworks_DateAcquired']):
        if id_ in i['ConstituentID'][1:-1].split(","):
            lt.addLast(artworks_by_artist, i)
    return artworks_by_artist,artist,id_

def artist_medium1(catalog, artist):
    mediums= lt.newList('ARRAY_LIST')
    mediums_count = lt.newList('ARRAY_LIST')
    id_,artist=id_artist(catalog, artist)
    for i in lt.iterator(catalog['artworks_Artist']):
        if int(i['artist']) == int(id_):
            artworks_by_artist=i['artworks']
            break
    for i in lt.iterator(artworks_by_artist):
        posmedium = lt.isPresent(mediums, i['Medium'])
        if posmedium <= 0: # Si no está el medio en la lista de medios
            lt.addLast(mediums, i['Medium'])
            lt.addLast(mediums_count, 1)
        else: # Si sí está el medio en la lista de medios
            lt.changeInfo(mediums_count, posmedium, lt.getElement(mediums_count, posmedium)+1)
    greatest=0
    pos_actual=0
    for cuenta_medium in lt.iterator(mediums_count):
        pos_actual+=1
        if cuenta_medium > greatest:
            greatest=cuenta_medium
            pos_most_used=pos_actual
    artworks_medium= lt.newList('ARRAY_LIST')        
    for obra in lt.iterator(artworks_by_artist):
        if obra['Medium']==lt.getElement(mediums,pos_most_used):
            lt.addLast(artworks_medium, obra)
    return artist,id_,artworks_by_artist,mediums,artworks_medium,pos_most_used

# Forma alternativa de implementar el Req. 3 sin usar la lista 'artworks_Artist'
# del catálogo. Esta no es la que se usa porque es más rápido ayudarse con la
#lista que se carga directamente del catálogo.
def artist_medium(catalog, artist):
    mediums= lt.newList('ARRAY_LIST')
    mediums_count = lt.newList('ARRAY_LIST')
    artworks_by_artist,artist,id_= artist_artworks(catalog, artist)
    for i in lt.iterator(artworks_by_artist):
        posmedium = lt.isPresent(mediums, i['Medium'])
        if posmedium <= 0: # Si no está el medio en la lista de medios
            lt.addLast(mediums, i['Medium'])
            lt.addLast(mediums_count, 1)
        else: # Si sí está el medio en la lista de medios
            lt.changeInfo(mediums_count, posmedium, lt.getElement(mediums_count, posmedium)+1)
    greatest=0
    pos_actual=0
    for cuenta_medium in lt.iterator(mediums_count):
        pos_actual+=1
        if cuenta_medium > greatest:
            greatest=cuenta_medium
            pos_most_used=pos_actual
    artworks_medium= lt.newList('ARRAY_LIST')        
    for obra in lt.iterator(artworks_by_artist):
        if obra['Medium']==lt.getElement(mediums,pos_most_used):
            lt.addLast(artworks_medium, obra)
    return artist,id_,artworks_by_artist,mediums,artworks_medium,pos_most_used

# Req. 4

def id_nation(catalog, ids):
    """
    retorna la nacion de un artista. O(n)
    """
    for i in lt.iterator(catalog['artists_BeginDate']):
        if int(i['ConstituentID'])==int(ids):
            artist = i["Nationality"]
            if artist=="" or artist=="Nationality unknown":
                artist="Unknown"
            break
    return artist

# Req. 5


def departament_artworks(catalog, department):
    """
    ObjectID de las obras de un departamento determinado. 
    Ya ordenadas por fecha.
    """
    artworks_by_department=lt.newList('ARRAY_LIST',key='ObjectID')
    for i in lt.iterator(catalog['artworks_Date']):
        if i['Department'] == department:
            lt.addLast(artworks_by_department, i)              
    return artworks_by_department,department


def convertMeters(medida):
    try:
        medida_metros = float(medida)
        medida_metros = medida_metros/100.
    except:
        medida_metros = False
    if medida_metros == 0:
        medida_metros = False
    return medida_metros


def calculatePrice(artwork):
    depth = convertMeters(artwork['Depth (cm)'])
    height = convertMeters(artwork['Height (cm)'])
    lenght = convertMeters(artwork['Length (cm)'])
    width = convertMeters(artwork['Width (cm)'])
    cirfunference = convertMeters(artwork['Circumference (cm)'])
    diameter = convertMeters(artwork['Diameter (cm)'])
    medidas_lineales=1
    price1 = 0
    price2 = 0
    for medida in [depth, height, lenght, width, cirfunference]:
        if type(medida) is float:
            medidas_lineales *= medida
            price1 = medidas_lineales*72.
    if type(diameter) is float:
        area = 3.141593 * (diameter/2)**2
        price2 = area*72.
    try:
        peso = float(obra['Weight (kg)'])
        price3 = peso*72.
    except:
        price3 = 0
    price = max([price1, price2, price3])
    if price == 0.:
        price = 48
    return price

    
def transport(catalog, department):
    artworks_by_department,department=departament_artworks(catalog, department)
    precios_obras=lt.newList('ARRAY_LIST')
    for obra in lt.iterator(artworks_by_department):
        precio_obra = calculatePrice(obra)
        lt.addLast(precios_obras,precio_obra)
    precio_final=0
    for precio in lt.iterator(precios_obras):
        precio_final+=precio
    peso = 0.
    return artworks_by_department,department,precios_obras,precio_final,peso


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

def compareArtworks_Artist(artist_id, artist):
    if artist_id == artist['artist']:
        return 0
    return -1
    
def compareArtworks_Date(artwork1,artwork2):
    """
    Por antiguedad. Deja las que no tienen fecha al final.
    """
    if artwork1["Date"]=="" or artwork2["Date"]=="":
        if artwork1["Date"]=="":
            return 0
        return -1
    elif artwork1["Date"]<=artwork2["Date"]:
        return -1
    return 0

def compareNationality(artist_id, artist):
    if artist_id == artist['nation']:
        return 0
    return -1

def compareNationality2(nation1, nation2):
    if lt.size(nation1["artworks"]) < lt.size(nation2["artworks"]):
        return -1
    return 0

# Funciones de ordenamiento

def sortArtists_BeginDate(catalog):
    sub_list = catalog["artists_BeginDate"].copy()
    start_time = time.process_time()
    sorted_list= mer.sort(sub_list, compareArtists_BeginDate)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list

def sortArtworks_DateAcquired(catalog):
    sub_list = catalog["artworks_DateAcquired"].copy()
    start_time = time.process_time()
    sorted_list= mer.sort(sub_list, compareArtworks_DateAcquired)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list

def sortArtworks_Date(catalog):
    sub_list = catalog["artworks_Date"].copy()
    start_time = time.process_time()
    sorted_list= mer.sort(sub_list, compareArtworks_Date)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list

def sortNationality(catalog):
    sub_list = catalog["nationality"].copy()
    start_time = time.process_time()
    sorted_list= mer.sort(sub_list, compareNationality2)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list