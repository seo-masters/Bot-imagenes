import os
import requests
from APIpexels import PexelsAPI

# Lista de búsquedas y rutas de guardado
busquedas = [
    ['raton', 'comida'],
    ['gatos', 'perros'],
    ['reloj', 'campanas']
    # Agrega más búsquedas aquí si es necesario
]

rutas_imagenes = [
    r'C:/Users/USER/Desktop/Nueva carpeta2',
    r'C:/Users/USER/Desktop/Nueva carpeta',
    r'C:\Users\USER\Desktop\Nueva carpeta3'
]

def descargar_imagenes_pexels():
    api = PexelsAPI()
    numero_carpeta = 0
    while numero_carpeta < len(busquedas):
        palabras_clave = busquedas[numero_carpeta]

        # Verificar si la primera palabra clave está vacía
        if palabras_clave[0].strip() == "":
            print("La primera palabra clave está vacía. Saltando a la siguiente búsqueda.")
            numero_carpeta += 1
            continue

        success, data = api.search(" ".join(palabras_clave))

        if success:
            for photo in data['photos']:
                print("Descripción de la imagen:", photo['alt'])

                image_url = photo['src']['original']
                nombre_archivo = os.path.join(rutas_imagenes[numero_carpeta], os.path.basename(image_url))
                respuesta = requests.get(image_url)

                if respuesta.status_code == 200:
                    with open(nombre_archivo, 'wb') as archivo:
                        archivo.write(respuesta.content)
                    print(f"Imagen {nombre_archivo} descargada con éxito.")
                else:
                    print(f"No se pudo descargar la imagen desde {image_url}. Código de estado: {respuesta.status_code}")
            numero_carpeta += 1
        else:
            print("Error en la búsqueda.")
descargar_imagenes_pexels()