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

El resultado debiera indicar un número superior a 3.
Luego de clonar el repositorio y para instalar las dependencias debe ejecutar el comando `pipenv stall`.

## Migraciones
Para ejecutar las migraciones el comando es el siguiente:

```
flask db upgrade
```

En caso de modificar un Modelo agregando o modificando un atributo, debemos generar una nueva migración, con el comando:

```
flask db migrate -m "mensaje de la migración"
```

**nota**: Los comandos anteriores se deben ejecutar dentro de `pipen shell`

## Levantando la aplicación
Para ejecutar el servidor de desarrollo el comando es el siguiente:
```
flask --app app --debug run
```

