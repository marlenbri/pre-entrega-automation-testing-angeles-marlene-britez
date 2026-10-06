# Pre-entrega Automation Testing – Angeles Marlene Britez

## Propósito del proyecto
Este proyecto automatiza pruebas funcionales del sitio Sauce demo utilizando Python y Selenium.  
El objetivo es validar el correcto funcionamiento de las principales funcionalidades de la aplicación:
- Inicio de sesión: 01_test_login
- Catálogo de productos: 02_test_catalogo
- Interacción con el carrito: 03_test_carrito

La automatización permite detectar errores de forma rápida, repetible y confiable.

---


### Tecnologías utilizadas:
- Python 
- Selenium WebDriver  
- ChromeDriver  
- Pytest  
- pytest-html (para reportes HTML)  

---

### Instalación de dependencias
Asegurarse de tener Python instalado.
Luego instalar las dependencias necesarias:
- Instalar Selenium:
```bash
pip install selenium
```
- Instalar Pytest:
```bash
pip install pytest
```
- Instalar pytest-html (para reportes)
```bash
pip install pytest-html
```

### Ejecución de las pruebas:
#### Ejecutar todos los tests:
```bash
pytest -v
```
#### Ejecutar los test con reporte HTML:
```bash
pytest -v --html=reports/reporte.html
```


---

## Estructura del proyecto

pre-entrega-automation-testing-marlene-britez/
│
├── reports/              # Reportes HTML y capturas
│   ├── reporte.html
│   └── screenshots/
│       └── error.png (ejemplo)
├── tests/                # Casos de prueba automatizados
│   ├── 01_test_login.py
│   ├── 02_test_catalogo.py
│   ├── 03_test_carrito.py
│   └── 04_test_adicionales.py
│
├── utils/                # Funciones auxiliares
│   └── helpers.py
│
└── .gitignore

### Casos de prueba implementados:
01_test_login.py

Validación del flujo de login correcto:
- Ingreso de usuario y contraseña válidos
- Espera explícita hasta la carga del inventario
- Validación de URL y título
- Captura automática OK
- Captura automática ERROR en caso de fallo

02_test_catalogo.py
Validaciones del catálogo:
- Login mediante helper
- Verificación del título “Products”
- Verificación de productos visibles
- Validación de nombre y precio del primer producto
- Aplicación del filtro Z - A
- Validación del producto resultante
- Agregar producto al carrito y validar actualización
- Captura automática ERROR

03_test_carrito.py
Validaciones del carrito:
- Login mediante helper
- Agregar producto al carrito
- Validación del contador del carrito
- Ingreso al carrito
- Validación del nombre y precio del producto agregado
- Captura automática ERROR

04_test_adicionales.py (Son casos de prueba adicionales)
Se agregaron validaciones extra para ampliar la cobertura del módulo de login:
- Validar que el sistema permita iniciar sesión únicamente con credenciales válidas.
- Validar que no permita iniciar sesión sin ingresar contraseña.
- Validar que no permita iniciar sesión sin ingresar usuario.


### Helpers utilizados:
login (driver)
Realiza el login reutilizable para todos los tests.

captura_ok(driver, nombre_test)
Genera una captura cuando el test finaliza correctamente.

captura_error(driver, nombre_test)
Genera una captura automática cuando ocurre una excepción.
Las capturas se guardan en: reports/screenshots/
