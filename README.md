# Synthetic Data

Este proyecto consiste en tres partes principales:

1. Generación de datos sintéticos demográficos y de comportamiento de viaje para 1K conductores, principalmente haciendo uso de `faker` y de _distribuciones de probabilidad_ tomando como base la información presentada por la Secretaría de Economía en la [encuesta para la ocupación de Conductores de Camiones, Camionetas y Automóviles de Carga](https://www.economia.gob.mx/datamexico/es/profile/occupation/conductores-de-camiones-camionetas-y-automoviles-de-carga)

2. Creación de las potenciales quejas de los conductores respecto a su trabajo en las categorías de finanzas, recursos humanos u operaciones haciendo uso de `OpenAI` en particular del modelo `gpt-4o-mini` así como la determinación de la probabilidad de abandono del empleo en cada caso.

3. Uso de oversampling para la contrucción de una muestra de 3K operadores que son usados en la construcción del modelo `XGBoost` con la finalidad de pronosticar la probabilidad de renuncia para cada uno de los operadores

## Requisitos

- Python 3.11
- Jupyter Notebooks
- Una cuenta en [OpenAI](https://openai.com) y una clave de API

## Instalación

### 1. Instalar Python 3.11

Asegúrate de tener Python 3.11 instalado en tu sistema. Puedes verificar tu versión de Python con el siguiente comando:

```bash
python --version
```

### 2. Instalar Jupyter Notebooks

Para instalar Jupyter Notebooks en tu sistema en caso de no haberlo hecho. Ejecuta el siguiente comando:

```bash
pip install notebook
```

### 3. Establecer la variable de entorno OPENAI_API_KEY

Asegurate de haber generado una clave de API para el uso de [OpenAI](https://openai.com). Con el siguiente comando la puedes establecer:

```bash
set OPENAI_API_KEY=sk-...
```

### 3. Instalar las librería en el archivo de requirements.txt

Una vez que tengas Python 3.11, instala las dependencias necesarias para el proyecto:

```bash
pip install -r requirements.txt
```

## Ejecucción

### 1. Generar los datos demográficos y de comportamiento

Una vez con todo instalado, necesitamos ejecutar el script [generar_datos.py](scripts/generar_datos.py) pasando como parámetros una ruta para guardar los datos y el tamaño de la muestra a generar:

```bash
python scripts/generar_datos.py data/operadores.csv 10
```

### 2. Construir quejas y probabilidades de abandono

El siguiente paso es ejecutar el script [construir_quejas.py](scripts/construir_quejas.py) pasando como argumentos la ruta del archivo del paso 1 y la ruta donde queremos guardar los datos con las quejas generadas:

```bash
python scripts/construir_quejas.py data/operadores.csv data/quejas.csv
```

### 2. Entrenar el modelo de predicción

Finalmente podemos ejecutar el notebook [entrenar_modelo.py](notebooks/entrenar_modelo.py). Para ello levantamos jupyter:

```bash
jupyter notebook
```

Buscamos el [entrenar_modelo.py](notebooks/entrenar_modelo.py) en nuestro equipo y después de abrirlo podremos ejecutar interactivamente.

## Por hacer

1. Crear un Dockefile para que sea más sencillo
2. Correr un análisis exploratorio de datos para ver nuestros datos generados
3. Óptimizar el modelo que construimos afinando los hiperparámetros
