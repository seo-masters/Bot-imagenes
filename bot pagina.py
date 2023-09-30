from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os


# Opciones del navegador Chrome
options = webdriver.ChromeOptions()
options.executable_path = r'C:\driver_chrome\chromedriver.exe'

# Ruta de la carpeta de imágenes
ruta_imagenes = r"C:\Users\USER\Desktop\imagenes a redimencionar"
archivos = os.listdir(ruta_imagenes)
# Obtener la lista de archivos en la carpeta
archivos = os.listdir(ruta_imagenes)

# Inicializar el controlador de Chrome fuera de las funciones
driver = webdriver.Chrome(options=options)
driver.get("https://www.iloveimg.com/resize-image")
driver.maximize_window()

def cargar_archivo(archivo):
    archivo_a_cargar = os.path.join(ruta_imagenes, archivo)
    # Aquí puedes realizar las operaciones que necesitas con el archivo cargado
    return archivo_a_cargar
def cargar_imagen(archivo_a_cargar):
    # Encontrar el campo de entrada de archivos y cargar la imagen
    try:
        file_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
        )
        file_input.send_keys(archivo_a_cargar)
    except Exception as e:
        print(f"Ocurrió un error al cargar la imagen: {e}")

def escalar_imagen():       
    # Escribir el valor "1200" en la casilla con id "pixels_width"
    try:
        width_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "pixels_width"))
        )
        width_input.clear()  # Limpiar cualquier valor existente en la casilla
        width_input.send_keys("1200")
    except Exception as e:
        print(f"Ocurrió un error al ingresar el valor en la casilla 'pixels_width': {e}")

def procesar_imagen():
    try:
        # Esperar a que el botón esté presente en la página
        boton = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "processTask"))
        )
        # Hacer clic en el botón
        boton.click()
        print("Se hizo clic en el botón con éxito.")
    except Exception as e:
        print(f"Ocurrió un error al hacer clic en el botón: {e}")

def cortar_imagen():
    try:
        continue_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//li[@data-title='Continue to Crop IMAGE']"))
        )
        continue_button.click()
        print("Se hizo clic en el botón 'Continue to Crop IMAGE' con éxito.")
    except Exception as e:
        print(f"Ocurrió un error al hacer clic en el botón 'Continue to Crop IMAGE': {e}")

def cambiar_ancho():
    try:
        # Esperar a que el campo de entrada de altura esté presente en la página
        ancho_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "dataWidth"))
        )
        ancho_input.clear()  # Limpiar cualquier valor existente en la casilla
        ancho_input.send_keys("1200")
        print("Se cambió el ancho (px) a 1200 con éxito.")
    except Exception as e:
        print(f"Ocurrió un error al cambiar el ancho (px): {e}")

def cambiar_altura():
    try:
        # Esperar a que el campo de entrada de altura esté presente en la página
        altura_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "dataHeight"))
        )
        
        # Utilizar JavaScript para cambiar el valor del campo directamente
        driver.execute_script("arguments[0].value = '628';", altura_input)
        
        print("Se cambió la altura (px) a 628 con éxito.")
    except Exception as e:
        print(f"Ocurrió un error al cambiar la altura (px): {e}")

def comprimir_imagen():
    try:
        comp_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//li[@data-title='Continue to Compress IMAGE']"))
        )
        comp_button.click()
        print("Se hizo clic en el botón 'Continue to Compress IMAGE' con éxito.")
    except Exception as e:
        print(f"Ocurrió un error al hacer clic en el botón 'Continue to Compress IMAGE': {e}")
def descargar_imagen(nombre_archivo):
    try:
        # Esperar a que el botón de descarga esté presente en la página
        download_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "pickfiles"))
        )
        # Hacer clic en el botón de descarga
        download_button.click()
        print(f"Se hizo clic en el botón de descarga para {nombre_archivo}.")
    except Exception as e:
        print(f"Ocurrió un error al hacer clic en el botón de descarga: {e}")

# Iterar sobre cada archivo en la carpeta
for archivo in archivos:
    archivo_a_cargar = cargar_archivo(archivo)
    nombre_archivo = os.path.basename(archivo_a_cargar)  # Obtener el nombre del archivo
    time.sleep(3)
    cargar_imagen(archivo_a_cargar)
    time.sleep(3)
    escalar_imagen()
    time.sleep(3)
    procesar_imagen()
    time.sleep(3)
    cortar_imagen()
    time.sleep(3)
    cambiar_altura()
    time.sleep(3)
    cambiar_ancho()
    time.sleep(3)
    procesar_imagen()
    time.sleep(3)
    comprimir_imagen()
    time.sleep(3)
    procesar_imagen()
    time.sleep(4)
    
    # Descargar la imagen redimensionada
    descargar_imagen(nombre_archivo)
    
    # Volver a la página inicial después de procesar una imagen
    driver.get("https://www.iloveimg.com/resize-image")
    time.sleep(4)

# Cerrar el navegador después de procesar todas las imágenes
driver.quit()