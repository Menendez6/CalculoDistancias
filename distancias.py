import pandas as pd
import requests
import json
import googlemaps
from datetime import datetime
from obtain_time import extract_distance

path_data = 'recursos/direccionesEB_final1.xlsx'
path_alm = 'recursos/direcciones de EB.xlsx'
df_datos = pd.read_excel(path_data)
df_almacenes = pd.read_excel(path_alm, sheet_name='Almacenes',header=None)

coord_alma = {}
sitios = ["Alcala","Sanfer","Alcorcon","Merca"]
for i in range(4):
    coord_alma[sitios[i]] = df_almacenes[2][i]

#print(coord_alma)


#Lo que queda es correr esta api y guardar los datos en un excel nuevo y done
#Lo que interesa es la coordenada de shipping imagino

dist = {"Alcala":[],"Sanfer":[],"Alcorcon":[],"Merca":[]}
dist_bill = {"Alcala":df_datos['Distancia Alcala'],"Sanfer":df_datos['Distancia SF'],"Alcorcon":df_datos['Distancia Alcorcón'],"Merca":df_datos['Distancia MercaMadrid']}
for ind in df_datos.index:
    bill = df_datos['Coord Billing'][ind]
    ship = df_datos['Coord shipping'][ind]
    if (isinstance(ship,float) or isinstance(bill,float)):
        for sitio in sitios:
            dist[sitio].append("")
    elif bill.replace(" ","") == ship.replace(" ",""):
        print("igual")
        for sitio in sitios:
            dist[sitio].append(dist_bill[sitio][ind])
    else:
        ship = ship.replace(" ","")
        for sitio in sitios:
            tiempo = extract_distance(ship,coord_alma[sitio])
            dist[sitio].append(tiempo)

df_datos['Distancia Alcala'] = dist["Alcala"]
df_datos['Distancia SF'] = dist["Sanfer"]
df_datos['Distancia Alcorcón'] = dist["Alcorcon"]
df_datos['Distancia MercaMadrid'] = dist["Merca"]
df_datos.to_excel('direccionesEB_final2.xlsx')

