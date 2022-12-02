# Documentación
Esta es una aplicación Web realizada con el Framework Flask y Bottstrap.
Su próposito es ejemplificar un CRUD utilizando el recurso mensaje.
Los datos se guardan en la base de datos Postgres utilizando Migraciones.
Las dependencias del proyecto se gestionan con Pipenv.

## Dependencias
Para correr este proyecto se necesita previamente tener instalado Phyton3 y su herramienta Pip.
Para revisar si las tiene instalado, debe ejecutar los siguientes comandos:

```
python -V
pip -V
```

El resultado debiera indicar un número superior a 30 o algo así.
Luego de clonar el repositorio y para instalar las dependencias debe ejecutar el comando `pipenv stall`.

## Migraciones
Para ejecutar las migraciones el comando es el siguiente:
Para ejecutar hacia adelante
```
flask db upgrade
```
Para ejecutar hacia atrás
```
flask db downgrade
```
Cuando hacemos algún cambio en un modelo y necesitamos considerar esos cambios también en la base de datos, hay que generar una nueva migración.

```
flask db migrate -m "mensaje de la migración"
```

**nota**: Los comandos anteriores se deben ejecutar dentro de `pipen shell`

## Levantando la aplicación
Para ejecutar el servidor de desarrollo el comando es el siguiente:
```bash
pipenv shell
pipenv install
set FLASK_APP=app
set FLASK_ENV=development
flask run
```
O con la siguiente línea
`pipenv run flask --app app --debug run`

Y si tiene el archivo .env con las variables FLAS_DEBUG=1 y FLASK_APP= app. Sólo debe ejecutar lo siguiente
`flask run`

** nota**: Los comandos anteriores se deben ejecutar dentro de `pipenv shell`

## Blueprint

Los blueprint permiten componer aplicaciones desde componentes pequeños.Cada componente es como una mini aplicación. Permiten crear aplicaciones grandes, pero manteniendo el código y la estructura simple.

## Módulos

Para que los Blueprint estén bien organizados, es mejor trabajarlos como módulos, es decir, que estén dentro de una carpeta. Los módulos se pueden anidar, de hecho, nosotros hicimos el módulo `app` con su respectivo `__init__.py` y dentro tenemos otros módulos como el módulo `messages` que es además un blueprint.

## Tarea 
Crear un nuevo recurso sencillo, sin base de datos, como blueprint bajo a url `/memes` y debe renderiar un html lleno de memes

## MVC (Model-View-Controller)

![MVC](https://cdn.educba.com/academy/wp-content/uploads/2019/04/what-is-mvc-design-pattern.jpg.webp)

Es una arquitectura para separar las responsabilidades en la manipulación de las solicitudes y respuestas. Quien recibe las solicitudes es el Controlador o en flask, las rutas.Los controladores se encargan de revisar que la solicitud cumpla con las características necesarias para entregar una respuesta acorde (que tenga todos los datos). Si el controlador lo permite, se podría opcionalmente, llamar al modelo para obtener o modificar los datos de la BBDD (base de datos). Y finalmente, enviar una respuesta que contenga la presentación de la aplicación. En nuestro caso, la capa de presentación comúnmente conocida como Vistas (views) se llaman Templates.

Por lo tanto, en Flask el MVC podría ser adaptado como MTR (Modelo, Template, Ruta), pero es lo mismo en términos de separar la responsabilidad.
