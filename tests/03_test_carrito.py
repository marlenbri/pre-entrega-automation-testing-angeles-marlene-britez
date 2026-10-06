from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import login, captura_error
import time

def test_interaccion_con_carrito():
 try: 
   options = Options()
   options.add_argument('--start-maximized')
   driver = webdriver.Chrome(options=options)
   
   login(driver)
   #Validaciones del login exitoso
   assert "inventory.html" in driver.current_url
   assert driver.title == "Swag Labs"
      
   #Añadir un producto al carrito
   boton_add_carrito = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']")
   boton_add_carrito.click()

   #Validar que el carrito se actualice correctamente.
   cart = driver.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')
   assert cart.get_attribute("aria-label") == "Cart, 1 items"
      
   #Ir al carrito
   cart.click()
      
   #Validar que el producto añadido esté en el carrito con su nombre correcto.
   WebDriverWait(driver,10).until(EC.url_contains("/cart.html"))
   producto_en_carrito = driver.find_element(By.CLASS_NAME, "inventory_item_name")
   assert producto_en_carrito.text == "Sauce Labs Bike Light"

   #Validar precio del producto que se encuentra en el carrito.
   precio_producto_en_carrito = driver.find_element(By.CLASS_NAME, "inventory_item_price")
   assert precio_producto_en_carrito.text == "$9.99"
    
 except Exception:
  captura_error(driver, "test_interaccion_con_carrito")
  raise

 finally:
  time.sleep(5)
  driver.quit()