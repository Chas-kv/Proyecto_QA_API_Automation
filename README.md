# Automation Web Framework - Playwright & Python

Este proyecto es una suite de pruebas automatizadas para la plataforma **SauceDemo**, diseñada bajo el patrón de diseño **Page Object Model (POM)** para garantizar escalabilidad y mantenimiento.

## 🚀 Tecnologías utilizadas
* **Python 3.8+**
* **Playwright**: Automatización de navegador de última generación.
* **Pytest**: Framework de pruebas y ejecución.
* **Pytest-html**: Generación de reportes técnicos.

## 🏗️ Estructura del Proyecto
* `pages/`: Contiene los selectores y lógica de cada página (Login, Inventory, Checkout).
* `tests/`: Casos de prueba funcionales (Flujo de compra completo, validación de login).
* `pytest.ini`: Configuración global de ejecución y reportes.

## 🛠️ Instalación y Ejecución
1. Clonar el repositorio.
2. Crear entorno virtual: `python -m venv venv`
3. Activar entorno: `.\venv\Scripts\activate` (Windows)
4. Instalar dependencias: `pip install -r requirements.txt`
5. Instalar navegadores: `playwright install chromium`
6. Ejecutar pruebas: `pytest`