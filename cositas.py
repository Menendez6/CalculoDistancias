from obtain_time import extract_distance
import pandas as pd

path_alm = 'recursos/direcciones de EB.xlsx'

df_almacenes = pd.read_excel(path_alm, sheet_name='Almacenes',header=None)

coord_alma = {}
sitios = ["Alcala","Sanfer","Alcorcon","Merca"]
for i in range(4):
    coord_alma[sitios[i]] = df_almacenes[2][i]
for sitio in sitios:
    print(extract_distance("40.344423,-3.815670",coord_alma[sitio]))