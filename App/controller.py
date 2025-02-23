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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de obras

def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos

def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadArtists(catalog)
    loadArtworks(catalog)
 
def loadArtists(catalog):
    """
    Carga los artistas desde el archivo CSV. 
    """
    artistsfile = cf.data_dir + 'MoMA/Artists-utf8-small.csv'
    input_file = csv.DictReader(open(artistsfile, encoding='utf-8'))
    for artist in input_file:
        model.addArtist(catalog, artist)

def loadArtworks(catalog):
    """
    Carga las obras de arte del archivo.
    """
    artworksfile = cf.data_dir + 'MoMA/Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(artworksfile, encoding='utf-8'))
    for artwork in input_file:
        model.addArtwork(catalog, artwork)

# Funciones de ordenamiento

def sortArtists_BeginDate(catalog):
    return model.sortArtists_BeginDate(catalog)

def sortArtworks_DateAcquired(catalog):
    return model.sortArtworks_DateAcquired(catalog)

def sortArtworks_Date(catalog):
    return model.sortArtworks_Date(catalog)

def sortNationality(catalog):
    return model.sortNationality(catalog)

# Funciones de consulta sobre el catálogo

def rangoArtists(catalog, anio1, anio2):
    return model.rangoArtists(catalog, anio1, anio2)

def rangoArtworks(catalog, fecha1, fecha2):
    return model.rangoArtworks(catalog, fecha1, fecha2)

def artist_medium(catalog,artist):
    return model.artist_medium(catalog,artist)

def artist_medium1(catalog,artist):
    return model.artist_medium1(catalog,artist)

def transport(catalog, department):
    return model.transport(catalog, department)

def id_artworks(catalog,author):
    return model.id_artworks(catalog, author)