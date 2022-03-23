import pandas as pd
import requests
import json
import googlemaps
from datetime import datetime
from obtain_time import extract_distance

path_data = 'recursos/direccionesEB_final.xlsx'
path_alm = 'recursos/direcciones de EB.xlsx'
df_datos = pd.read_excel(path_data)
df_almacenes = pd.read_excel(path_alm, sheet_name='Almacenes',header=None)

coord_alma = []
for i in range(4):
    coord_alma.append(df_almacenes[2][i])

#print(coord_alma)
bill = df_datos['Coord Billing'][0]
bill = bill.replace(" ","")
alma=coord_alma[0].replace(" ","")

distance = extract_distance(bill,alma)
print(distance)


#Lo que queda es correr esta api y guardar los datos en un excel nuevo y done

'''dist = []
for ind in df_datos.index:
    bill = df_datos['Coord Billing'][ind]
    bill = bill.replace(" ","")
    for alma in coord_alma:
        alma=alma.replace(" ","")
    break'''