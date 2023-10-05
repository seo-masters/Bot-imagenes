from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from APIpexels import PexelsAPI
import os
import requests
import time
import shutil
import subprocess
import threading
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
        'descripcion': 'En Amarres de amor en Chicago realizo mis poderosos rituales, que te ayudarán a regresar con tu ser amado, ¡cambio tu sufrimiento por felicidad!, Cuento con más de 30 años de experiencia en hechizos de amor en Chicago Illinois, Ofreciendo una amplia gama de servicios para satisfacer todas tus necesidades, como servicios de amarres de magia, incluyendo amarres pactados y amarres con solo la foto. Además, realizo amarres del mismo sexo, endulzamientos de amor, amarres de amor express, lecturas del tarot y amarres de matrimonio. Trabajo las 24 horas y garantizo resultados en 24 horas. ¡Permíteme ayudarte a encontrar el amor y la felicidad que mereces!',
        'titulo': ' ',
        'etiquetas': 'Santeria Botanica Chicago, Santeria Botanica Chicago, Santeria Botanica Chicago Illinois, Chicago Santeria Botanica, Santeria Botanica Chicago, Santeria Botanica Chicago cerca de mi, la mejor Santeria Botanica Chicago, Amarres de amor gay chicago, Amarres de amor gay en Chicago, Amarres de amor gay Chicago IL, Los mejores amarres de amor Gay en Chicago, Amarres de amor gay Illinois, Brujeria Chicago, Brujeria en Chicago, Brujos Buenos En Chicago, Brujos Chicago Illinois, Los Mejores Brujos Chicago, Brujos Expertos En Chicago, Amarres de amor Chicago, Amarres De Amor En Chicago, Amarres De Amor Chicago IL, Expertos Amarres De Amor En Chicago, Amarres De Amor En IL, Los Mejores Amarres De Amor En Chicago, Amarres Chicago, Amarres 24 horas chicago, Ritual Abrecaminos Chicago, Ritual Abrecaminos Chicago, Ritual Abrecaminos Chicago Il, Ritual Abrecaminos Chicago Illinois, El Mejor Ritual Abrecaminos Chicago, Ritual Abrecaminos Cerca de Mi, Expertos en Ritual abrecaminos en Chicago, Limpieza espiritual Chicago, Limpia Espiritual Chicago, Limpieza Espirituales en Chicago Il, Limpieza Espiritual en Chicago Illinois, La mejor Limpieza Espiritual en Chicago, Limpieza Espiritual Cerca de Mi, Limpias y Barridas Chicago, Limpias y Barridas en Chicago, Limpias y Barridas  Chicago Il, Limpias y Barridas en Chicago Illinois, Las mejores Limpias y Barridas en Chicago, Limpias y Barridas Cerca de Mi, Limpieza espiritual para negocios Chicago, Limpia Espiritual para negocios Chicago, Limpieza Espiritual para negocios en Chicago Il, Limpieza  Espiritual para negocios en Chicago Illinois, La mejor Limpieza  Espiritual para negocios en Chicago, Limpieza Espiritual para negocios Cerca de Mi, Limpieza espiritual del Hogar Chicago, Limpieza espiritual del Hogar en Chicago, Limpieza espiritual del Hogar en Chicago Il, Limpieza espiritual del Hogar  en Chicago Illinois, La mejor Limpieza espiritual del Hogar en Chicago, Limpieza espiritual del Hogar Cerca de Mi, Endulzamientos de amor Chicago, Chicago Endulsamiento de Amor, Endulzamiento de amor en Chicago Il, Endulzamientos de amor Chicago Illinois, los mejores Endulzamientos de amor en Chicago , Endulzamiento de Amor Cerca de Mi, Lectura del tarot Chicago, Lectura del tarot en Chicago, Lectura del tarot Chicago IL, Expertos en Lectura del tarot en Chicago, Lectura del tarot en IL, la mejor Lectura del tarot en Chicago, lectura de cartas Chicago, lectura de cartas cerca de mi, Curacion espiritual Chicago, Curacion espiritual en Chicago, Curacion espiritual Chicago IL, Expertos en Curaciones espirituales en Chicago, Curacion espiritual en IL, La mejor Curacion espiritual en Chicago, Union de parejas Chicago, Union de parejas Chicago, Union de parejas cerca de mi, Union de parejas en Chicago Illionis, Union de parejas en Chicago Il, La mejor union de parejas en Chicago, Dominios de amor Chicago, Dominios de Amor Chicago, Dominios de Amor Chicago Il, Dominios de amor Chicago Illinois, Los mejores Dominios de Amor en Chicago, Dominios de Amor Cerca de Mi, Hechizos de amor Chicago, Hechizos de amor Chicago, Hechizos de amor Chicago Il, Hechizos de amor Chicago Illinois, Los mejores Hechizos de amor en Chicago, Hechizos de amor Cerca de Mi',
        'latitud': '41.84454120773466',
        'longitud': '-87.70350036142716'
    },
    {
        'ruta': r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA DEL AMOR",
        'descripcion': 'Si estás buscando brujos en Chicago, has llegado a la Botánica del Amor, donde te ofrecemos todo tipo de trabajos espirituales. Contamos con todos los productos necesarios para ayudarte en el amor, el dinero, el trabajo y la salud. Además, ofrecemos diversos servicios espirituales, como limpiezas espirituales, lecturas de la mente, lectura del tarot y servicios de vidente, para aquellas personas que necesitan consejos espirituales. Si estás buscando una Botánica que te ayude con tus problemas, llama ya a la Botánica del Amor. Con una experiencia de 45 años, estoy aquí para brindarte todo lo que necesites. Y eso no es todo. También ofrecemos una variedad de servicios adicionales para satisfacer tus necesidades como: lectura del tarot, rituales con magia blanca, ritual de florecimiento, curaciones en botánica, limpieza de tu hogar y amarres de amor. También, puede visitarnos en La Villita de Chicago o Little Village. Aquí, usted podrá encontrar diferentes rituales y hechizos de santería en Chicago.',
        'titulo': ' ',
        'etiquetas': 'Santeria Botanica Chicago, Santeria Botanica Chicago, Santeria Botanica Chicago Illinois, Chicago Santeria Botanica, Santeria Botanica Chicago, Santeria Botanica Chicago cerca de mi, la mejor Santeria Botanica Chicago, Amarres de amor gay chicago, Amarres de amor gay en Chicago, Amarres de amor gay Chicago IL, Los mejores amarres de amor Gay en Chicago, Amarres de amor gay Illinois, Brujeria Chicago, Brujeria en Chicago, Brujos Buenos En Chicago, Brujos Chicago Illinois, Los Mejores Brujos Chicago, Brujos Expertos En Chicago, Amarres de amor Chicago, Amarres De Amor En Chicago, Amarres De Amor Chicago IL, Expertos Amarres De Amor En Chicago, Amarres De Amor En IL, Los Mejores Amarres De Amor En Chicago, Amarres Chicago, Amarres 24 horas chicago, Ritual Abrecaminos Chicago, Ritual Abrecaminos Chicago, Ritual Abrecaminos Chicago Il, Ritual Abrecaminos Chicago Illinois, El Mejor Ritual Abrecaminos Chicago, Ritual Abrecaminos Cerca de Mi, Expertos en Ritual abrecaminos en Chicago, Limpieza espiritual Chicago, Limpia Espiritual Chicago, Limpieza Espirituales en Chicago Il, Limpieza Espiritual en Chicago Illinois, La mejor Limpieza Espiritual en Chicago, Limpieza Espiritual Cerca de Mi, Limpias y Barridas Chicago, Limpias y Barridas en Chicago, Limpias y Barridas  Chicago Il, Limpias y Barridas en Chicago Illinois, Las mejores Limpias y Barridas en Chicago, Limpias y Barridas Cerca de Mi, Limpieza espiritual para negocios Chicago, Limpia Espiritual para negocios Chicago, Limpieza Espiritual para negocios en Chicago Il, Limpieza  Espiritual para negocios en Chicago Illinois, La mejor Limpieza  Espiritual para negocios en Chicago, Limpieza Espiritual para negocios Cerca de Mi, Limpieza espiritual del Hogar Chicago, Limpieza espiritual del Hogar en Chicago, Limpieza espiritual del Hogar en Chicago Il, Limpieza espiritual del Hogar  en Chicago Illinois, La mejor Limpieza espiritual del Hogar en Chicago, Limpieza espiritual del Hogar Cerca de Mi, Endulzamientos de amor Chicago, Chicago Endulsamiento de Amor, Endulzamiento de amor en Chicago Il, Endulzamientos de amor Chicago Illinois, los mejores Endulzamientos de amor en Chicago , Endulzamiento de Amor Cerca de Mi, Lectura del tarot Chicago, Lectura del tarot en Chicago, Lectura del tarot Chicago IL, Expertos en Lectura del tarot en Chicago, Lectura del tarot en IL, la mejor Lectura del tarot en Chicago, lectura de cartas Chicago, lectura de cartas cerca de mi, Curacion espiritual Chicago, Curacion espiritual en Chicago, Curacion espiritual Chicago IL, Expertos en Curaciones espirituales en Chicago, Curacion espiritual en IL, La mejor Curacion espiritual en Chicago, Union de parejas Chicago, Union de parejas Chicago, Union de parejas cerca de mi, Union de parejas en Chicago Illionis, Union de parejas en Chicago Il, La mejor union de parejas en Chicago, Dominios de amor Chicago, Dominios de Amor Chicago, Dominios de Amor Chicago Il, Dominios de amor Chicago Illinois, Los mejores Dominios de Amor en Chicago, Dominios de Amor Cerca de Mi, Hechizos de amor Chicago, Hechizos de amor Chicago, Hechizos de amor Chicago Il, Hechizos de amor Chicago Illinois, Los mejores Hechizos de amor en Chicago, Hechizos de amor Cerca de Mi',
        'latitud': '41.84416952145552',
        'longitud': '-87.70333239849182'
    },
    {
        'ruta': r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA INDIO AMAZONICO",
        'descripcion': 'En Indio Amazónico, tengo a disposición los rituales más poderosos que te permitirán reconquistar ese amor que una vez se alejó. Cuento con una amplia experiencia realizando amarres de amor en Chicago y puedes confiar en que tengo la capacidad para ayudarte a encontrar la felicidad nuevamente junto a tu ser amado es inigualable. Además, podrás acceder a una amplia gama de trabajos como las limpiezas espirituales, baños esotéricos, curaciones, lecturas de cartas, entre otros, que están pensados en satisfacer las necesidades de mis clientes en Chicago, Illinois.',
        'titulo': ' ',
        'etiquetas': 'Santeria Botanica Chicago, Santeria Botanica Chicago, Santeria Botanica Chicago Illinois, Chicago Santeria Botanica, Santeria Botanica Chicago, Santeria Botanica Chicago cerca de mi, la mejor Santeria Botanica Chicago, Amarres de amor gay chicago, Amarres de amor gay en Chicago, Amarres de amor gay Chicago IL, Los mejores amarres de amor Gay en Chicago, Amarres de amor gay Illinois, Brujeria Chicago, Brujeria en Chicago, Brujos Buenos En Chicago, Brujos Chicago Illinois, Los Mejores Brujos Chicago, Brujos Expertos En Chicago, Amarres de amor Chicago, Amarres De Amor En Chicago, Amarres De Amor Chicago IL, Expertos Amarres De Amor En Chicago, Amarres De Amor En IL, Los Mejores Amarres De Amor En Chicago, Amarres Chicago, Amarres 24 horas chicago, Ritual Abrecaminos Chicago, Ritual Abrecaminos Chicago, Ritual Abrecaminos Chicago Il, Ritual Abrecaminos Chicago Illinois, El Mejor Ritual Abrecaminos Chicago, Ritual Abrecaminos Cerca de Mi, Expertos en Ritual abrecaminos en Chicago, Limpieza espiritual Chicago, Limpia Espiritual Chicago, Limpieza Espirituales en Chicago Il, Limpieza Espiritual en Chicago Illinois, La mejor Limpieza Espiritual en Chicago, Limpieza Espiritual Cerca de Mi, Limpias y Barridas Chicago, Limpias y Barridas en Chicago, Limpias y Barridas  Chicago Il, Limpias y Barridas en Chicago Illinois, Las mejores Limpias y Barridas en Chicago, Limpias y Barridas Cerca de Mi, Limpieza espiritual para negocios Chicago, Limpia Espiritual para negocios Chicago, Limpieza Espiritual para negocios en Chicago Il, Limpieza  Espiritual para negocios en Chicago Illinois, La mejor Limpieza  Espiritual para negocios en Chicago, Limpieza Espiritual para negocios Cerca de Mi, Limpieza espiritual del Hogar Chicago, Limpieza espiritual del Hogar en Chicago, Limpieza espiritual del Hogar en Chicago Il, Limpieza espiritual del Hogar  en Chicago Illinois, La mejor Limpieza espiritual del Hogar en Chicago, Limpieza espiritual del Hogar Cerca de Mi, Endulzamientos de amor Chicago, Chicago Endulsamiento de Amor, Endulzamiento de amor en Chicago Il, Endulzamientos de amor Chicago Illinois, los mejores Endulzamientos de amor en Chicago , Endulzamiento de Amor Cerca de Mi, Lectura del tarot Chicago, Lectura del tarot en Chicago, Lectura del tarot Chicago IL, Expertos en Lectura del tarot en Chicago, Lectura del tarot en IL, la mejor Lectura del tarot en Chicago, lectura de cartas Chicago, lectura de cartas cerca de mi, Curacion espiritual Chicago, Curacion espiritual en Chicago, Curacion espiritual Chicago IL, Expertos en Curaciones espirituales en Chicago, Curacion espiritual en IL, La mejor Curacion espiritual en Chicago, Union de parejas Chicago, Union de parejas Chicago, Union de parejas cerca de mi, Union de parejas en Chicago Illionis, Union de parejas en Chicago Il, La mejor union de parejas en Chicago, Dominios de amor Chicago, Dominios de Amor Chicago, Dominios de Amor Chicago Il, Dominios de amor Chicago Illinois, Los mejores Dominios de Amor en Chicago, Dominios de Amor Cerca de Mi, Hechizos de amor Chicago, Hechizos de amor Chicago, Hechizos de amor Chicago Il, Hechizos de amor Chicago Illinois, Los mejores Hechizos de amor en Chicago, Hechizos de amor Cerca de Mi',
        'latitud': '41.84460058305401',
        'longitud': '-87.7137918366031'
    },
    {
        'ruta': r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA MAESTROS ESPIRITUALES",
        'descripcion': 'En Maestros Espirituales, podrás encontrar la solución a todas tus dudas y problemas, ya que cuento con una amplia experiencia en el mundo del esoterismo y te puedo ayudar con todo tipos de trabajos o hechizos que necesites, para que puedas vivir en total plenitud, Somos la mejor Botánica de Chicago. Con mas de 30 años de experiencia, Aquí podrás encontrar un sin fin de servicios que te ayudarán a tener la vida que tanto deseas, cómo mis amarres de amor, mis limpiezas espirituales, baños esotéricos, curaciones, lectura de cartas, entre otros más que poseo, los cuales están únicamente pensados para satisfacer las necesidades de mis clientes en Chicago, Illinois.',
        'titulo': ' ',
        'etiquetas': 'Santeria Botanica Chicago, Santeria Botanica Chicago, Santeria Botanica Chicago Illinois, Chicago Santeria Botanica, Santeria Botanica Chicago, Santeria Botanica Chicago cerca de mi, la mejor Santeria Botanica Chicago, Amarres de amor gay chicago, Amarres de amor gay en Chicago, Amarres de amor gay Chicago IL, Los mejores amarres de amor Gay en Chicago, Amarres de amor gay Illinois, Brujeria Chicago, Brujeria en Chicago, Brujos Buenos En Chicago, Brujos Chicago Illinois, Los Mejores Brujos Chicago, Brujos Expertos En Chicago, Amarres de amor Chicago, Amarres De Amor En Chicago, Amarres De Amor Chicago IL, Expertos Amarres De Amor En Chicago, Amarres De Amor En IL, Los Mejores Amarres De Amor En Chicago, Amarres Chicago, Amarres 24 horas chicago, Ritual Abrecaminos Chicago, Ritual Abrecaminos Chicago, Ritual Abrecaminos Chicago Il, Ritual Abrecaminos Chicago Illinois, El Mejor Ritual Abrecaminos Chicago, Ritual Abrecaminos Cerca de Mi, Expertos en Ritual abrecaminos en Chicago, Limpieza espiritual Chicago, Limpia Espiritual Chicago, Limpieza Espirituales en Chicago Il, Limpieza Espiritual en Chicago Illinois, La mejor Limpieza Espiritual en Chicago, Limpieza Espiritual Cerca de Mi, Limpias y Barridas Chicago, Limpias y Barridas en Chicago, Limpias y Barridas  Chicago Il, Limpias y Barridas en Chicago Illinois, Las mejores Limpias y Barridas en Chicago, Limpias y Barridas Cerca de Mi, Limpieza espiritual para negocios Chicago, Limpia Espiritual para negocios Chicago, Limpieza Espiritual para negocios en Chicago Il, Limpieza  Espiritual para negocios en Chicago Illinois, La mejor Limpieza  Espiritual para negocios en Chicago, Limpieza Espiritual para negocios Cerca de Mi, Limpieza espiritual del Hogar Chicago, Limpieza espiritual del Hogar en Chicago, Limpieza espiritual del Hogar en Chicago Il, Limpieza espiritual del Hogar  en Chicago Illinois, La mejor Limpieza espiritual del Hogar en Chicago, Limpieza espiritual del Hogar Cerca de Mi, Endulzamientos de amor Chicago, Chicago Endulsamiento de Amor, Endulzamiento de amor en Chicago Il, Endulzamientos de amor Chicago Illinois, los mejores Endulzamientos de amor en Chicago , Endulzamiento de Amor Cerca de Mi, Lectura del tarot Chicago, Lectura del tarot en Chicago, Lectura del tarot Chicago IL, Expertos en Lectura del tarot en Chicago, Lectura del tarot en IL, la mejor Lectura del tarot en Chicago, lectura de cartas Chicago, lectura de cartas cerca de mi, Curacion espiritual Chicago, Curacion espiritual en Chicago, Curacion espiritual Chicago IL, Expertos en Curaciones espirituales en Chicago, Curacion espiritual en IL, La mejor Curacion espiritual en Chicago, Union de parejas Chicago, Union de parejas Chicago, Union de parejas cerca de mi, Union de parejas en Chicago Illionis, Union de parejas en Chicago Il, La mejor union de parejas en Chicago, Dominios de amor Chicago, Dominios de Amor Chicago, Dominios de Amor Chicago Il, Dominios de amor Chicago Illinois, Los mejores Dominios de Amor en Chicago, Dominios de Amor Cerca de Mi, Hechizos de amor Chicago, Hechizos de amor Chicago, Hechizos de amor Chicago Il, Hechizos de amor Chicago Illinois, Los mejores Hechizos de amor en Chicago, Hechizos de amor Cerca de Mi',
        'latitud': '41.84449527218073',
        'longitud': '-87.71918606179513'
    },
    {
        'ruta': r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA SECRETO AZTECA",
        'descripcion': 'En Botanicas Chicago, cuento con una amplia variedad de rituales de gran poderío que te ayudarán a recuperar el amor que alguna vez se alejó de ti. Gracias a mis 35 años de experiencia puedo realizar los mejores amarres de amor. Para poder satisfacer todas las necesidades de mis clientes, también cuento con servicios de limpiezas espirituales, baños esotéricos, curaciones, lecturas de cartas, entre otros, Visitanos en nuestra botanica Chicago.',
        'titulo': ' ',
        'etiquetas': 'Santeria Botanica Chicago, Santeria Botanica Chicago, Santeria Botanica Chicago Illinois, Chicago Santeria Botanica, Santeria Botanica Chicago, Santeria Botanica Chicago cerca de mi, la mejor Santeria Botanica Chicago, Amarres de amor gay chicago, Amarres de amor gay en Chicago, Amarres de amor gay Chicago IL, Los mejores amarres de amor Gay en Chicago, Amarres de amor gay Illinois, Brujeria Chicago, Brujeria en Chicago, Brujos Buenos En Chicago, Brujos Chicago Illinois, Los Mejores Brujos Chicago, Brujos Expertos En Chicago, Amarres de amor Chicago, Amarres De Amor En Chicago, Amarres De Amor Chicago IL, Expertos Amarres De Amor En Chicago, Amarres De Amor En IL, Los Mejores Amarres De Amor En Chicago, Amarres Chicago, Amarres 24 horas chicago, Ritual Abrecaminos Chicago, Ritual Abrecaminos Chicago, Ritual Abrecaminos Chicago Il, Ritual Abrecaminos Chicago Illinois, El Mejor Ritual Abrecaminos Chicago, Ritual Abrecaminos Cerca de Mi, Expertos en Ritual abrecaminos en Chicago, Limpieza espiritual Chicago, Limpia Espiritual Chicago, Limpieza Espirituales en Chicago Il, Limpieza Espiritual en Chicago Illinois, La mejor Limpieza Espiritual en Chicago, Limpieza Espiritual Cerca de Mi, Limpias y Barridas Chicago, Limpias y Barridas en Chicago, Limpias y Barridas  Chicago Il, Limpias y Barridas en Chicago Illinois, Las mejores Limpias y Barridas en Chicago, Limpias y Barridas Cerca de Mi, Limpieza espiritual para negocios Chicago, Limpia Espiritual para negocios Chicago, Limpieza Espiritual para negocios en Chicago Il, Limpieza  Espiritual para negocios en Chicago Illinois, La mejor Limpieza  Espiritual para negocios en Chicago, Limpieza Espiritual para negocios Cerca de Mi, Limpieza espiritual del Hogar Chicago, Limpieza espiritual del Hogar en Chicago, Limpieza espiritual del Hogar en Chicago Il, Limpieza espiritual del Hogar  en Chicago Illinois, La mejor Limpieza espiritual del Hogar en Chicago, Limpieza espiritual del Hogar Cerca de Mi, Endulzamientos de amor Chicago, Chicago Endulsamiento de Amor, Endulzamiento de amor en Chicago Il, Endulzamientos de amor Chicago Illinois, los mejores Endulzamientos de amor en Chicago , Endulzamiento de Amor Cerca de Mi, Lectura del tarot Chicago, Lectura del tarot en Chicago, Lectura del tarot Chicago IL, Expertos en Lectura del tarot en Chicago, Lectura del tarot en IL, la mejor Lectura del tarot en Chicago, lectura de cartas Chicago, lectura de cartas cerca de mi, Curacion espiritual Chicago, Curacion espiritual en Chicago, Curacion espiritual Chicago IL, Expertos en Curaciones espirituales en Chicago, Curacion espiritual en IL, La mejor Curacion espiritual en Chicago, Union de parejas Chicago, Union de parejas Chicago, Union de parejas cerca de mi, Union de parejas en Chicago Illionis, Union de parejas en Chicago Il, La mejor union de parejas en Chicago, Dominios de amor Chicago, Dominios de Amor Chicago, Dominios de Amor Chicago Il, Dominios de amor Chicago Illinois, Los mejores Dominios de Amor en Chicago, Dominios de Amor Cerca de Mi, Hechizos de amor Chicago, Hechizos de amor Chicago, Hechizos de amor Chicago Il, Hechizos de amor Chicago Illinois, Los mejores Hechizos de amor en Chicago, Hechizos de amor Cerca de Mi',
        'latitud': '41.84766294762597',
        'longitud': '-87.7048978741096'
    },
    {
        'ruta': r"C:\Carpeta entrada y salida\Salida de imagen\BOTANICA VIRGEN MORENA",
        'descripcion': 'En Virgen Morena, cuento con lo más poderozos rituales que podrán ayudarte a recuperar ese amor que alguna vez se fue. ¡Yo te podré ayudar a ser feliz junto tu ser amado nuevamente! Cuento con una amplia experiencia en la ciudad de Chicago, realizando amarres de amor, hechizos, amarres, rituales abre caminos, limpias y barridas espirituales, dominio, brujeria y otros servicios más. Contamos con todas las capacidades, preparación y experiencia necesaria para llevar a cabo cualquier servicio que necesite. Somos expertos en el mundo del esoterismo con los cuales le ayudaremos a solucionar todos los problemas de amor que necesite. Encuentranos en Chicago Illinois',
        'titulo': ' ',
        'etiquetas': 'Santeria Botanica Chicago, Santeria Botanica Chicago, Santeria Botanica Chicago Illinois, Chicago Santeria Botanica, Santeria Botanica Chicago, Santeria Botanica Chicago cerca de mi, la mejor Santeria Botanica Chicago, Amarres de amor gay chicago, Amarres de amor gay en Chicago, Amarres de amor gay Chicago IL, Los mejores amarres de amor Gay en Chicago, Amarres de amor gay Illinois, Brujeria Chicago, Brujeria en Chicago, Brujos Buenos En Chicago, Brujos Chicago Illinois, Los Mejores Brujos Chicago, Brujos Expertos En Chicago, Amarres de amor Chicago, Amarres De Amor En Chicago, Amarres De Amor Chicago IL, Expertos Amarres De Amor En Chicago, Amarres De Amor En IL, Los Mejores Amarres De Amor En Chicago, Amarres Chicago, Amarres 24 horas chicago, Ritual Abrecaminos Chicago, Ritual Abrecaminos Chicago, Ritual Abrecaminos Chicago Il, Ritual Abrecaminos Chicago Illinois, El Mejor Ritual Abrecaminos Chicago, Ritual Abrecaminos Cerca de Mi, Expertos en Ritual abrecaminos en Chicago, Limpieza espiritual Chicago, Limpia Espiritual Chicago, Limpieza Espirituales en Chicago Il, Limpieza Espiritual en Chicago Illinois, La mejor Limpieza Espiritual en Chicago, Limpieza Espiritual Cerca de Mi, Limpias y Barridas Chicago, Limpias y Barridas en Chicago, Limpias y Barridas  Chicago Il, Limpias y Barridas en Chicago Illinois, Las mejores Limpias y Barridas en Chicago, Limpias y Barridas Cerca de Mi, Limpieza espiritual para negocios Chicago, Limpia Espiritual para negocios Chicago, Limpieza Espiritual para negocios en Chicago Il, Limpieza  Espiritual para negocios en Chicago Illinois, La mejor Limpieza  Espiritual para negocios en Chicago, Limpieza Espiritual para negocios Cerca de Mi, Limpieza espiritual del Hogar Chicago, Limpieza espiritual del Hogar en Chicago, Limpieza espiritual del Hogar en Chicago Il, Limpieza espiritual del Hogar  en Chicago Illinois, La mejor Limpieza espiritual del Hogar en Chicago, Limpieza espiritual del Hogar Cerca de Mi, Endulzamientos de amor Chicago, Chicago Endulsamiento de Amor, Endulzamiento de amor en Chicago Il, Endulzamientos de amor Chicago Illinois, los mejores Endulzamientos de amor en Chicago , Endulzamiento de Amor Cerca de Mi, Lectura del tarot Chicago, Lectura del tarot en Chicago, Lectura del tarot Chicago IL, Expertos en Lectura del tarot en Chicago, Lectura del tarot en IL, la mejor Lectura del tarot en Chicago, lectura de cartas Chicago, lectura de cartas cerca de mi, Curacion espiritual Chicago, Curacion espiritual en Chicago, Curacion espiritual Chicago IL, Expertos en Curaciones espirituales en Chicago, Curacion espiritual en IL, La mejor Curacion espiritual en Chicago, Union de parejas Chicago, Union de parejas Chicago, Union de parejas cerca de mi, Union de parejas en Chicago Illionis, Union de parejas en Chicago Il, La mejor union de parejas en Chicago, Dominios de amor Chicago, Dominios de Amor Chicago, Dominios de Amor Chicago Il, Dominios de amor Chicago Illinois, Los mejores Dominios de Amor en Chicago, Dominios de Amor Cerca de Mi, Hechizos de amor Chicago, Hechizos de amor Chicago, Hechizos de amor Chicago Il, Hechizos de amor Chicago Illinois, Los mejores Hechizos de amor en Chicago, Hechizos de amor Cerca de Mi',
        'latitud': '41.844438928654014',
        'longitud': '-87.7047041772723'
    },
    {
        'ruta': r"C:\Carpeta entrada y salida\Salida de imagen\CASH DEALS TODAY",
        'descripcion': 'We specialize in helping homeowners sell their homes for cash, securely and quickly, all across the United States. Our team in Chicago of experts is dedicated to providing you with the best possible experience, ensuring that you get the most value for your property. So why wait? Sell your home for cash with us today!',
        'titulo': ' ',
        'etiquetas': 'we buy houses in chicago, cash home buyers in chicago, sell my house fast chicago, cash buyers Chicago, Chicago cash home buyers, companies that buy houses for cash near me, cash buyers near me, cash home buyers near me, real estate cash buyers near me, we buy home for cash',
        'latitud': '41.877598439904915',
        'longitud': '-87.63996559956378'
    },
    {
        'ruta': r"C:\Carpeta entrada y salida\Salida de imagen\ELITE CHICAGO SPA",
        'descripcion': 'At Elite Chicago Spa, you can find the best solutions to all your skin problems or fat accumulated in your body. With Elite Chicago Spa, you can have the body or the look you want, because we have the best procedures approved by the FDA.In our catalog you can find a variety of the best treatments for both skin and fat accumulated as Detox, Microneedling, Coolsculpting, Liposonix HIFU, Yoni Steam Cleanse, Lip Fillers, Glow Facial, Nano Needling, among others that are designed to meet the needs of our customers in Chicago.',
        'titulo': ' ',
        'etiquetas': 'Spa in Chicago, the best spa in Chicago, spa Chicago Illinios, Chicago Spa, Spa near me, Medspa in Chicago, Carboxytherapy in Chicago, Chicago Carboxitherapy, Carboxitherapy in Chicago Il, Carboxitherapy in Chicaho Illinois, The best Carboxitherapy in Chicago, Carboxitherapy near me, coolsculpting chicago, Coolsculpting chicago, Coolsculpting Clinic in Chicago, Coolsculpting Doctor in Chicago,coolsculpting in Chicago Illinois,Best Coolsculpting Chicago, Coolsculpting Near me, Ultrasonic Cavitation in Chicago, Chicago Ultrasonic Cavitation, ultrasonic cavitation near me, Cavitation Treatment in Chicago, cavitation treatment near me, Best Ultrasonic Cavitation in Chicago, body cavitation treatment near me, cavitation chicago, Facials Chicago, Facials in Chicago, Facials Chicago IL, Facials Chicago Illinois, the best facials in chicago, facials near me, Glow Facial Chicago, Glow Facial in Chicago, Glow Facial Chicago Illinois, Glow Facial near me, the best glow facial chicago, Dermaplaning Chicago, Dermaplaning Chicago, Dermaplaning in Chicago, Dermaplaning Chicago IL, Dermaplaning Illinois, Dermaplaning near me, The best dermaplaning chicago, dermaplane with peel in chicago, dermaplaning facial in chicago',
        'latitud': '41.95403011638448',
        'longitud': '-87.6643714490458'
    },
    {
        'ruta': r"C:\Carpeta entrada y salida\Salida de imagen\ELITE FRENCHIES",
        'descripcion': 'At Elite Frenchies we have the best and most exotic Frenchies for sale in Chicago, IL, which have the best physical and aesthetic characteristics, making them totally unique French Bulldogs. With us you can be totally sure that the Frenchie you choose, will be of the highest quality possible, because here we have the best French Bulldog couples, with an AND quality certified by the AKC.',
        'titulo': ' ',
        'etiquetas': 'Fluffy Frenchie for sale Chicago, french bulldog breeders Chicago, frenchies for sale Chicago, frenchies for sale Los Angeles, french bulldogs for sale Chicago, french bulldogs stud Chicago, Fluffy Frenchie for sale, Fluffy French Bulldogs for sale, frenchies for sale, Fluffy Frenchie for sale USA, exotic frenchies for sale, exotic french bulldogs stud services, french bulldog breeders Chicago, exotic french bulldogs for sale, french bulldogs stud services',
        'latitud': '41.844280867197256',
        'longitud': '-87.7033847772517'
    },
    {
        'ruta': r"C:\Carpeta entrada y salida\Salida de imagen\EXPRESS CLEAN",
        'descripcion': 'At Express Clean we have always helped those who need a cleaning service for their home, apartment, business or office. We have more than 10 years of experience, which makes us your best choice when you need a cleaning service in Chicago . We have a wide catalog of cleaning services in Chicago, Illinois . Where you can find the best Airbnb Cleaning Services, Apartment Cleaning, House Cleaning, Moving Cleaning and Same Day Cleaning, but in addition to this we have the best Event Cleaning, Office Cleaning and Restaurant Cleaning . All these services are designed to give you an excellent cleaning experience.',
        'titulo': ' ',
        'etiquetas': 'Aurora Apartment Cleaning, Aurora Illinois Apartment Cleaning, Best Apartment Cleaning Aurora, Apartment Cleaning Near Me, Aurora Office Cleaning, Office Cleaning Aurora Il, Best Office Cleaning Aurora, Office Cleaning Aurora near me, Aurora Cleaning Service, Cleaning Services Aurora, Cleaning Service in Aurora IL, Best Cleaning Service In Aurora, Cleaning service near me, Cleaning Service Chicago IL, Cleaning Service Illinois, Cleaning Service in chicago, Best Chicago Cleaning Service',
        'latitud': '41.84442723563825',
        'longitud': '-87.727523346538'
    },
    {
        'ruta': r"C:\Carpeta entrada y salida\Salida de imagen\LOPEZ Y LOPEZ ABOGADOS",
        'descripcion': 'En nuestro Bufete de Abogados en Bogotá Lopez & Lopez, cuenta con los más experimentados profesionales los cuales están dispuestos a brindar asesorías jurídicas de la más alta calidad. En Lopez & Lopez contamos con los mejores Abogados en Bogotá con excelentes referencias, expertos en la materia, accesibles y honrados. Ofrecemos una amplia gama de servicios en diversas áreas legales. Estos incluyen Derecho Penal, Derecho Laboral, Derecho Tributario, Derecho Civil, Derecho de Familia, Derecho Administrativo y Derecho Comercial. Puedes contar con nosotros para obtener asesoramiento y representación en cualquiera de estas áreas según tus necesidades específicas.',
        'titulo': ' ',
        'etiquetas': 'derecho penal, derecho laboral, derecho tributario, derecho civil, derecho de familia, derecho administrativo, derecho comercial',
        'latitud': '4.608202173944595',
        'longitud': '-74.14332542979223'
    },
    {
        'ruta': r"C:\Carpeta entrada y salida\Salida de imagen\OSCEOLA",
        'descripcion': 'At Osceola Fence, we have over 40 years of experience providing the highest quality fence for businesses and properties in Chicago and surrounding areas. If you need it, OSCEOLA offers a wide variety of services such as Industrial Fence, Automatic Gates, Chain Link Fence, Wood Fence, Vinyl Fence and others that are designed to meet the needs of our customers.',
        'titulo': ' ',
        'etiquetas': 'Chicago Fence Company, Chicago Illinois fence company, best fence company chicago, fencing companies chicago, Commercial Fence Installation Chicago, Chicago Commercial Fence Installation, Commercial Fence Installation in Chicago Il, Commercial Fence Installation in Chicago Illinois, Best Commercial Fence Installation, Commercial Fence Installation Near me, Commercial Fence Contractors, industrial fences, Automatic Gates Chicago, Automatic Security Gates Chicago, Automatic Security Gates in chicago, Automatic Security Gates Illinois, Automatic Security Gates Chicago IL, Chicago Automatic Security Gates, automatic gate installation chicago, electric gate systems chicago, gate operator chicago, electric gate system chicago, electric gates chicago, Iron Railing, commercial railings chicago, commercial railings chicago illinois, commercial railing chicago IL, Residential Fences, wrought iron fence near me, wrought iron fence panel, wrought iron fence designs, wrought iron fence designs, wrought iron fence in chicago, Chain Link, Chicago chain link fence, Best Chain Link Fences in Chicago, Chicago chain link fence installation, Residential Services Chicago',
        'latitud': '41.9159036598422',
        'longitud': '-87.75441179525404'
    },
    {
        'ruta': r"C:\Carpeta entrada y salida\Salida de imagen\QUICK CLEANING",
        'descripcion': 'At Quick Cleaning, we have a long history of assisting individuals and businesses in need of cleaning services for their homes, apartments, companies, or offices. With a solid decade of experience, we have proven our expertise helping individuals and businesses with top-notch cleaning services for homes, apartments, businesses, and offices. Our established history in Chicago makes us the ideal choice for all of your cleaning needs. As a result, we have become a trusted name in the cleaning industry, known for our dependability, efficiency, and commitment to ensuring spaces are spotless and welcoming. Whether it is a residential space or a commercial establishment, you can trust Quick Cleaning to exceed your expectations and leave your environment looking its best.',
        'titulo': ' ',
        'etiquetas': 'cleaning services chicago, Cleaning Service Chicago IL, Cleaning Service Illinois, Cleaning Service in chicago, Best Chicago Cleaning Service, Cleaning Service Near Me, house cleaning chicago, Chicago Cleaning Service, Cleaning Company Chicago, Cleaning Service in Chicago, same day cleaning chicago, maid service chicago, maid services in chicago, chicago maids, best maid service in chicago, maid company chicago, chicago maid service, maid services near me, chicago maid services, Maid service chicago IL, Maid service chicago illinois, apartment cleaning chicago, apartment cleaning services in Chicago, apartment cleaning services near me, apartment cleaning services prices, apartment cleaning companies in Chicago, apartment cleaning services chicago, apartment cleaning company Chicago, Chicago Apartment Cleaners, Airbnb Cleaning Service Chicago, Airbnb Cleaning Services Chicago Il Airbnb Cleaning Services Chicago Illinois, Chicago Airbnb Cleaning Services, Best Airbnb Cleaning Services, Airbnb Cleaning Services Near Me, Move Out Cleaning Chicago, Cleaning movers in Chicago Il, Moving Cleaning in Chicago Illinois, The Best Moving Cleaning Service in Chicago, Moving Cleaning Near me, Chicago Moving Cleaning, Office Cleaning Chicago, Chicago Office Cleaning, Office Cleaning Chicago Il, Office Cleaning Chicago Illinois, Best Office Cleaning Chicago, Office Cleaning near me, 24 Hour Cleaning Service Chicago, Event Cleaning Services Chicago, Chicago Event Cleaning Services, Post Event Cleaning Services Chicago, Commercial Cleaning Services Chicago, Chicago Commercial CleaningServices, Best Commercial Cleaning Services Chicago,  Commercial Cleaning Services Near Me',
        'latitud': '41.84444242421529',
        'longitud': '-87.70470567627932'
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
busquedas = [
#BOTANICA AMARRES DE AMOR
    ['raton', 'comida'],#AMARRES DE AMOR
    ['gatos', 'perros'],#AMULETOS PREPARADOS
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
    ['', ''],#LECTURA DE CARTAS
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
#QUICK CLEANING - RESIDENCIAL
    ['', ''],#AIRBNB CLEANING
    ['', ''],#APARTAMENT CLEANING
    ['', ''],#DEEP CLEANING SERVICES
    ['', ''],#HOUSE CLEANING
    ['', ''],#MAID CLEANING SERVICES
    ['', ''],#MAID SERVICES
    ['', ''],#MOVE OUT CLEANING
    ['', ''],#POST CONSTRUCTION CLEANING
    ['', ''],#RENTAL PROPERTY CLEANING SERVICES
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
    def modify_metadata(ruta_archivo, metadata):
        nueva_descripcion = metadata.get('descripcion', '')
        nuevo_titulo = metadata.get('titulo', '')
        nuevas_etiquetas = metadata.get('etiquetas', '')
        nueva_latitud = metadata.get('latitud', '')
        nueva_longitud = metadata.get('longitud', '')

        # Dividir las etiquetas en una lista
        etiquetas_lista = nuevas_etiquetas.split(', ')

        # Construir una lista de argumentos para Keywords
        keywords_args = ['-Keywords=' + etiqueta for etiqueta in etiquetas_lista]

        # Modificar metadatos con ExifTool para el archivo
        command = [
            exiftool_path,
            '-ImageDescription=' + nueva_descripcion,
            '-Title=' + nuevo_titulo,
            *keywords_args,  # Usar el operador * para desempaquetar la lista de argumentos
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
def descargar_imagenes_pexels():
    api = PexelsAPI()
    numero_carpeta=0
    while numero_carpeta < len(busquedas):
        palabras_clave = busquedas[numero_carpeta]

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
