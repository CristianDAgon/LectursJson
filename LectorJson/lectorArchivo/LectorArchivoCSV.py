import csv


"""
Definimos la clase correpondiente para la lectura de los archivos csv pasando como atributo
la ruta que necesitamos que lea
"""
class LectorArchivoCSV:
    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo

    def leer_archivo_csv(self):
        #Previamente comprombamod de que la ruta especificada si sea .csv
        if not self.ruta_archivo.endswith('.csv'):
            print('Error: El archivo seleccionado no es un archivo CSV.')
            return None
        #Creamos un diccionario el cual nos va a guardar todos los datos del archivo
        datos = []

        """
        Empezamos abriendo el archivo csv el cual ingreso por la ruta de modo lectura "r",
        por medio de la funcion csv.reader nos ayuda a procesar la informacion del documento linea por lina,
        utilizamos un ciclo for el cual va a recorrer cada linea generada y le va a dar su indentidicador a
        cada columna , utilizamos tambien strip() para limpiar la posicion de espacios y de caracteres especiales,
        agregamos cada uno de estos a nuestro diccionario datos y retornamos
        """
        with open(self.ruta_archivo, 'r', newline='') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            for fila in lector_csv:
                estudiante = {"id": fila[0].strip(), "nombre": fila[1].strip(), "apellido": fila[2].strip()}
                datos.append(estudiante)
        return datos