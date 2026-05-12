## Get Client Secret
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Data import data
import json
import time

class SpotifyGenres:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(data.SPOTIFY_URL)


        print("Inicia sesión manualmente y luego presiona ENTER...")
        input()

        #Obtener las cookies para no volver a iniciar sesión en cada prueba
        cookies = cls.driver.get_cookies()

        with open("cookies_spotify.json", "w") as f:
            json.dump(cookies, f)

        # Cargar cookies
        with open("cookies_spotify.json", "r") as f:
            cookies = json.load(f)

        for cookie in cookies:
            cls.driver.add_cookie(cookie)

        # Refrescar para aplicar sesión
        cls.driver.refresh()

        # Ahora ya estás logueado

    def get_client_secret(self):
        self.driver.get(data.DEVELOPER_DASHBOARD_URL)


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

# Ejecutar
test = SpotifyGenres()

SpotifyGenres.setup_class()

test.get_client_secret()

input("Presiona ENTER para cerrar...")

SpotifyGenres.teardown_class()