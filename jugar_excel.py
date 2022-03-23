import pandas as pd
from obtain_coord import extract_lat_long_via_address
import numpy as np

path = 'recursos/direccionesEB.xlsx'
df_datos = pd.read_excel(path)
#df_almacenes = pd.read_excel(path, sheet_name='Almacenes')

#Primero creamos la lista con las coordenadas y luego lo añadimos

#Primero las de billing
'''coord = []
for ind in df_datos.index:
    calle = df_datos['BILLINGSTREET'][ind]
    ciudad = df_datos['BILLINGCITY'][ind]
    if (isinstance(calle,float)):
        coord.append("")
    else:
        direccion = calle +", " +ciudad
        lat, long = extract_lat_long_via_address(direccion)
        coord.append(str(lat)+", " + str(long))
print(coord)'''

coord = []
for ind in df_datos.index:
    calle = df_datos['SHIPPINGSTREET'][ind]
    ciudad = df_datos['SHIPPINGCITY'][ind]
    if (isinstance(calle,float)):
        coord.append("")
    elif (calle == df_datos['BILLINGSTREET'][ind]):
        print("igual")
        coord.append(df_datos['Coord Billing'][ind])
    else:
        direccion = calle +", " +ciudad
        lat, long = extract_lat_long_via_address(direccion)
        coord.append(str(lat)+", " + str(long))
print(coord)

df_datos['Coord shipping'] = coord
df_datos.to_excel('direccionesEB_final.xlsx')
