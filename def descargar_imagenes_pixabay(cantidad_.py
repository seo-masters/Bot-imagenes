import os
import requests

# Lista de búsquedas y rutas de guardado

busquedas = [
#BOTANICA AMARRES DE AMOR
    ['', ''],#AMARRES DE AMOR
    ['', ''],#AMULETOS PREPARADOS
    ['', ''],#CURACIONES ESPIRITUALES
    ['', ''],#ENDULZAMIENTOS DE AMOR
    ['', ''],#HIERBAS ESOTERICAS
    ['', ''],#LECTURA DE CARTAS
    ['', ''],#LIMPIEZAS ESPIRITUALES
    ['', ''],#SANTERIA
#BOTANICA DEL AMOR
    ['', ''],#AMARRES DE AMOR
    ['', ''],#AMULETOS PREPARADOS
    ['', ''],#CENTRO ESPIRITUAL
    ['', ''],#CURACIONES ESPIRITUALES
    ['', ''],#ENDULZAMIENTOS DE AMOR
    ['raton', ''],#LECTURA DE CARTAS
    ['', ''],#LECTURA DEL TAROT
    ['', ''],#LIMPIEZAS ESPIRITUALES
    ['', ''],#TIENDA ESOTERICA
#BOTANICA INDIO AMAZONICO
    ['', ''],#AMARRES DE AMOR
    ['', ''],#AMULETOS PREPARADOS
    ['', ''],#CENTRO ESPIRITUAL
    ['', ''],#CURACIONES ESPIRITUALES
    ['', ''],#ENDULZAMIENTOS DE AMOR
    ['', ''],#HIERBAS ESOTERICAS
    ['', ''],#LECTURA DE CARTAS
    ['', ''],#LIMPIEZAS ESPIRITUALES
    ['', ''],#SANTERIA
#BOTANICA MAESTROS ESPIRITUALES
    ['', ''],#AMARRES DE AMOR
    ['', ''],#AMULETOS PREPARADOS
    ['', ''],#CENTRO ESPIRITUAL
    ['', ''],#CURACIONES ESPIRITUALES
    ['', ''],#ENDULZAMIENTOS DE AMOR
    ['', ''],#LECTURA DE CARTAS
    ['', ''],#LIMPIEZAS ESPIRITUALES
    ['', ''],#TIENDA ESOTERICA
#BOTANICA SECRETO AZTECA
    ['', ''],#AMARRES DE AMOR
    ['', ''],#AMULETOS PREPARADOS
    ['', ''],#CENTRO ESPIRITUAL
    ['', ''],#CURACIONES ESPIRITUALES
    ['', ''],#ENDULZAMIENTOS DE AMOR
    ['', ''],#LECTURA DEL TAROT
    ['', ''],#LIMPIEZAS ESPIRITUALES
    ['', ''],#SANTERIA
    ['', ''],#TIENDA ESOTERICA
#BOTANICA VIRGEN MORENA
    ['', ''],#AMARRES DE AMOR
    ['', ''],#AMULETOS PREPARADOS
    ['', ''],#BRUJOS
    ['', ''],#CURACIONES ESPIRITUALES
    ['', ''],#ENDULZAMIENTOS DE AMOR
    ['', ''],#LECTURA DE CARTAS
    ['', ''],#LIMPIEZAS ESPIRITUALES
    ['', ''],#SANTERIA
    ['', ''],#TIENDA ESOTERICA
#CASH DEALS TODAY
    ['', ''],#BUYING A HOME WITHOUT FINANCING HOW TO DO IT
    ['', ''],#BUYING HOMES NO MORTGAGE, CASH ONLY
    ['', ''],#BUYING HOMES THE POWER OF DIRECT PAYMENT
    ['', ''],#BUYING IN CASH AN EASY PATH TO HOUSING
    ['', ''],#BUYING YOUR HOME THE FORMULA FOR SUCCESS IS CASH
    ['', ''],#CASH AND PROPERTY YOUR FUTURE HOME WITHIN REACH
    ['', ''],#CASH IN HAND, HOME OWNERSHIP HOW
    ['', ''],#LIQUID MONEY! BUY YOUR HOUSE RIGHT NOW
    ['', ''],#NO FINANCING YOUR GUIDE TO BUYING A HOME FOR CASH
    ['', ''],#QUICK BUY CASH HOMES IN THE SPOTLIGHT
    ['', ''],#YOUR HOME, YOUR MONEY BUY CASH TODAY
    ['', ''],#YOUR OWN HOME CASH ON DELIVERY, NO WAITING
#ELITE CHICAGO SPA-FACIAL
    ['', ''],#BOTOX CHICAGO
    ['', ''],#DERMAL FILLERS
    ['', ''],#DERMAPLANING CHICAGO
    ['', ''],#FRACTIONAL RADIO FRECUENCY
    ['', ''],#GLOW FACIAL
    ['', ''],#MICRODERMABRASION
    ['', ''],#MICRONEEDLING
    ['', ''],#PRP (PLATELET RICH PLASMA)
    ['', ''],#SISTEM CELL PRP
    ['', ''],#THREAD LIFT
#ELITE CHICAGO SPA - GRASA
    ['', ''],#CARBOXITERAPY
    ['', ''],#CELLULITE REMOVAL
    ['', ''],#COOL SCULPTING
    ['', ''],#DOUBLE CHIN REDUCTION
    ['', ''],#LAKEVIEW MASSAGE SPA
    ['', ''],#LASER HAIR REMOVAL
    ['', ''],#LIP FILLERS CHICAGO
    ['', ''],#LIPO LASER
    ['', ''],#ULTRA SONIC CAVITATION
#ELITE FRENCHIES
    ['', ''],#CARE OF A FRENCH BULLDOG
    ['', ''],#FRENCH BULLDOG - CHARACTER AND CHARACTERISTICS
    ['', ''],#FRENCH BULLDOG BREEDERS
    ['', ''],#FRENCH BULLDOG BREEDING
    ['', ''],#FRENCH BULLDOG GESTATION, PREGNANCY AND CARE
    ['', ''],#FRENCH BULLDOG STUD
    ['', ''],#FRENCH BULLDOG, ONE OF THE WORLD´S BEST COMPANION DOGS
    ['', ''],#FRENCH BULLDOGS CHARACTERISTICS AND PERSONALITY
    ['', ''],#KEY ASPECTS TO TAKE GOOD CARE OF A FRENCH BULLDOG
    ['', ''],#KNOW THE TEMPERAMENT OF THE FRENCH BULLDOG
    ['', ''],#RARE COLORS IN FRENCH BULLDOGS
    ['', ''],#THE BULLDOG, THE DOG BREED THAT WILL CONQUER YOUR HEART
#EXPRESS CLEAN - COMERCIAL
    ['', ''],#CLEANING SERVICES
    ['', ''],#COMERCIAL CLEANING SERVICES
    ['', ''],#EVENT CLEANING
    ['', ''],#OFFICE CLEANING
    ['', ''],#RESTAURANT CLEANING SERVICES
#EXPRESS CLEAN - RESIDENCIAL
    ['', ''],#AIRBNB CLEANING
    ['', ''],#APARTAMENT CLEANING
    ['', ''],#CLEANING SERVICES
    ['', ''],#DAME DAY CLEANING
    ['', ''],#HOUSE CLEANING
    ['', ''],#MAID CLEANING SERVICES
    ['', ''],#MAID SERVICE SKOKIE IL
    ['', ''],#MAID SERVICES
    ['', ''],#MOVE OUT CLEANING
    ['', ''],#SAME DAY CLEANING
#LOPEZ Y LOPEZ ABOGADOS
    ['', ''],#ABOGADOS EN BOSA
    ['', ''],#ABOGADOS EN CALI
    ['', ''],#ABOGADOS EN CARTAGENA
    ['', ''],#ABOGADOS EN CUCUTA
    ['', ''],#ABOGADOS EN DERECHO ADMINISTRATIVO
    ['', ''],#ABOGADOS EN ENGATIVA
    ['', ''],#ABOGADOS EN KENNEDY
    ['', ''],#ABOGADOS EN SANTA MARTA
    ['', ''],#ABOGADOS EN USME
    ['', ''],#ABOGADOS PENALISTAS BOGOTA
    ['', ''],#DERECHO DE FAMILIA
#OSCEOLA - COMERCIAL
    ['', ''],#CHAIN LINK FENCE
    ['', ''],#CHICAGO STEEL FENCE
    ['', ''],#COMMERCIAL FENCE INSTALLATION
    ['', ''],#INDUSTRIAL FENCE COMPANY
    ['', ''],#IRON BOLLARDS INSTALLATION
    ['', ''],#IRON FENCE INDUSTRIAL
    ['', ''],#VINYL FENCE
    ['', ''],#WOOD FENCE
    ['', ''],#WROUGHT IRON STAIRCA SES
#OSCEOLA - RESIDENCIAL
    ['', ''],#AUTOMATIC GATE
    ['', ''],#CHAIN LINK FENCE
    ['', ''],#COMPOSITE FENCE
    ['', ''],#CUSTOM WROUGHT IRON RAILINGS
    ['', ''],#FENCE COMPANY WINNETKA
    ['', ''],#FIRE SCAPES CHICAGO
    ['', ''],#IRON FENCE
    ['', ''],#RESIDENTIAL ALUMINUM FENCES
    ['', ''],#SECURITY CAMERAS SYSTEMS
    ['', ''],#VINYL FENCE
    ['', ''],#WOOD FENCE
    ['', ''],#WROUGHT IRON BALCONY RAILING
#QUICK CLEANING - COMERCIAL
    ['', ''],#CLEANING SERVICES
    ['', ''],#CLEANING SERVICES LOGAN SQUARE
    ['', ''],#COMMERCIAL CLEANING
    ['', ''],#DAYCARE CLEANING
    ['', ''],#DENTAL OFFICE CLEANING
    ['', ''],#EVENT CLEANING
    ['', ''],#GYM CLEANING
    ['', ''],#OFFICE CLEANING
    ['', ''],#RESTAURANT CLEANING SERVICES
    # Agrega más búsquedas aquí si es necesario
]

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
