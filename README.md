# Tarea de Consulta de Tipo de Cambio

## Estudiante: David Arturo Brenes Angulo

¡Bienvenido! Este es un proyecto simple para consultar el tipo de cambio de compra y venta del Banco Central de Costa Rica (BCCR) para una fecha específica. Utilizamos Flask para el backend, Zeep y lxml para consumir un servicio web.

## Requisitos

- Python 3.x
- Flask
- Zeep
- lxml

## Instalación

1. Clona este repositorio:

    ```bash
    git clone https://github.com/tu_usuario/Tarea2_david.git
    cd Tarea2_david
    ```

2. (Opcional) Crea y activa un entorno virtual para mantener las dependencias organizadas:

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3. Instala las dependencias necesarias:

    ```bash
    pip install -r requirements.txt
    ```

## Cómo Ejecutar

1. Asegúrate de estar en el entorno virtual si estás usando uno.

2. Ejecuta la aplicación:

    ```bash
    python run.py
    ```

3. Abre tu navegador y ve a [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Estructura del Proyecto

(app):
- (static):
- css:
- style.css
- (templates):
- index.html
- result.html
- error.html
- init.py
- routes.py

    -accesoDatos.py
    -entidades.py
    -logicaNegocio.py
    -run.py 


### Descripción de Archivos

- **app/__init__.py**: Configuración de la aplicación Flask.
- **app/routes.py**: Define las rutas y la lógica principal.
- **app/static/css/style.css**: Estilos CSS para la página web.
- **app/templates/index.html**: Plantilla HTML principal.
- **app/templates/result.html**: Plantilla HTML para mostrar resultados.
- **app/templates/error.html**: Plantilla HTML para mostrar errores.
- **accesoDatos.py**: Se comunica con el servicio web y maneja el acceso a datos.
- **entidades.py**: Define la entidad ExchangeRate.
- **logicaNegocio.py**: Maneja la lógica de negocio para obtener los tipos de cambio.
- **run.py**: Script para iniciar la aplicación.

## Uso

1. Ve a [http://127.0.0.1:5000/](http://127.0.0.1:5000/) en tu navegador.
2. Selecciona una fecha y haz clic en "Consultar".
3. Verás el tipo de cambio de compra y venta para la fecha seleccionada.

## Solución de Problemas

- **Problemas con dependencias**: Asegúrate de instalar todo correctamente con `pip install -r requirements.txt`.
- **Error al consultar el servicio web**: Verifica que tienes conexión a internet y que el servicio web del BCCR está disponible.

## Autor

David Arturo Brenes Angulo


