# Cómo instalar Portal afiliados en Windows
<p>
Esta guía explica cómo instalar el proyecto Portal Afiliados con Odoo 15 en Windows, así como cómo conectarse a una base de datos Oracle y configurar el entorno para ejecutar el proyecto localmente el cual corresponde Portal Afiliados
</p>

## Instalar Python 

Para instalar Python, siga los siguientes pasos:

1. Descargue la última versión de Python desde el sitio web oficial.
2. Haga doble clic en el archivo descargado para iniciar la instalación.
3. Siga las instrucciones del instalador para completar la instalación

 ### Instalar PIP

1. Abrir la consola o el power Shell
2. ejecutar el sigiente comando

###Clonación del repositorio del proyecto en GitHub

Para clonar el repositorio del proyecto en GitHub, siga los siguientes pasos:

1. Abra la página del repositorio en GitHub.
2. Haga clic en el botón*"Code"* y seleccione*"Clone"*.
3. Copie la URL del repositorio.
4. Abra una línea de comando y escriba *git clone* seguido de la URL del repositorio.
`$ git clone https://github.com/Fenalco/modulos_odoo_fenalco.git`
5. Presione Enter para clonar el repositorio.

###Agregar la ruta del proyecto al archivo de configuracion
Para agregar la ruta del repositorio al archivo *odoo.conf*, siga los siguientes pasos:

1. Abra la carpeta donde se instaló Odoo.
2. Busque el archivo odoo.conf y ábralo con un editor de texto.
3. Busque la línea de *addons_path* en la sección de opciones *[options]*.
4. Agregue la ruta de la carpeta donde clonó el repositorio de GitHub después de una coma *","*.
```python
[options]
addons_path = C:\odoo15\server\odoo\addons,C:\Users\vmartinez\Proyectos Odoo\modulos_odoo_fenalco
```

###Conectar Odoo con una base de datos Oracle
<p>
Para conectar Odoo con una base de datos Oracle, debes utilizar un ORM que traduzca las consultas y comandos de Odoo para que sean compatibles con Oracle. Además, se debe inicializar el cliente de Oracle en la máquina local mediante la librería *cx_Oracle* y la dirección de la ubicación donde se encuentra la librería.
</p>


1. Abre el proyecto con tu IDE de preferencia
2. Ubica la siguiente ruta: *base_external_dbsource_oracle > models > base_external_dbsource.py*
```windows
 C:\Users\vmartinez\Proyectos Odoo\modulos_odoo_fenalco\base_external_dbsource_oracle\models\base_external_dbsource.py
```
3. Encuentra la línea de *código cx_Oracle.init_oracle_client(lib_dir= r"C:\instantclient_19_14")*
```python
   # TODO : Pasar como parametro general del modulo data source la ruta del installclient oracle
        cx_Oracle.init_oracle_client(lib_dir= r"C:\instantclient_19_14")
        CONNECTORS.append(('cx_Oracle', 'Oracle')) 
```
4. Donde dice* lib_dir=r"*, agrega la ruta donde se encuentra la carpeta *instantclient_19_14*.
```python
        cx_Oracle.init_oracle_client(lib_dir= r"agrega la ruta aqui")
```
	(Esto se hace para utilizar la librería cx_Oracle para inicializar el cliente de Oracle en la máquina local. La función init_oracle_client recibe como parámetro la dirección de la ubicación donde se encuentra la librería de Oracle (instantclient_19_14 en este caso), de manera que el ORM pueda utilizarla para conectarse con la base de datos.)

###Crear una variable de entorno en la máquina local

Para crear una variable de entorno en la máquina local, sigue estos pasos:

1. En la sección de variables del sistema, busca la variable *path*.
2. Entra a la ubicación donde se instaló Odoo
3. Ubica la siguiente carpeta *\odoo15\python\Scripts*
4. Copia la ruta completa de esa ubicación, por ejemplo: 
`C:\odoo15\python\Scripts`
5. Abre la variable path
6. Haz clic en "*Nuevo*"
7. Pega finalmente la ruta de la dirección de la carpeta.
8. Acepta para guardar los cambios.


###Ejecutar e instalar las librerías del archivo *requirements.txt*
Abre la consola y ejecuta el siguiente comando:

`pip install -r requirements.txt`

###Resolución de advertencias
> - Inicia la ejecución del proyecto Odoo localmente.
- Si persisten las advertencias en la consola, revisa los mensajes de error para identificar qué librerías o dependencias faltan por instalar.
- Instala las librerías o dependencias faltantes utilizando el comando: 
	`pip install <nombre-de-la-librería>`.
<p>
> **¡Listo!** Con estas instrucciones, deberías ser capaz de instalar Odoo 15 localmente y conectarlo con Oracle. Si tienes alguna duda o problema durante la instalación, no dudes en preguntar.
</p>
