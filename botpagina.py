from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import shutil
import subprocess
exiftool_path = "./exiftool.exe"

ruta_origen = r"C:\Carpeta entrada y salida\imagenes procesadas"
chrome_options = webdriver.ChromeOptions()
chrome_options.executable_path = r'C:\driver_chrome\chromedriver.exe'
# Configurar la ruta de descargas
prefs = {"download.default_directory": ruta_origen}
chrome_options.add_experimental_option("prefs", prefs)
# Iniciar el navegador con las opciones configuradas
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.iloveimg.com/resize-image")
driver.maximize_window()

# Lista de metadatos a procesar
metadata_list = [
    {
        'ruta': r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA AMARRES DE AMOR",
        'descripcion': 'Nueva Descripción 1',
        'titulo': 'Nuevo Título 1',
        'etiquetas': 'Nueva Etiqueta1, Nueva Etiqueta2',
        'latitud': '100',
        'longitud': '233'
    },
    {
        'ruta': r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA DEL AMOR",
        'descripcion': 'Nueva Descripción 2',
        'titulo': 'Nuevo Título 2',
        'etiquetas': 'Otra Etiqueta1, Otra Etiqueta2',
        'latitud': '200',
        'longitud': '300'
    },
    {
        'ruta': r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA INDIO AMAZONICO",
        'descripcion': 'Nueva Descripción 1',
        'titulo': 'Nuevo Título 1',
        'etiquetas': 'Nueva Etiqueta1, Nueva Etiqueta2',
        'latitud': '100',
        'longitud': '233'
    },
    {
        'ruta': r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA MAESTROS ESPIRITUALES",
        'descripcion': 'Nueva Descripción 2',
        'titulo': 'Nuevo Título 2',
        'etiquetas': 'Otra Etiqueta1, Otra Etiqueta2',
        'latitud': '200',
        'longitud': '300'
    },
    {
        'ruta': r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA AMARRES DE AMOR",
        'descripcion': 'Nueva Descripción 1',
        'titulo': 'Nuevo Título 1',
        'etiquetas': 'Nueva Etiqueta1, Nueva Etiqueta2',
        'latitud': '100',
        'longitud': '233'
    },
    {
        'ruta': r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA SECRETO AZTECA",
        'descripcion': 'Nueva Descripción 2',
        'titulo': 'Nuevo Título 2',
        'etiquetas': 'Otra Etiqueta1, Otra Etiqueta2',
        'latitud': '200',
        'longitud': '300'
    },
    {
        'ruta': r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA VIRGEN MORENA",
        'descripcion': 'Nueva Descripción 1',
        'titulo': 'Nuevo Título 1',
        'etiquetas': 'Nueva Etiqueta1, Nueva Etiqueta2',
        'latitud': '100',
        'longitud': '233'
    },
    {
        'ruta': r"C:\Carpeta entrada y salida\Salida de imagen\CASH DEALS TODAY",
        'descripcion': 'Nueva Descripción 2',
        'titulo': 'Nuevo Título 2',
        'etiquetas': 'Otra Etiqueta1, Otra Etiqueta2',
        'latitud': '200',
        'longitud': '300'
    },
    {
        'ruta': r"C:\Carpeta entrada y salida\Salida de imagen\ELITE CHICAGO SPA",
        'descripcion': 'Nueva Descripción 1',
        'titulo': 'Nuevo Título 1',
        'etiquetas': 'Nueva Etiqueta1, Nueva Etiqueta2',
        'latitud': '100',
        'longitud': '233'
    },
    {
        'ruta': r"C:\Carpeta entrada y salida\Salida de imagen\ELITE FRENCHIES",
        'descripcion': 'Nueva Descripción 2',
        'titulo': 'Nuevo Título 2',
        'etiquetas': 'Otra Etiqueta1, Otra Etiqueta2',
        'latitud': '200',
        'longitud': '300'
    },
    {
        'ruta': r"C:\Carpeta entrada y salida\Salida de imagen\EXPRESS CLEAN",
        'descripcion': 'Nueva Descripción 1',
        'titulo': 'Nuevo Título 1',
        'etiquetas': 'Nueva Etiqueta1, Nueva Etiqueta2',
        'latitud': '100',
        'longitud': '233'
    },
    {
        'ruta': r"C:\Carpeta entrada y salida\Salida de imagen\LOPEZ Y LOPEZ ABOGADOS",
        'descripcion': 'Nueva Descripción 2',
        'titulo': 'Nuevo Título 2',
        'etiquetas': 'Otra Etiqueta1, Otra Etiqueta2',
        'latitud': '200',
        'longitud': '300'
    },
    {
        'ruta': r"C:\Carpeta entrada y salida\Salida de imagen\OSCEOLA",
        'descripcion': 'Nueva Descripción 2',
        'titulo': 'Nuevo Título 2',
        'etiquetas': 'Otra Etiqueta1, Otra Etiqueta2',
        'latitud': '200',
        'longitud': '300'
    },
    {
        'ruta': r"C:\Carpeta entrada y salida\Salida de imagen\QUICK CLEANING",
        'descripcion': 'Nueva Descripción 2',
        'titulo': 'Nuevo Título 2',
        'etiquetas': 'Otra Etiqueta1, Otra Etiqueta2',
        'latitud': '200',
        'longitud': '300'
    }
]
# Lista de rutas de destino
rutas_destino = [    
    # Botanica amarres de amor
    r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA AMARRES DE AMOR\AMARRES DE AMOR",
    r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA AMARRES DE AMOR\AMULETOS PREPARADOS",
    r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA AMARRES DE AMOR\CURACIONES ESPIRITUALES",
    r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA AMARRES DE AMOR\ENDULZAMIENTOS DE AMOR",
    r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA AMARRES DE AMOR\HIERBAS ESOTERICAS",
    r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA AMARRES DE AMOR\LECTURA DE CARTAS",
    r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA AMARRES DE AMOR\LIMPIEZAS ESPIRITUALES",
    r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA AMARRES DE AMOR\SANTERIA",
    # Botanica del amor
    r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA DEL AMOR\AMARRES DE AMOR",
    r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA DEL AMOR\AMULETOS PREPARADOS",
    r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA DEL AMOR\CENTRO ESPIRITUAL",
    r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA DEL AMOR\CURACIONES ESPIRITUALES",
    r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA DEL AMOR\ENDULZAMIENTOS DE AMOR",
    r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA DEL AMOR\LECTURA DE CARTAS",
    r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA DEL AMOR\LECTURA DEL TAROT",
    r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA DEL AMOR\LIMPIEZAS ESPIRITUALES",
    r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA DEL AMOR\TIENDA ESOTERICA",
    # Botanica indio amazonico
    r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA INDIO AMAZONICO\AMARRES DE AMOR",
    r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA INDIO AMAZONICO\AMULETOS PREPARADOS",
    r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA INDIO AMAZONICO\CENTRO ESPIRITUAL",
    r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA INDIO AMAZONICO\CURACIONES ESPIRITUALES",
    r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA INDIO AMAZONICO\ENDULZAMIENTOS DE AMOR",
    r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA INDIO AMAZONICO\HIERBAS ESOTERICAS",
    r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA INDIO AMAZONICO\LECTURA DE CARTAS",
    r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA INDIO AMAZONICO\LIMPIEZAS ESPIRITUALES",
    r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA INDIO AMAZONICO\SANTERIA",
    # Botanica maestros espirituales
    r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA MAESTROS ESPIRITUALES\AMARRES DE AMOR",
    r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA MAESTROS ESPIRITUALES\AMULETOS PREPARADOS",
    r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA MAESTROS ESPIRITUALES\CENTRO ESPIRITUAL",
    r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA MAESTROS ESPIRITUALES\CURACIONES ESPIRITUALES",
    r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA MAESTROS ESPIRITUALES\ENDULZAMIENTOS DE AMOR",
    r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA MAESTROS ESPIRITUALES\LECTURA DE CARTAS",
    r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA MAESTROS ESPIRITUALES\LIMPIEZAS ESPIRITUALES",
    r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA MAESTROS ESPIRITUALES\TIENDA ESOTERICA",
    # Botanica secreto azteca
    r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA SECRETO AZTECA\AMARRES DE AMOR",
    r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA SECRETO AZTECA\AMULETOS PREPARADOS",
    r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA SECRETO AZTECA\CENTRO ESPIRITUAL",
    r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA SECRETO AZTECA\CURACIONES ESPIRITUALES",
    r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA SECRETO AZTECA\ENDULZAMIENTOS DE AMOR",
    r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA SECRETO AZTECA\LECTURA DEL TAROT",
    r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA SECRETO AZTECA\LIMPIEZAS ESPIRITUALES",
    r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA SECRETO AZTECA\SANTERIA",
    r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA SECRETO AZTECA\TIENDA ESOTERICA",
    # Botanica virgen morena
    r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA VIRGEN MORENA\AMARRES DE AMOR",
    r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA VIRGEN MORENA\AMULETOS PREPARADOS",
    r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA VIRGEN MORENA\BRUJOS",
    r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA VIRGEN MORENA\CURACIONES ESPIRITUALES",
    r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA VIRGEN MORENA\ENDULZAMIENTOS DE AMOR",
    r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA VIRGEN MORENA\LECTURA DE CARTAS",
    r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA VIRGEN MORENA\LIMPIEZAS ESPIRITUALES",
    r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA VIRGEN MORENA\SANTERIA",
    r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA VIRGEN MORENA\TIENDA ESOTERICA",
    # Cash deals today
    r"C:\Carpeta entrada y salida\Salida de imagen\CASH DEALS TODAY\BUYING A HOME WITHOUT FINANCING HOW TO DO IT",
    r"C:\Carpeta entrada y salida\Salida de imagen\CASH DEALS TODAY\BUYING HOMES NO MORTGAGE, CASH ONLY",
    r"C:\Carpeta entrada y salida\Salida de imagen\CASH DEALS TODAY\BUYING HOMES THE POWER OF DIRECT PAYMENT",
    r"C:\Carpeta entrada y salida\Salida de imagen\CASH DEALS TODAY\BUYING IN CASH AN EASY PATH TO HOUSING",
    r"C:\Carpeta entrada y salida\Salida de imagen\CASH DEALS TODAY\BUYING YOUR HOME THE FORMULA FOR SUCCESS IS CASH",
    r"C:\Carpeta entrada y salida\Salida de imagen\CASH DEALS TODAY\CASH AND PROPERTY YOUR FUTURE HOME WITHIN REACH",
    r"C:\Carpeta entrada y salida\Salida de imagen\CASH DEALS TODAY\CASH IN HAND, HOME OWNERSHIP HOW",
    r"C:\Carpeta entrada y salida\Salida de imagen\CASH DEALS TODAY\LIQUID MONEY! BUY YOUR HOUSE RIGHT NOW",
    r"C:\Carpeta entrada y salida\Salida de imagen\CASH DEALS TODAY\NO FINANCING YOUR GUIDE TO BUYING A HOME FOR CASH",
    r"C:\Carpeta entrada y salida\Salida de imagen\CASH DEALS TODAY\QUICK BUY CASH HOMES IN THE SPOTLIGHT",
    r"C:\Carpeta entrada y salida\Salida de imagen\CASH DEALS TODAY\YOUR HOME, YOUR MONEY BUY CASH TODAY",
    r"C:\Carpeta entrada y salida\Salida de imagen\CASH DEALS TODAY\YOUR OWN HOME CASH ON DELIVERY, NO WAITING",
    # Elite chicago spa- facial
    r"C:\Carpeta entrada y salida\Salida de imagen\ELITE CHICAGO SPA\ELITE CHICAGO SPA - FACIAL\BOTOX CHICAGO",
    r"C:\Carpeta entrada y salida\Salida de imagen\ELITE CHICAGO SPA\ELITE CHICAGO SPA - FACIAL\DERMAL FILLERS",
    r"C:\Carpeta entrada y salida\Salida de imagen\ELITE CHICAGO SPA\ELITE CHICAGO SPA - FACIAL\DERMAPLANING CHICAGO",
    r"C:\Carpeta entrada y salida\Salida de imagen\ELITE CHICAGO SPA\ELITE CHICAGO SPA - FACIAL\FRACTIONAL RADIO FRECUENCY",
    r"C:\Carpeta entrada y salida\Salida de imagen\ELITE CHICAGO SPA\ELITE CHICAGO SPA - FACIAL\GLOW FACIAL",
    r"C:\Carpeta entrada y salida\Salida de imagen\ELITE CHICAGO SPA\ELITE CHICAGO SPA - FACIAL\MICRODERMABRASION",
    r"C:\Carpeta entrada y salida\Salida de imagen\ELITE CHICAGO SPA\ELITE CHICAGO SPA - FACIAL\MICRONEEDLING",
    r"C:\Carpeta entrada y salida\Salida de imagen\ELITE CHICAGO SPA\ELITE CHICAGO SPA - FACIAL\PRP (PLATELET RICH PLASMA)",
    r"C:\Carpeta entrada y salida\Salida de imagen\ELITE CHICAGO SPA\ELITE CHICAGO SPA - FACIAL\SISTEM CELL PRP",
    r"C:\Carpeta entrada y salida\Salida de imagen\ELITE CHICAGO SPA\ELITE CHICAGO SPA - FACIAL\THREAD LIFT",
    # Elite chicago spa- grasa
    r"C:\Carpeta entrada y salida\Salida de imagen\ELITE CHICAGO SPA\ELITE CHICAGO SPA - GRASA\CARBOXITERAPY",
    r"C:\Carpeta entrada y salida\Salida de imagen\ELITE CHICAGO SPA\ELITE CHICAGO SPA - GRASA\CELLULITE REMOVAL",
    r"C:\Carpeta entrada y salida\Salida de imagen\ELITE CHICAGO SPA\ELITE CHICAGO SPA - GRASA\COOL SCULPTING",
    r"C:\Carpeta entrada y salida\Salida de imagen\ELITE CHICAGO SPA\ELITE CHICAGO SPA - GRASA\DOUBLE CHIN REDUCTION",
    r"C:\Carpeta entrada y salida\Salida de imagen\ELITE CHICAGO SPA\ELITE CHICAGO SPA - GRASA\LAKEVIEW MASSAGE SPA",
    r"C:\Carpeta entrada y salida\Salida de imagen\ELITE CHICAGO SPA\ELITE CHICAGO SPA - GRASA\LASER HAIR REMOVAL",
    r"C:\Carpeta entrada y salida\Salida de imagen\ELITE CHICAGO SPA\ELITE CHICAGO SPA - GRASA\LIP FILLERS CHICAGO",
    r"C:\Carpeta entrada y salida\Salida de imagen\ELITE CHICAGO SPA\ELITE CHICAGO SPA - GRASA\LIPO LASER",
    r"C:\Carpeta entrada y salida\Salida de imagen\ELITE CHICAGO SPA\ELITE CHICAGO SPA - GRASA\ULTRA SONIC CAVITATION",
    # Elite frenchies
    r"C:\Carpeta entrada y salida\Salida de imagen\ELITE FRENCHIES\CARE OF A FRENCH BULLDOG",
    r"C:\Carpeta entrada y salida\Salida de imagen\ELITE FRENCHIES\FRENCH BULLDOG - CHARACTER AND CHARACTERISTICS",
    r"C:\Carpeta entrada y salida\Salida de imagen\ELITE FRENCHIES\FRENCH BULLDOG BREEDERS",
    r"C:\Carpeta entrada y salida\Salida de imagen\ELITE FRENCHIES\FRENCH BULLDOG BREEDING",
    r"C:\Carpeta entrada y salida\Salida de imagen\ELITE FRENCHIES\FRENCH BULLDOG GESTATION, PREGNANCY AND CARE",
    r"C:\Carpeta entrada y salida\Salida de imagen\ELITE FRENCHIES\FRENCH BULLDOG STUD",
    r"C:\Carpeta entrada y salida\Salida de imagen\ELITE FRENCHIES\FRENCH BULLDOG, ONE OF THE WORLD´S BEST COMPANION DOGS",
    r"C:\Carpeta entrada y salida\Salida de imagen\ELITE FRENCHIES\FRENCH BULLDOGS CHARACTERISTICS AND PERSONALITY",
    r"C:\Carpeta entrada y salida\Salida de imagen\ELITE FRENCHIES\KEY ASPECTS TO TAKE GOOD CARE OF A FRENCH BULLDOG",
    r"C:\Carpeta entrada y salida\Salida de imagen\ELITE FRENCHIES\KNOW THE TEMPERAMENT OF THE FRENCH BULLDOG",
    r"C:\Carpeta entrada y salida\Salida de imagen\ELITE FRENCHIES\RARE COLORS IN FRENCH BULLDOGS",
    r"C:\Carpeta entrada y salida\Salida de imagen\ELITE FRENCHIES\THE BULLDOG, THE DOG BREED THAT WILL CONQUER YOUR HEART",
    # Express clean - comercial
    r"C:\Carpeta entrada y salida\Salida de imagen\EXPRESS CLEAN\EXPRESS CLEAN - COMERCIAL\CLEANING SERVICES",
    r"C:\Carpeta entrada y salida\Salida de imagen\EXPRESS CLEAN\EXPRESS CLEAN - COMERCIAL\COMERCIAL CLEANING SERVICES",
    r"C:\Carpeta entrada y salida\Salida de imagen\EXPRESS CLEAN\EXPRESS CLEAN - COMERCIAL\EVENT CLEANING",
    r"C:\Carpeta entrada y salida\Salida de imagen\EXPRESS CLEAN\EXPRESS CLEAN - COMERCIAL\OFFICE CLEANING",
    r"C:\Carpeta entrada y salida\Salida de imagen\EXPRESS CLEAN\EXPRESS CLEAN - COMERCIAL\RESTAURANT CLEANING SERVICES",
    # Express clean - residencial
    r"C:\Carpeta entrada y salida\Salida de imagen\EXPRESS CLEAN\EXPRESS CLEAN - RESIDENCIAL\AIRBNB CLEANING",
    r"C:\Carpeta entrada y salida\Salida de imagen\EXPRESS CLEAN\EXPRESS CLEAN - RESIDENCIAL\APARTAMENT CLEANING",
    r"C:\Carpeta entrada y salida\Salida de imagen\EXPRESS CLEAN\EXPRESS CLEAN - RESIDENCIAL\CLEANING SERVICES",
    r"C:\Carpeta entrada y salida\Salida de imagen\EXPRESS CLEAN\EXPRESS CLEAN - RESIDENCIAL\DAME DAY CLEANING",
    r"C:\Carpeta entrada y salida\Salida de imagen\EXPRESS CLEAN\EXPRESS CLEAN - RESIDENCIAL\HOUSE CLEANING",
    r"C:\Carpeta entrada y salida\Salida de imagen\EXPRESS CLEAN\EXPRESS CLEAN - RESIDENCIAL\MAID CLEANING SERVICES",
    r"C:\Carpeta entrada y salida\Salida de imagen\EXPRESS CLEAN\EXPRESS CLEAN - RESIDENCIAL\MAID SERVICE SKOKIE IL",
    r"C:\Carpeta entrada y salida\Salida de imagen\EXPRESS CLEAN\EXPRESS CLEAN - RESIDENCIAL\MAID SERVICES",
    r"C:\Carpeta entrada y salida\Salida de imagen\EXPRESS CLEAN\EXPRESS CLEAN - RESIDENCIAL\MOVE OUT CLEANING",
    r"C:\Carpeta entrada y salida\Salida de imagen\EXPRESS CLEAN\EXPRESS CLEAN - RESIDENCIAL\SAME DAY CLEANING",
    # Lopez y Lopez abogados
    r"C:\Carpeta entrada y salida\Salida de imagen\LOPEZ Y LOPEZ ABOGADOS\ABOGADOS EN BOSA",
    r"C:\Carpeta entrada y salida\Salida de imagen\LOPEZ Y LOPEZ ABOGADOS\ABOGADOS EN CALI",
    r"C:\Carpeta entrada y salida\Salida de imagen\LOPEZ Y LOPEZ ABOGADOS\ABOGADOS EN CARTAGENA",
    r"C:\Carpeta entrada y salida\Salida de imagen\LOPEZ Y LOPEZ ABOGADOS\ABOGADOS EN CUCUTA",
    r"C:\Carpeta entrada y salida\Salida de imagen\LOPEZ Y LOPEZ ABOGADOS\ABOGADOS EN DERECHO ADMINISTRATIVO",
    r"C:\Carpeta entrada y salida\Salida de imagen\LOPEZ Y LOPEZ ABOGADOS\ABOGADOS EN ENGATIVA",
    r"C:\Carpeta entrada y salida\Salida de imagen\LOPEZ Y LOPEZ ABOGADOS\ABOGADOS EN KENNEDY",
    r"C:\Carpeta entrada y salida\Salida de imagen\LOPEZ Y LOPEZ ABOGADOS\ABOGADOS EN SANTA MARTA",
    r"C:\Carpeta entrada y salida\Salida de imagen\LOPEZ Y LOPEZ ABOGADOS\ABOGADOS EN USME",
    r"C:\Carpeta entrada y salida\Salida de imagen\LOPEZ Y LOPEZ ABOGADOS\ABOGADOS PENALISTAS BOGOTA",
    r"C:\Carpeta entrada y salida\Salida de imagen\LOPEZ Y LOPEZ ABOGADOS\DERECHO DE FAMILIA",
    # Oceola - comercial
    r"C:\Carpeta entrada y salida\Salida de imagen\OSCEOLA\OSCEOLA - COMERCIAL\CHAIN LINK FENCE",
    r"C:\Carpeta entrada y salida\Salida de imagen\OSCEOLA\OSCEOLA - COMERCIAL\CHICAGO STEEL FENCE",
    r"C:\Carpeta entrada y salida\Salida de imagen\OSCEOLA\OSCEOLA - COMERCIAL\COMMERCIAL FENCE INSTALLATION",
    r"C:\Carpeta entrada y salida\Salida de imagen\OSCEOLA\OSCEOLA - COMERCIAL\INDUSTRIAL FENCE COMPANY",
    r"C:\Carpeta entrada y salida\Salida de imagen\OSCEOLA\OSCEOLA - COMERCIAL\IRON BOLLARDS INSTALLATION",
    r"C:\Carpeta entrada y salida\Salida de imagen\OSCEOLA\OSCEOLA - COMERCIAL\IRON FENCE INDUSTRIAL",
    r"C:\Carpeta entrada y salida\Salida de imagen\OSCEOLA\OSCEOLA - COMERCIAL\VINYL FENCE",
    r"C:\Carpeta entrada y salida\Salida de imagen\OSCEOLA\OSCEOLA - COMERCIAL\WOOD FENCE",
    r"C:\Carpeta entrada y salida\Salida de imagen\OSCEOLA\OSCEOLA - COMERCIAL\WROUGHT IRON STAIRCASES",
    # Oceola - residencial
    r"C:\Carpeta entrada y salida\Salida de imagen\OSCEOLA\OSCEOLA - RESIDENCIAL\AUTOMATIC GATE",
    r"C:\Carpeta entrada y salida\Salida de imagen\OSCEOLA\OSCEOLA - RESIDENCIAL\CHAIN LINK FENCE",
    r"C:\Carpeta entrada y salida\Salida de imagen\OSCEOLA\OSCEOLA - RESIDENCIAL\COMPOSITE FENCE",
    r"C:\Carpeta entrada y salida\Salida de imagen\OSCEOLA\OSCEOLA - RESIDENCIAL\CUSTOM WROUGHT IRON RAILINGS",
    r"C:\Carpeta entrada y salida\Salida de imagen\OSCEOLA\OSCEOLA - RESIDENCIAL\FENCE COMPANY WINNETKA",
    r"C:\Carpeta entrada y salida\Salida de imagen\OSCEOLA\OSCEOLA - RESIDENCIAL\FIRE SCAPES CHICAGO",
    r"C:\Carpeta entrada y salida\Salida de imagen\OSCEOLA\OSCEOLA - RESIDENCIAL\IRON FENCE",
    r"C:\Carpeta entrada y salida\Salida de imagen\OSCEOLA\OSCEOLA - RESIDENCIAL\RESIDENTIAL ALUMINUM FENCES",
    r"C:\Carpeta entrada y salida\Salida de imagen\OSCEOLA\OSCEOLA - RESIDENCIAL\SECURITY CAMERAS SYSTEMS",
    r"C:\Carpeta entrada y salida\Salida de imagen\OSCEOLA\OSCEOLA - RESIDENCIAL\VINYL FENCE",
    r"C:\Carpeta entrada y salida\Salida de imagen\OSCEOLA\OSCEOLA - RESIDENCIAL\WOOD FENCE",
    r"C:\Carpeta entrada y salida\Salida de imagen\OSCEOLA\OSCEOLA - RESIDENCIAL\WROUGHT IRON BALCONY RAILING",
    # Quick cleaning - comercial
    r"C:\Carpeta entrada y salida\Salida de imagen\QUICK CLEANING\QUICK CLEANING - COMERCIAL\CLEANING SERVICES",
    r"C:\Carpeta entrada y salida\Salida de imagen\QUICK CLEANING\QUICK CLEANING - COMERCIAL\CLEANING SERVICES LOGAN SQUARE",
    r"C:\Carpeta entrada y salida\Salida de imagen\QUICK CLEANING\QUICK CLEANING - COMERCIAL\COMMERCIAL CLEANING",
    r"C:\Carpeta entrada y salida\Salida de imagen\QUICK CLEANING\QUICK CLEANING - COMERCIAL\DAYCARE CLEANING",
    r"C:\Carpeta entrada y salida\Salida de imagen\QUICK CLEANING\QUICK CLEANING - COMERCIAL\DENTAL OFFICE CLEANING",
    r"C:\Carpeta entrada y salida\Salida de imagen\QUICK CLEANING\QUICK CLEANING - COMERCIAL\EVENT CLEANING",
    r"C:\Carpeta entrada y salida\Salida de imagen\QUICK CLEANING\QUICK CLEANING - COMERCIAL\GYM CLEANING",
    r"C:\Carpeta entrada y salida\Salida de imagen\QUICK CLEANING\QUICK CLEANING - COMERCIAL\OFFICE CLEANING",
    r"C:\Carpeta entrada y salida\Salida de imagen\QUICK CLEANING\QUICK CLEANING - COMERCIAL\RESTAURANT CLEANING SERVICES",
    # Quick cleaning - residencial
    r"C:\Carpeta entrada y salida\Salida de imagen\QUICK CLEANING\QUICK CLEANING - RESIDENCIAL\AIRBNB CLEANING",
    r"C:\Carpeta entrada y salida\Salida de imagen\QUICK CLEANING\QUICK CLEANING - RESIDENCIAL\APARTAMENT CLEANING",
    r"C:\Carpeta entrada y salida\Salida de imagen\QUICK CLEANING\QUICK CLEANING - RESIDENCIAL\DEEP CLEANING SERVICES",
    r"C:\Carpeta entrada y salida\Salida de imagen\QUICK CLEANING\QUICK CLEANING - RESIDENCIAL\HOUSE CLEANING",
    r"C:\Carpeta entrada y salida\Salida de imagen\QUICK CLEANING\QUICK CLEANING - RESIDENCIAL\MAID CLEANING SERVICES",
    r"C:\Carpeta entrada y salida\Salida de imagen\QUICK CLEANING\QUICK CLEANING - RESIDENCIAL\MAID SERVICES",
    r"C:\Carpeta entrada y salida\Salida de imagen\QUICK CLEANING\QUICK CLEANING - RESIDENCIAL\MOVE OUT CLEANING",
    r"C:\Carpeta entrada y salida\Salida de imagen\QUICK CLEANING\QUICK CLEANING - RESIDENCIAL\POST CONSTRUCTION CLEANING",
    r"C:\Carpeta entrada y salida\Salida de imagen\QUICK CLEANING\QUICK CLEANING - RESIDENCIAL\RENTAL PROPERTY CLEANING SERVICES"

]
# Lista de rutas de carpetas de imágenes a procesar
rutas_imagenes = [
    # Botanica amarres de amor
    r"C:\Carpeta entrada y salida\Entrada de imagenes\BOTANICA AMARRES DE AMOR\AMARRES DE AMOR",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\BOTANICA AMARRES DE AMOR\AMULETOS PREPARADOS",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\BOTANICA AMARRES DE AMOR\CURACIONES ESPIRITUALES",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\BOTANICA AMARRES DE AMOR\ENDULZAMIENTOS DE AMOR",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\BOTANICA AMARRES DE AMOR\HIERBAS ESOTERICAS",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\BOTANICA AMARRES DE AMOR\LECTURA DE CARTAS",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\BOTANICA AMARRES DE AMOR\LIMPIEZAS ESPIRITUALES",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\BOTANICA AMARRES DE AMOR\SANTERIA",
    # Botanica del amor
    r"C:\Carpeta entrada y salida\Entrada de imagenes\BOTANICA DEL AMOR\AMARRES DE AMOR",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\BOTANICA DEL AMOR\AMULETOS PREPARADOS",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\BOTANICA DEL AMOR\CENTRO ESPIRITUAL",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\BOTANICA DEL AMOR\CURACIONES ESPIRITUALES",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\BOTANICA DEL AMOR\ENDULZAMIENTOS DE AMOR",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\BOTANICA DEL AMOR\LECTURA DE CARTAS",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\BOTANICA DEL AMOR\LECTURA DEL TAROT",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\BOTANICA DEL AMOR\LIMPIEZAS ESPIRITUALES",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\BOTANICA DEL AMOR\TIENDA ESOTERICA",
    # Botanica indio amazonico
    r"C:\Carpeta entrada y salida\Entrada de imagenes\BOTANICA INDIO AMAZONICO\AMARRES DE AMOR",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\BOTANICA INDIO AMAZONICO\AMULETOS PREPARADOS",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\BOTANICA INDIO AMAZONICO\CENTRO ESPIRITUAL",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\BOTANICA INDIO AMAZONICO\CURACIONES ESPIRITUALES",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\BOTANICA INDIO AMAZONICO\ENDULZAMIENTOS DE AMOR",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\BOTANICA INDIO AMAZONICO\HIERBAS ESOTERICAS",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\BOTANICA INDIO AMAZONICO\LECTURA DE CARTAS",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\BOTANICA INDIO AMAZONICO\LIMPIEZAS ESPIRITUALES",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\BOTANICA INDIO AMAZONICO\SANTERIA",
    # Botanica maestros espirituales
    r"C:\Carpeta entrada y salida\Entrada de imagenes\BOTANICA MAESTROS ESPIRITUALES\AMARRES DE AMOR",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\BOTANICA MAESTROS ESPIRITUALES\AMULETOS PREPARADOS",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\BOTANICA MAESTROS ESPIRITUALES\CENTRO ESPIRITUAL",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\BOTANICA MAESTROS ESPIRITUALES\CURACIONES ESPIRITUALES",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\BOTANICA MAESTROS ESPIRITUALES\ENDULZAMIENTOS DE AMOR",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\BOTANICA MAESTROS ESPIRITUALES\LECTURA DE CARTAS",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\BOTANICA MAESTROS ESPIRITUALES\LIMPIEZAS ESPIRITUALES",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\BOTANICA MAESTROS ESPIRITUALES\TIENDA ESOTERICA",
    # Botanica secreto azteca
    r"C:\Carpeta entrada y salida\Entrada de imagenes\BOTANICA SECRETO AZTECA\AMARRES DE AMOR",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\BOTANICA SECRETO AZTECA\AMULETOS PREPARADOS",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\BOTANICA SECRETO AZTECA\CENTRO ESPIRITUAL",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\BOTANICA SECRETO AZTECA\CURACIONES ESPIRITUALES",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\BOTANICA SECRETO AZTECA\ENDULZAMIENTOS DE AMOR",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\BOTANICA SECRETO AZTECA\LECTURA DEL TAROT",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\BOTANICA SECRETO AZTECA\LIMPIEZAS ESPIRITUALES",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\BOTANICA SECRETO AZTECA\SANTERIA",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\BOTANICA SECRETO AZTECA\TIENDA ESOTERICA",
    # Botanica virgen morena
    r"C:\Carpeta entrada y salida\Entrada de imagenes\BOTANICA VIRGEN MORENA\AMARRES DE AMOR",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\BOTANICA VIRGEN MORENA\AMULETOS PREPARADOS",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\BOTANICA VIRGEN MORENA\BRUJOS",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\BOTANICA VIRGEN MORENA\CURACIONES ESPIRITUALES",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\BOTANICA VIRGEN MORENA\ENDULZAMIENTOS DE AMOR",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\BOTANICA VIRGEN MORENA\LECTURA DE CARTAS",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\BOTANICA VIRGEN MORENA\LIMPIEZAS ESPIRITUALES",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\BOTANICA VIRGEN MORENA\SANTERIA",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\BOTANICA VIRGEN MORENA\TIENDA ESOTERICA",
    # Cash deals today
    r"C:\Carpeta entrada y salida\Entrada de imagenes\CASH DEALS TODAY\BUYING A HOME WITHOUT FINANCING HOW TO DO IT",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\CASH DEALS TODAY\BUYING HOMES NO MORTGAGE, CASH ONLY",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\CASH DEALS TODAY\BUYING HOMES THE POWER OF DIRECT PAYMENT",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\CASH DEALS TODAY\BUYING IN CASH AN EASY PATH TO HOUSING",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\CASH DEALS TODAY\BUYING YOUR HOME THE FORMULA FOR SUCCESS IS CASH",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\CASH DEALS TODAY\CASH AND PROPERTY YOUR FUTURE HOME WITHIN REACH",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\CASH DEALS TODAY\CASH IN HAND, HOME OWNERSHIP HOW",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\CASH DEALS TODAY\LIQUID MONEY! BUY YOUR HOUSE RIGHT NOW",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\CASH DEALS TODAY\NO FINANCING YOUR GUIDE TO BUYING A HOME FOR CASH",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\CASH DEALS TODAY\QUICK BUY CASH HOMES IN THE SPOTLIGHT",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\CASH DEALS TODAY\YOUR HOME, YOUR MONEY BUY CASH TODAY",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\CASH DEALS TODAY\YOUR OWN HOME CASH ON DELIVERY, NO WAITING",
    # Elite chicago spa- facial
    r"C:\Carpeta entrada y salida\Entrada de imagenes\ELITE CHICAGO SPA\ELITE CHICAGO SPA - FACIAL\BOTOX CHICAGO",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\ELITE CHICAGO SPA\ELITE CHICAGO SPA - FACIAL\DERMAL FILLERS",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\ELITE CHICAGO SPA\ELITE CHICAGO SPA - FACIAL\DERMAPLANING CHICAGO",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\ELITE CHICAGO SPA\ELITE CHICAGO SPA - FACIAL\FRACTIONAL RADIO FRECUENCY",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\ELITE CHICAGO SPA\ELITE CHICAGO SPA - FACIAL\GLOW FACIAL",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\ELITE CHICAGO SPA\ELITE CHICAGO SPA - FACIAL\MICRODERMABRASION",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\ELITE CHICAGO SPA\ELITE CHICAGO SPA - FACIAL\MICRONEEDLING",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\ELITE CHICAGO SPA\ELITE CHICAGO SPA - FACIAL\PRP (PLATELET RICH PLASMA)",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\ELITE CHICAGO SPA\ELITE CHICAGO SPA - FACIAL\SISTEM CELL PRP",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\ELITE CHICAGO SPA\ELITE CHICAGO SPA - FACIAL\THREAD LIFT",
    # Elite chicago spa- grasa
    r"C:\Carpeta entrada y salida\Entrada de imagenes\ELITE CHICAGO SPA\ELITE CHICAGO SPA - GRASA\CARBOXITERAPY",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\ELITE CHICAGO SPA\ELITE CHICAGO SPA - GRASA\CELLULITE REMOVAL",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\ELITE CHICAGO SPA\ELITE CHICAGO SPA - GRASA\COOL SCULPTING",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\ELITE CHICAGO SPA\ELITE CHICAGO SPA - GRASA\DOUBLE CHIN REDUCTION",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\ELITE CHICAGO SPA\ELITE CHICAGO SPA - GRASA\LAKEVIEW MASSAGE SPA",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\ELITE CHICAGO SPA\ELITE CHICAGO SPA - GRASA\LASER HAIR REMOVAL",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\ELITE CHICAGO SPA\ELITE CHICAGO SPA - GRASA\LIP FILLERS CHICAGO",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\ELITE CHICAGO SPA\ELITE CHICAGO SPA - GRASA\LIPO LASER",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\ELITE CHICAGO SPA\ELITE CHICAGO SPA - GRASA\ULTRA SONIC CAVITATION",
    # Elite frenchies
    r"C:\Carpeta entrada y salida\Entrada de imagenes\ELITE FRENCHIES\CARE OF A FRENCH BULLDOG",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\ELITE FRENCHIES\FRENCH BULLDOG - CHARACTER AND CHARACTERISTICS",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\ELITE FRENCHIES\FRENCH BULLDOG BREEDERS",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\ELITE FRENCHIES\FRENCH BULLDOG BREEDING",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\ELITE FRENCHIES\FRENCH BULLDOG GESTATION, PREGNANCY AND CARE",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\ELITE FRENCHIES\FRENCH BULLDOG STUD",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\ELITE FRENCHIES\FRENCH BULLDOG, ONE OF THE WORLD´S BEST COMPANION DOGS",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\ELITE FRENCHIES\FRENCH BULLDOGS CHARACTERISTICS AND PERSONALITY",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\ELITE FRENCHIES\KEY ASPECTS TO TAKE GOOD CARE OF A FRENCH BULLDOG",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\ELITE FRENCHIES\KNOW THE TEMPERAMENT OF THE FRENCH BULLDOG",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\ELITE FRENCHIES\RARE COLORS IN FRENCH BULLDOGS",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\ELITE FRENCHIES\THE BULLDOG, THE DOG BREED THAT WILL CONQUER YOUR HEART",
    # Express clean - comercial
    r"C:\Carpeta entrada y salida\Entrada de imagenes\EXPRESS CLEAN\EXPRESS CLEAN - COMERCIAL\CLEANING SERVICES",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\EXPRESS CLEAN\EXPRESS CLEAN - COMERCIAL\COMERCIAL CLEANING SERVICES",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\EXPRESS CLEAN\EXPRESS CLEAN - COMERCIAL\EVENT CLEANING",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\EXPRESS CLEAN\EXPRESS CLEAN - COMERCIAL\OFFICE CLEANING",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\EXPRESS CLEAN\EXPRESS CLEAN - COMERCIAL\RESTAURANT CLEANING SERVICES",
    # Express clean - residencial
    r"C:\Carpeta entrada y salida\Entrada de imagenes\EXPRESS CLEAN\EXPRESS CLEAN - RESIDENCIAL\AIRBNB CLEANING",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\EXPRESS CLEAN\EXPRESS CLEAN - RESIDENCIAL\APARTAMENT CLEANING",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\EXPRESS CLEAN\EXPRESS CLEAN - RESIDENCIAL\CLEANING SERVICES",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\EXPRESS CLEAN\EXPRESS CLEAN - RESIDENCIAL\DAME DAY CLEANING",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\EXPRESS CLEAN\EXPRESS CLEAN - RESIDENCIAL\HOUSE CLEANING",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\EXPRESS CLEAN\EXPRESS CLEAN - RESIDENCIAL\MAID CLEANING SERVICES",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\EXPRESS CLEAN\EXPRESS CLEAN - RESIDENCIAL\MAID SERVICE SKOKIE IL",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\EXPRESS CLEAN\EXPRESS CLEAN - RESIDENCIAL\MAID SERVICES",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\EXPRESS CLEAN\EXPRESS CLEAN - RESIDENCIAL\MOVE OUT CLEANING",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\EXPRESS CLEAN\EXPRESS CLEAN - RESIDENCIAL\SAME DAY CLEANING",
    # Lopez y Lopez abogados
    r"C:\Carpeta entrada y salida\Entrada de imagenes\LOPEZ Y LOPEZ ABOGADOS\ABOGADOS EN BOSA",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\LOPEZ Y LOPEZ ABOGADOS\ABOGADOS EN CALI",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\LOPEZ Y LOPEZ ABOGADOS\ABOGADOS EN CARTAGENA",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\LOPEZ Y LOPEZ ABOGADOS\ABOGADOS EN CUCUTA",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\LOPEZ Y LOPEZ ABOGADOS\ABOGADOS EN DERECHO ADMINISTRATIVO",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\LOPEZ Y LOPEZ ABOGADOS\ABOGADOS EN ENGATIVA",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\LOPEZ Y LOPEZ ABOGADOS\ABOGADOS EN KENNEDY",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\LOPEZ Y LOPEZ ABOGADOS\ABOGADOS EN SANTA MARTA",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\LOPEZ Y LOPEZ ABOGADOS\ABOGADOS EN USME",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\LOPEZ Y LOPEZ ABOGADOS\ABOGADOS PENALISTAS BOGOTA",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\LOPEZ Y LOPEZ ABOGADOS\DERECHO DE FAMILIA",
    # Oceola - comercial
    r"C:\Carpeta entrada y salida\Entrada de imagenes\OSCEOLA\OSCEOLA - COMERCIAL\CHAIN LINK FENCE",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\OSCEOLA\OSCEOLA - COMERCIAL\CHICAGO STEEL FENCE",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\OSCEOLA\OSCEOLA - COMERCIAL\COMMERCIAL FENCE INSTALLATION",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\OSCEOLA\OSCEOLA - COMERCIAL\INDUSTRIAL FENCE COMPANY",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\OSCEOLA\OSCEOLA - COMERCIAL\IRON BOLLARDS INSTALLATION",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\OSCEOLA\OSCEOLA - COMERCIAL\IRON FENCE INDUSTRIAL",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\OSCEOLA\OSCEOLA - COMERCIAL\VINYL FENCE",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\OSCEOLA\OSCEOLA - COMERCIAL\WOOD FENCE",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\OSCEOLA\OSCEOLA - COMERCIAL\WROUGHT IRON STAIRCA SES",
    # Oceola - residencial
    r"C:\Carpeta entrada y salida\Entrada de imagenes\OSCEOLA\OSCEOLA - RESIDENCIAL\AUTOMATIC GATE",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\OSCEOLA\OSCEOLA - RESIDENCIAL\CHAIN LINK FENCE",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\OSCEOLA\OSCEOLA - RESIDENCIAL\COMPOSITE FENCE",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\OSCEOLA\OSCEOLA - RESIDENCIAL\CUSTOM WROUGHT IRON RAILINGS",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\OSCEOLA\OSCEOLA - RESIDENCIAL\FENCE COMPANY WINNETKA",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\OSCEOLA\OSCEOLA - RESIDENCIAL\FIRE SCAPES CHICAGO",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\OSCEOLA\OSCEOLA - RESIDENCIAL\IRON FENCE",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\OSCEOLA\OSCEOLA - RESIDENCIAL\RESIDENTIAL ALUMINUM FENCES",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\OSCEOLA\OSCEOLA - RESIDENCIAL\SECURITY CAMERAS SYSTEMS",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\OSCEOLA\OSCEOLA - RESIDENCIAL\VINYL FENCE",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\OSCEOLA\OSCEOLA - RESIDENCIAL\WOOD FENCE",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\OSCEOLA\OSCEOLA - RESIDENCIAL\WROUGHT IRON BALCONY RAILING",
    # Quick cleaning - comercial
    r"C:\Carpeta entrada y salida\Entrada de imagenes\QUICK CLEANING\QUICK CLEANING - COMERCIAL\CLEANING SERVICES",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\QUICK CLEANING\QUICK CLEANING - COMERCIAL\CLEANING SERVICES LOGAN SQUARE",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\QUICK CLEANING\QUICK CLEANING - COMERCIAL\COMMERCIAL CLEANING",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\QUICK CLEANING\QUICK CLEANING - COMERCIAL\DAYCARE CLEANING",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\QUICK CLEANING\QUICK CLEANING - COMERCIAL\DENTAL OFFICE CLEANING",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\QUICK CLEANING\QUICK CLEANING - COMERCIAL\EVENT CLEANING",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\QUICK CLEANING\QUICK CLEANING - COMERCIAL\GYM CLEANING",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\QUICK CLEANING\QUICK CLEANING - COMERCIAL\OFFICE CLEANING",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\QUICK CLEANING\QUICK CLEANING - COMERCIAL\RESTAURANT CLEANING SERVICES",
    # Quick cleaning - residencial
    r"C:\Carpeta entrada y salida\Entrada de imagenes\QUICK CLEANING\QUICK CLEANING - RESIDENCIAL\AIRBNB CLEANING",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\QUICK CLEANING\QUICK CLEANING - RESIDENCIAL\APARTAMENT CLEANING",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\QUICK CLEANING\QUICK CLEANING - RESIDENCIAL\DEEP CLEANING SERVICES",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\QUICK CLEANING\QUICK CLEANING - RESIDENCIAL\HOUSE CLEANING",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\QUICK CLEANING\QUICK CLEANING - RESIDENCIAL\MAID CLEANING SERVICES",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\QUICK CLEANING\QUICK CLEANING - RESIDENCIAL\MAID SERVICES",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\QUICK CLEANING\QUICK CLEANING - RESIDENCIAL\MOVE OUT CLEANING",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\QUICK CLEANING\QUICK CLEANING - RESIDENCIAL\POST CONSTRUCTION CLEANING",
    r"C:\Carpeta entrada y salida\Entrada de imagenes\QUICK CLEANING\QUICK CLEANING - RESIDENCIAL\RENTAL PROPERTY CLEANING SERVICES"
]

indice_destino = 0
numero_ruta = 0
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
        os.remove(archivo_a_cargar)

    except Exception as e:
        print(f"Ocurrió un error al hacer clic en el botón de descarga: {e}")
def mover_archivos_entre_carpetas(ruta_origen, ruta_destino):
    # Itera sobre los archivos en la carpeta de origen y muévelos a la ruta de destino
    for archivo in os.listdir(ruta_origen):
        ruta_archivo_origen = os.path.join(ruta_origen, archivo)

        # Verifica si el elemento en la ruta de origen es un archivo (no es una carpeta)
        if os.path.isfile(ruta_archivo_origen):
            try:
                shutil.move(ruta_archivo_origen, os.path.join(ruta_destino, archivo))
                print(f"Archivo '{archivo}' movido a {ruta_destino}")
            except Exception as e:
                print(f"Error al mover el archivo '{archivo}' a {ruta_destino}: {str(e)}")
def modify_metadata_batch(metadata_list):
    # Ruta al ejecutable de ExifTool
    exiftool_path = "./exiftool.exe"

    def modify_metadata(ruta_archivo, metadata):
        nueva_descripcion = metadata.get('descripcion', '')
        nuevo_titulo = metadata.get('titulo', '')
        nuevas_etiquetas = metadata.get('etiquetas', '')
        nueva_latitud = metadata.get('latitud', '')
        nueva_longitud = metadata.get('longitud', '')

        # Modificar metadatos con ExifTool para el archivo
        command = [
            exiftool_path,
            '-ImageDescription=' + nueva_descripcion,
            '-Title=' + nuevo_titulo,
            '-Keywords=' + nuevas_etiquetas,
            '-GPSLatitude=' + nueva_latitud,
            '-GPSLongitude=' + nueva_longitud,
            '-overwrite_original',  # Sobrescribir el archivo original
            ruta_archivo
        ]

        try:
            subprocess.run(command, check=True)
            print(f"Metadatos modificados con éxito para: {ruta_archivo}")
        except subprocess.CalledProcessError as e:
            print(f"Error al modificar los metadatos para {ruta_archivo}: {e}")

    def modify_metadata_in_subfolders(root_folder, metadata):
        for foldername, _, filenames in os.walk(root_folder):
            for filename in filenames:
                ruta_archivo = os.path.join(foldername, filename)
                modify_metadata(ruta_archivo, metadata)

    # Procesar cada conjunto de metadatos en metadata_list
    for metadata in metadata_list:
        root_folder = metadata['ruta']
        modify_metadata_in_subfolders(root_folder, metadata)
# Iterar sobre cada ruta de carpeta de imágenes
for ruta_imagenes in rutas_imagenes:
    archivos = os.listdir(ruta_imagenes)  # Obtener la lista de archivos en la carpeta

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
        descargar_imagen(nombre_archivo)
        time.sleep(4)

        # Después de procesar la imagen y descargarla, mover archivos
        mover_archivos_entre_carpetas(ruta_origen, rutas_destino[numero_ruta])
        time.sleep(4)

        # Volver a la página inicial después de procesar una imagen
        driver.get("https://www.iloveimg.com/resize-image")
        time.sleep(4)

    numero_ruta += 1
    print(numero_ruta)
time.sleep(2)
modify_metadata_batch(metadata_list)
# Cerrar el navegador después de procesar todas las imágenes
driver.quit()
