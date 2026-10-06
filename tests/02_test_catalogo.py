from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import login, captura_error
import time

def test_catalogo ():
 try: 
   options = Options()
   options.add_argument('--start-maximized')
   driver = webdriver.Chrome(options=options)
   
   login(driver)

   #Validación del titulo de la página.
   titulo_inventario = driver.find_element(By.CLASS_NAME, "title")
   assert titulo_inventario.text == "Products"

   #Validar que se visualice al menos un producto.
   productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
   assert len(productos) > 0

   #Validar titulo del primer producto 
   titulo_primer_producto = driver.find_element(By.CLASS_NAME, "inventory_item_name")
   assert titulo_primer_producto.text == "Sauce Labs Backpack"

   #Validar precio del primer producto
   precio_primer_producto = driver.find_element(By.CLASS_NAME, "inventory_item_price")
   assert precio_primer_producto.text == "$29.99"

   #Validar que al seleccionar filtro de nombre de producto de Z-A, el primer producto sea el correcto.
   filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")
   filtro.click()
   filtro.find_element(By.XPATH, "//option[@value='za']").click()
   titulo_primer_producto_za = driver.find_element(By.CLASS_NAME, "inventory_item_name")
   assert titulo_primer_producto_za.text == "Test.allTheThings() T-Shirt (Red)"

   #Validar que se pueda añadir al carrito el segundo producto y que el carrito se actualice correctamente.
   boton_add_carrito = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']")
   boton_add_carrito.click()
   cart = driver.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')
   assert cart.get_attribute("aria-label") == "Cart, 1 items"

 except Exception:
     captura_error(driver, "test_catalogo")
     raise
 
 finally:
  time.sleep(5)
  driver.quit()