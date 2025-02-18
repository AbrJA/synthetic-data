# Synthetic Data

Este proyecto consiste en tres partes principales:

1. Generación de datos sintéticos demográficos y de comportamiento de viaje para 1K conductores, principalmente haciendo uso de `faker` y de _distribuciones de probabilidad_ tomando como base la información presentada por la Secretaría de Economía en la [encuesta para la ocupación de Conductores de Camiones, Camionetas y Automóviles de Carga](https://www.economia.gob.mx/datamexico/es/profile/occupation/conductores-de-camiones-camionetas-y-automoviles-de-carga)

2. Creación de las potenciales quejas de los conductores respecto a su trabajo en las categorías de finanzas, recursos humanos u operaciones haciendo uso de `OpenAI` en particular del modelo `gpt-4o-mini` así como la determinación de la probabilidad de abandono del empleo en cada caso.

3. Uso de oversampling para la contrucción de una muestra de 3K operadores que son usados en la construcción del modelo `XGBoost` con la finalidad de pronosticar la probabilidad de renuncia para cada uno de los operadores

## Requisitos

- Python 3.11
- Una cuenta en [OpenAI](https://openai.com) y una clave de API

## Instalación

### 1. Instalar Python 3.11

Asegúrate de tener Python 3.11 instalado en tu sistema. Puedes verificar tu versión de Python con el siguiente comando:

```bash
python --version
```

### 2. Establecer la variable de entorno OPENAI_API_KEY

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

Una vez con todo instalado, necesitamos ejecutar el script [generar_datos.py](scripts/generar_datos.py)
