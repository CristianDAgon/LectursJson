from lectorArchivo.LectorArchivoCSV import LectorArchivoCSV
from lectorArchivo.EscritorArchivoJSON import EscritorArchivoJSON

import json

class Main:
    #Ingresamos la ruta en la cual tenemos nuestro archivo
    ruta_csv ="C:/Users/USER/Desktop/UNIVERSIDAD CRISTIAN/SEMESTRE 5/ING SOFTWARE 1/Tarea4ArchivosJson/Estudiantes.csv"

    #Es necesario crear la ruta del archivo json, por lo cual utilizamos replace
    ruta_json = ruta_csv.replace('.csv', '.json')

    #En esta variable instaciamos la clase LectorArchivosCSV con la ruta mencionada
    lector_csv = LectorArchivoCSV(ruta_csv)
    #En datos estara los datos gurdados del archivo por medio de nuestro metodo leer_Archivo_csv
    datos_csv = lector_csv.leer_archivo_csv()

    #Instaciamos la clase Escritor con nuestra ruta json anteriormente creada
    escritor_json = EscritorArchivoJSON(ruta_json)
    #Por ultimo en esa ruta de nuestro archivo convertimos nuestros datos a formato json
    escritor_json.escribir_archivo_json(datos_csv)

    print(f"Se ha creado el archivo JSON: {ruta_json}")




Main()