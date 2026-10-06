from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver, username="standard_user", password="secret_sauce"):
    """Realiza el login en Sauce Demo con credenciales por defecto."""
    driver.get("https://www.saucedemo.com")

    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    # Espera explícita para confirmar login exitoso
    WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))


import os
import time

def captura_error(driver, nombre_test):
    """Guarda una captura de pantalla en caso de fallo."""
    carpeta = "reports/screenshots"
    os.makedirs(carpeta, exist_ok=True)

    timestamp = time.strftime("%Y%m%d-%H%M%S")
    ruta = f"{carpeta}/{nombre_test}_{timestamp}.png"

    driver.save_screenshot(ruta)

def captura_ok(driver, nombre_test):
    carpeta = "reports/screenshots"
    os.makedirs(carpeta, exist_ok=True)

    ruta = f"{carpeta}/{nombre_test}_OK.png"
    driver.save_screenshot(ruta)


