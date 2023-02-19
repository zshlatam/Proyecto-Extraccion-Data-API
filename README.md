# Proyecto-Extraccion-Data-API
---
## Índice 

- [Descripción](#descripción)
- [Instalación](#instalación)
- [Uso](#uso)
- [Licencia](#licencia)
- [Próximas caractéristicas](#próximas-caractéristicas)

## Descripción

El proyecto se realiza con el fin de obtener y almacenar datos de una API pública y hacerlos accesibles de manera estructurada para su uso en una aplicación web. La creación del modelo permite almacenar la información de forma persistente y flexible en una base de datos, lo que permite una fácil búsqueda y manipulación de los datos.

El stack de tecnologías usadas en este proyecto son:

1. Django 4
2. Postgre
3. Bootstrap 5

## Instalación

Para su correcta instalación se recomienda:
- Tener instalado Postgre.
- Tener creado la DB y su respectivo Usuario.
- Ejecutar el proyecto en un entorno virtual.

Los comandos para iniciar el proyecto son:

```
# Instala las bibliotecas necesarias
pip install -r requirements.txt

# Ejecuta las migraciones
python manage.py migrate

# Crea el superusuario para ingresar al administrador de Django
python manage.py createsuperuser

# Inicia el proyecto
python manage.py runserver

```


## Uso

El uso es simple, el proyecto se compone de una vista publica, la cual es la raiz `/` donde muestra la tabla con la información recopilada de la API.
Para acceder a el simplemente ingresamos a: `127.0.0.1:8000/`

Para acceder al modo administrador de Django: `127.0.0.1:8000/admin/`

## Resumen de lo realizado

1. Se analiza la información de la API.
2. Se crea un entorno virtual para el proyecto
3. Se crea el proyecto Django `bikesantiago`
4. Se crea la aplicación `estaciones_app`
5. Se importa la biblioteca `psicopg2-binary` para la conexión con Postgre
6. Se configura la conexión de la DB.
7. se crea el modelo `Estaciones` donde guardaremos la información extraida de la API
8. Se crea la vista `estaciones_view`, el cual se encarga de extraer la información de la API en formato JSON para posteriormente compararlo con la información de la DB, en caso que el registro exista, lo actualiza y si no existe lo crea.
9. Se crea la url respectiva de la vista, en este caso al ser solo una vista, se configura en la raiz `/`
10. Se crea el template `estaciones.html`, el cual tiene la tabla donde se visualiza la información extraida.
11. Se configura el administrador Django para acceder a la información del modelo Estaciones y manipularlo.
12. Se realiza la migración del modelo a la DB del proyecto.
13. Se crea el superusuario para el administrador Django
14. Se levanta el proyecto.
15. Accedemos al proyecto: `127.0.0.1:8000/`


## Licencia

Este proyecto está bajo la Licencia MIT.

## Próximas caractéristicas
🔹 Implementar biblioteca django-cron para la actualización de la Data en un horario definido.
