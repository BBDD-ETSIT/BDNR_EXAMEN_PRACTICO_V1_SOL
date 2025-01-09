<img  align="left" width="150" style="float: left;" src="https://www.upm.es/sfs/Rectorado/Gabinete%20del%20Rector/Logos/UPM/CEI/LOGOTIPO%20leyenda%20color%20JPG%20p.png">
<img  align="right" width="60" style="float: right;" src="http://www.dit.upm.es/figures/logos/ditupm-big.gif">


<br/><br/>


# Exámen Práctico de ODM con PYTHON-FLASK y MONGOENGINE

## 1. Dependencias

Para realizar la práctica el alumno deberá tener instalado en su ordenador:
- Herramienta GIT para gestión de repositorios [Github](https://git-scm.com/downloads)
- Entorno de ejecución de Python 3 [Python](https://www.python.org/downloads/)
- Base de datos MongoDB [MongoDB](https://www.mongodb.com/try/download/community)
- Base de datos [Fuseki](https://jena.apache.org/documentation/fuseki2/)

## 2. Descripción del examen 

El exámen utiliza como revusro base la práctica de ODM y SPARQL de la asignatura. Para ello se especifican las instrucciones necesarias para arrancar el entorno en el punto 3.

A diferencia de la práctica, esta aplicación incluye un desarrollo parcial  del código necesario para mostrar la información sobre un conjunto de productoras de películas. Se incluye un conjunto de datos de productoras que deben ser guardados en mongoDB por medio del uso de seeders. 

El estudiante debe a partir de el conjunto de datos de entrada desarrollar lo siguiente:

Las clases dentro del fichero `models.py` para poder generar el modelo Production, que mapeará el documento de porductoras en la base de datos.

Las funciones dentro del controlador de productoras, alojadas en el fichero `productionCOntroller.py`. Un vez implementado aquello, se debería poder visualizar la información de todas las productoras, con información estendida de un productora individual. Asímismo se debe implementar las funciones para poder realizar un firltrado de las productoras dado un rango de galardones obtenidos por ellas.


## 3. Descargar e instalar el código del proyecto

Abra un terminal en su ordenador y siga los siguientes pasos.

Clone el repositoro de GitHub
```
git clone https://github.com/BBDD-ETSIT/BDNR_EXAMEN_PRACTICO_V1.git
```

Navegue a través de un terminal a la carpeta BDNR_EXAMEN_PRACTICO_V1.
```
BDNR_EXAMEN_PRACTICO_V1
```

Una vez dentro de la carpeta, se instalan las dependencias. Para ello debe crear un virtual environment de la siguiente manera:

```
[LINUX/MAC] > python3 -m venv venv
[WINDOWS] > py.exe -m venv env
```

Si no tiene instalado venv, Lo puede instalar de la siguiente manera:

```
[LINUX/MAC] > python3 -m pip install --user virtualenv
[WINDOWS] > py.exe -m pip install --user virtualenv
```

Una vez creado el virtual environment lo activamos para poder instalar las dependencias:

```
[LINUX/MAC] > source venv/bin/activate
[WINDOWS] > .\env\Scripts\activate
```

Instalamos las dependencias con pip:

```
pip3 install -r flaskr/requirements.txt 
```

En un terminal distinto a donde se está ejecutando la aplicación, ejecutar los seeders para llenar la base de datos con los datos iniciales:
```
mongoimport -d moviesbdnr -c user --file ./flaskr/seeders/user.json --jsonArray
mongoimport -d moviesbdnr -c movie --file ./flaskr/seeders/movie.json --jsonArray
mongoimport -d moviesbdnr -c production --file ./flaskr/seeders/production.json --jsonArray
```

Comprobar que los datos han sido guardados en cada una de las colecciones. Para ello, se debe usar la mongo shell para conectarse a la bbdd y realizar un find en cada una de las colecciones.

Ahora podemos arrancar el servidor con el siguiente comando (Debemos tener arrancado MongoDB):

```
flask --app ./flaskr/run.py  run --debug
```

Abra un navegador y vaya a la url "http://localhost:5000" para ver la aplicación.

Si necesita arrancar la aplicación en un puerto diferente al predeterminado puede usar el siguiente comando (reemplazando el 5002 por el puerto correspondiente):

```
flask --app ./flaskr/run.py  run --debug --port=5002
```

> [!NOTE]  
> Si ha modificado algun documento de manera indeseada y se quiere volver a restablecer los valores por defecto, borre la base de datos que ha creado, repita los seeders y vuelva a arrancar el servidor con flask.

## 5. Tareas a realizar

La primera tarea es inspeccionar todo el código provisto y entender donde están los modelos, las vistas y los controladores, asi como la semilla o seeders.



### --------------------------------------------

### 5.1 Definir el modelo de Production:
A partir del documento de la productora, completar en el fichero `models.py` las  líneas de código que hagan falta para definir el modelo de Production:

**Production**:

```
{
    "name": "Castle Rock Entertainment",
    "alias": "castle",
    "thumbnail": "https://tinyurl.com/mr2pfp9f",
    "country": "United States",
    "foundation_year": 1987,
    "headquarters": "Burbank, California",
    "CEO": "Martin Shafer",
    "website": "https://www.warnerbros.com/studio/divisions/castle-rock-entertainment",
    "number_of_awards": 14,
    "notable_movies": [
      "Misery",
      "The Green Mile",
      "Seinfeld",
      "The Shawshank Redemption"
    ],
    "contact_info": {
      "address": "4000 Warner Blvd, Burbank, CA 91522",
      "phone": "+1-818-954-3000",
      "email": "info@castlerockent.com"
    }
  }
```
### 5.1 Definir el modelo de User y completar el de Movie:





### 5.2 Rellenar las funciones del cntrolador y producion que interactúan con la base de datos usando los modelos.

Se provee un esqueleto con todas los funciones que deberá rellenar. El alumno deberá editar los ficheros `controllers/productionController.py`

En cada una de estas funciones se debe hacer uso del ODM MongoEngine o de SPARQL para realizar operaciones con la base de datos y devolver un resultado de la operación.

Se debe completar cada una de las funciones de dicho controlador para `controllers/movieController.py` tenemos:

### read_productions()

**Descripción:**  Extrae por medio del model de productoras la lista de todas las productoras almacenadas en la base de datos

**Returns:** Un objeto productions con llista de todas las productoras

### read_production(alias)
**Descripción:**  Muestra la información de una productora dado su alias

**Parametros:** alias

**Returns:** Objeto production con los datos de la productora

():
### read_productions_by_filter

**Descripción:**  Muestra una lista de productoras filtradas por un rango de galardones obtenidos.

**Parametros:** min_number_of_awards, max_number_of_awards

**Restricciones:** el filtrado se debe realizar considerando valores a mayores o iguales a un número x y menores o iguales a un número y

**Returns:** Un objeto productions con la lista de las productoras que cumplen con el filtro.


-------------
### Consulta SPARQL en `read_movie()`


### read_movie()

**Descripción:**  Muestra la información de una película usando SPARQL

**Parametros:** slug

**Returns:** Un objeto movie

### Consulta SPARQL en `read_movie()`

Las tareas principales en este apartado son:

- Modificar el código de la consulta para que la página de una película incluya al menos 5 campos adicionales obtenidos mediante SPARQL a wikidata
- Generar un nuevo fichero de seed con más películas utilizando una consulta SPARQL a wikidata (`extra_movies.json`)
- Descargar toda la información necesaria para las consultas a un fichero `movies.ttl`

Para que la información recogida con SPARQL se muestre en la página web, deberemos añadir el atributo `extra` al objeto película antes de devolverlo en la función `read_movie`.
Para ello, haremos uso de la función `query` del módulo `sparql` presente en el proyecto flaskr.
Esta función envía la consulta SPARQL que pidamos y devuelve los como una lista de diccionarios, donde cada elemento es una fila, cuyas claves son los nombres de las columnas y el valor es la celda correspondiente en esa fila.

Este es un ejemplo de uso para capturar información sobre el país del que es la película:

```python
movie.extra = query('''
    SELECT (?country as ?Pais)
    WHERE {{
      <{uri}> wdt:P495 ?origin .
      ?origin rdfs:label ?country .
      FILTER(lang(?country) = "es")
    }}
    LIMIT 1
    '''.format(uri=movie.uri))
```

> [!WARNING]  
> Las consultas se construyen mediante una f-string en Python, por lo que para incluir llaves (`{` y `}`) en la consulta deberemos escaparlas usando una doble llave (`{{` y `}}`, respectivamente).

Para generar el nuevo fichero seeder de películas, es necesario generar una consulta que devuelva la información necesaria para el seed: título, imagen, lista de actores, director(es), fecha de estreno, etc.
Para esta tarea, se recomienda generar un fichero `generar_seeder.py` que genere una lista de películas haciendo varias consultas SPARQL a wikidata.

Por último, para descargar la información necesaria para generar `movies.ttl` tenemos varias alternativas:

* Descargar toda la información de cada película usando wikidata. Esta es la opción más sencilla, pero incluye información que puede no interesarnos.
* Utilizar `rdflib` para construir un grafo y añadir las triplas necesarias usando consultas SPARQL a wikipedia para cada una de las películas. Esta es la opción más flexible, pero requiere utilizar rdflib y un pequeño código python.
* Utilizar una única consulta SPARQL `CONSTRUCT`, que devuelve el resultado como un grafo (p.e., `ttl`). Esta es la opción más rápida, pero requiere tener un buen dominio de SPARQL para generar una única consulta SPARQL.
* Utilizar una consulta `CONSTRUCT` para cada película y unir los resultados 

### --------------------

### 5.4 Manejo de Concurrencia. 

En este apartado se plantean las tareas que van a permitir manejar la concurrencia para esta aplicación.

> [!WARNING]  
> Este apartado estará disponible cuando se haya cubierto el tema de concurrencia en clase.


## 6. Instrucciones para la Entrega y Evaluación.

> [!NOTE]  
> Se han includo una suite de tests para determinar si se han implementado de forma correcta cada una de las funciones y obtener una nota orientativa de acuerdo a la rúbrica.

**RÚBRICA**: Cada método que se pide resolver de la practica se puntuará de la siguiente manera:
-  **0.5 puntos por crear los Modelos solicitados en el punto 5.1**
-  **0.5 puntos por añadir la imagen de favoritos a la vista de la película, lo indicado en el punto 5.3**
-  **1 punto** por capturar la información adecuada en la Consulta SPARQL en `read_movie()`.
-  **0.5 puntos por cada uno de las siguientes funciones realizadas:**  `list_movies_by_filter`, `list_users` y `read_user`
-  **1 puntos por cada uno de las siguientes funciones realizadas:**   `create_user` y `update_user`
-  **1.5 puntos** por la función `add_favorite_movie_to_user`, `remove_favorite_movie_from_user` y `create_review`.
