
import json


"""
Definimos la clase correpondiente a la lectura del acrchivo json, no retornamos nada
ya que explicitamente solo necesitamos convertit el archivo a formato json
"""
class EscritorArchivoJSON:
    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo


    """
    Iniciamos con abrir el archivo en modo lectura para poder hacer uso de este,
    utilizamos la codificacion utf-8 para evitar carcateres especiales, previamente utilizamos el
    ident en 4 segun algunos sitios para mejorar la lectura del archivo json, la variable enconder
    nos permite codifica el archivo de esta manera con los parametros mencionados,  y por ultimo la linea
    nos permite tomar los datos y los convierte en formato json con la configuracion de ident y caracteres especiales
    
    """
    def escribir_archivo_json(self, datos, indent=4):
        with open(self.ruta_archivo, 'w', encoding='utf-8') as archivo_json:

            encoder = json.JSONEncoder(indent=indent, ensure_ascii=False)

            archivo_json.write(encoder.encode(datos))