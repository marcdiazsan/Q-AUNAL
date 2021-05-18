#NOTA SOBRE EL FRONT
En este momento esta corriendo de forma independiente al back. Estoy corriendo APIQueue.py como back en el localhost, en el puerto 5000. El front esta corriend en el localhost, puerto 8000, y haciendo llamadas a este back. Para correr el front, se usa API.py que esta en src/frontEnd.

Como nota adicional, para poder hacer llamadas a este back (y a cualquier otro si se mantiene separado front y back) es necesario modificar el CORS del back. La ruta /preguntas del back muestra como se encuentra esta modificacion, es necesario usar la libreria flask-cors y agregarle los headers tal y como se muestra en esta ruta



# Proyecto Q&A - Estructuras de Datos G2
Este proyecto pretende crear una aplicacion web propia de la Universidad Nacional, en la cual se puedan crear preguntas y contestarlas.

Dentro de este repositorio se encuentran los directorios:

#### src
Carpeta en la que se se incluyen los codigos de codigo fuente del proyecto. Se incluyen los codigos asociados a las estructuras probadas y los codigos asociados al despliegue de la plataforma como rest API, y su respectiva conexion con la consola, como primera entrega de este proyecto.

#### docs 
En esta carpeta contiene los documento de desarrollo del proyecto tal como
* **Documento definicion del proyecto** 
* **Presentacion de direccion del proyecto**
* **Video de presentacion de la aplicacion en funcionamiento**

#### data
En esta carpeta se encuentran contenidos los datos de prueba de la aplicacion, 10 mil, 100 mil y un millon de datos. El .json de un millon de datos, se encuentra en un drive externo, debido a que es muy grande. 

#### lib
En esta carpeta se encuentra el documento requirement.txt con las librerias necesarias para la ejecucion de este proyecto. Se utiliza el comando pip install requirements.txt


### Integrantes
Los integrantes de este proyecto son:

* **Ana Isabella Goyeneche Fonseca**
* **Edwin Ricardo Sanchez Vargas**
* **Juan Esteban Oviedo Garcia**
* **Julian David Sanchez Sanabria**
* **Maria Camila Diaz Sanchez**
