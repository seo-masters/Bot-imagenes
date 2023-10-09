import os
import requests

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

def descargar_imagenes_pixabay(cantidad_por_busqueda=5):
    api_key = "39882178-93a7eee8f4fa8bb659ed1f39a"  # Reemplaza con tu clave de API de Pixabay
    numero_carpeta = 0
    while numero_carpeta < len(busquedas):
        palabras_clave = busquedas[numero_carpeta]

        # Verificar si la primera palabra clave está vacía
        if palabras_clave[0].strip() == "":
            print("La primera palabra clave está vacía. Saltando a la siguiente búsqueda.")
            numero_carpeta += 1
            continue

        cantidad_descargar = cantidad_por_busqueda
        pagina = 1
        while cantidad_descargar > 0:
            url = f"https://pixabay.com/api/?key={api_key}&q={'+'.join(palabras_clave)}&per_page=200&page={pagina}"
            response = requests.get(url)
            data = response.json()

            if "hits" in data:
                hits = data["hits"]
                for i, imagen in enumerate(hits):
                    if cantidad_descargar <= 0:
                        break

                    imagen_url = imagen["largeImageURL"]
                    response = requests.get(imagen_url)

                    if response.status_code == 200:
                        # Guardar la imagen en la carpeta de descargas
                        with open(os.path.join(rutas_imagenes[numero_carpeta], f"imagen_{i+1}.jpg"), "wb") as file:
                            file.write(response.content)
                        cantidad_descargar -= 1

                pagina += 1
            else:
                print("Error en la respuesta de Pixabay API.")
                break

        numero_carpeta += 1

# Llama a la función para descargar imágenes de Pixabay
cantidad_por_busqueda = 10  # Puedes ajustar esta cantidad según tus necesidades
descargar_imagenes_pixabay(cantidad_por_busqueda)
