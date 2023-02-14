print("FERNANDO DAVID CONTRERAS MORAN, CARNÉ 1631023, INTRODUCCIÓN A LA INGENIERIA EN INFORMÁTICA Y SISTEMAS")

import os

mi_ubicacion = os.getcwd()
if os.path.exists("modulos"):
    print("La carpeta ya existe")
else:
    os.mkdir(mi_ubicacion + "\\modulos")
    archivo = open('./modulos/prueba.txt','w')
    archivo.write('Hola mundo')
    archivo.close()