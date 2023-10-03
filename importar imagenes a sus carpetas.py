import os
import shutil
import time

def mover_archivos_entre_carpetas(ruta_origen, rutas_destino):
    indice_destino = 0
    # Inicializa el índice de destino en 0

    while True:
        ruta_destino_actual = rutas_destino[indice_destino]
        print(f"Cambiando a la ruta de destino: {ruta_destino_actual}")

        # Itera sobre los archivos en la carpeta de origen y muévelos a la ruta de destino actual
        for archivo in os.listdir(ruta_origen):
            ruta_archivo_origen = os.path.join(ruta_origen, archivo)

            # Verifica si el elemento en la ruta de origen es un archivo (no es una carpeta)
            if os.path.isfile(ruta_archivo_origen):
                try:
                    shutil.move(ruta_archivo_origen, os.path.join(ruta_destino_actual, archivo))
                    print(f"Archivo '{archivo}' movido a {ruta_destino_actual}")
                except Exception as e:
                    print(f"Error al mover el archivo '{archivo}' a {ruta_destino_actual}: {str(e)}")

        # Incrementa el índice de destino o vuelve al inicio si llega al final de la lista
        indice_destino = (indice_destino + 1) % len(rutas_destino)

# Ruta de la carpeta de origen que contiene los archivos que deseas mover
ruta_origen = r"C:\Users\USER\Desktop\imagenes procesadas"

# Lista de rutas de destino
rutas_destino = [
    r"C:\Users\USER\Downloads\bot imagenes\Salida de imagen\AMARRES CHICAGO\AMARRES DE AMOR",
    r"C:\Users\USER\Downloads\bot imagenes\Salida de imagen\AMARRES CHICAGO\SANTERIA"
]

# Llama a la función para ejecutar el proceso de movimiento de archivos
mover_archivos_entre_carpetas(ruta_origen, rutas_destino)
