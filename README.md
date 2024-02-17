# imagine-apps
Repositorio para prueba técnica de imagine apps
################################################################################################################################################################
Autor: Wdpinto
Fecha: 17/12/2024
Descripción: En este archivo se encuentran todas las instrucciones necesarias para poder ejecutar el proyecto construido para la prueba técnica como desarrollador Django en la compañia Imagine apps.
#################################################################################################################################################################
Versiones de las dependencias usadas
git version 2.43.0.windows.1
Python 3.12.2
pip pip 24.0
Django 5.0.2
djangorestframework-3.14.0
#################################################################################################################################################################
Instrucciones:
Instalación de Python, PIP y Django

1. Descarga Python:
Visita el sitio web oficial de Python en https://www.python.org/ y descarga la última versión estable de Python para tu sistema operativo. Sigue las instrucciones de instalación proporcionadas en la página de descarga.
3. Instala Python:
Ejecuta el instalador descargado y sigue las instrucciones del asistente de instalación para instalar Python en tu sistema.
4. Verifica la instalación:
Una vez que la instalación esté completa, puedes verificar si Python se instaló correctamente abriendo una terminal o símbolo del sistema y escribiendo:
python --version
Esto debería imprimir la versión de Python que acabas de instalar.
5. Verifica pip:
Después de instalar Python, pip generalmente se instala automáticamente. Para verificar si pip se instaló correctamente, escribe lo siguiente en tu terminal o símbolo del sistema:
pip --version
Esto debería imprimir la versión de pip que se instaló en tu sistema.
Si por alguna razón pip no se instaló automáticamente, puedes seguir las instrucciones en la documentación oficial de Python para instalar pip manualmente: https://pip.pypa.io/en/stable/installation/
6. Revisar si tenemos instalado django en nuestro entorno:
python -m django --version
En caso de que se tenga una versión de django revisar que sea la version 1.11.29 o alguna compatible con la version de Python que tenemos actualmente.
Si no se tiene instalada ejecutar el siguiente comando para instalarla:
pip install django
Aca se instalarán los paquetes necesarios para Django y luego de esto debemos revisar que la instalación se haya realizado de forma correcta ejecutando el comando del paso numero 6.

###############################################################################################################################################################
Instalación de Git

1. Verificar si ya tenemos instalada una versión de git en nuestro entorno a través del siguiente comando:
   git --version
2. En caso de tener una versión instalada, podemos continuar con el siguiente paso a la inicialización del repositorio, de lo contrario continuar con el paso 3 para realizar la instalación.
3. Visita el sitio web oficial de Git en https://git-scm.com/ y descarga el instalador para Windows.
4. Ejecuta el instalador descargado y sigue las instrucciones del asistente de instalación.
5. Verificar la instalación de git repitiendo el comando del paso 1.
   
###############################################################################################################################################################
Inicialización del repositorio en GIT:

1. Crear una carpeta en el directorio en el que queremos que este ubicado nuestro proyecto por ejemplo C:\Users\PC\Desktop
2. Luego de crearla abrir un cmd o la terminal de preferencia que queramos manejar
3. ingresar a la ubicación de la carpeta que creamos a través del siguiente comando:
   Si la carpeta creada se llama por ejemplo imagine-apps   
   cd C:\Users\PC\Desktop\imagine-apps\
4. Una vez nos encontramos dentro de la carpeta creada ejecutar el comando para la inicialización del respositorio en Git:
   git init
5. Clonar el repositorio del proyecto con el siguiente comando:
git clone https://github.com/wdpintor1/imagine-apps.git
6. Una vez clonado podemos poner a correr la aplicación con el siguiente comando:

