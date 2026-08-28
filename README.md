# proyecto_s7_rm
Proyecto final Sprint 7 TripleTen Rafael Malez.

# Enlace aplicación web
https://proyecto-s7-rm.onrender.com

PROYECTO SPRINT 7

DESCRIPCIÓN.
Desarrollo de una aplicación web o Dashboard Interactivo construido con Streamlit, diseñado para analizar un conjunto de datos de anuncios de venta de coches.

COMPOSICIÓN DEL REPOSITORIO.
- Un archivo .gitignore que indica a Git qué archivos o carpetas debe ignorar para que no se suban a GitHub.

- Un archivo EDA.ipynb, con el análisis correspondiente del conjunto de datos base para nuestra aplicación web.

- Un archivo README.md, con una descripción clara del proyecto, incluyendo cómo está organizado el repositorio y los pasos necesarios para ejecutar la aplicación de manera local.

- Un archivo Python (app.py) con el código que permite la graficación del análisis de los datos y la creación de elementos web para la interacción del usuario final en nuestra aplicación web.

- Un archivo de texto requirements.txt, con la mención de las librerías que se usaron en el archivo app.py.

- Un archivo vehicles_us.csv, que contiene la tabla de datos analizada y graficada.

INSTRUCCIONES DE EJECUCIÓN LOCAL:
1. Clonar el repositorio y navegar a la carpeta:
   Bash
   git clone "https://github.com/RAFAMALEZ/proyecto_s7_rm"
   cd proyecto_s7_rm

2. Crear y activar el entorno virtual:
   Bash
   python -m venv vehicles_env
   # En Windows (PowerShell):
   .\vehicles_env\Scripts\activate

3. Instalar las dependencias necesarias:
   Bash
   pip install -r requirements.txt

4. Ejecutar la aplicación interactiva de Streamlit:
   Bash
   streamlit run app.py
   
