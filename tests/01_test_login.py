from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import captura_error, captura_ok
import time

def test_login_correcto():
 try: 
   options = Options()
   options.add_argument('--start-maximized')
   driver = webdriver.Chrome(options=options)
   driver.get("https://www.saucedemo.com")
   
   #Ingresar credenciales correctas
   driver.find_element(By.ID,"user-name").send_keys("standard_user")
   driver.find_element(By.ID,"password").send_keys("secret_sauce")
   driver.find_element(By.ID, "login-button").click()

   #Espera explicita hasta que cargue la página de inventario
   WebDriverWait(driver,10).until(EC.url_contains("/inventory.html"))
   
   #Validaciones del login exitoso
   assert "inventory.html" in driver.current_url
   assert driver.title == "Swag Labs"
   
   titulo_inventario = driver.find_element(By.CLASS_NAME, "title")
   assert titulo_inventario.text == "Products"
   #Validar Ok del test
   captura_ok(driver, "test_login_correcto")
 
 except Exception:
   captura_error(driver, "test_login_correcto")
   raise
  
 finally:
  time.sleep(5)
  driver.quit()



