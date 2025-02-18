import sys
import pandas as pd
import numpy as np
from faker import Faker

def bounded_normal(mean, std, lower, upper):
    while True:
        value = np.random.normal(mean, std)
        if lower <= value <= upper:
            return value

def generar_datos_sinteticos(num_registros=100):
    fake = Faker('es_ES')
    datos = []
    for _ in range(num_registros):
        id_conductor = fake.uuid4()
        celular = fake.phone_number()
        masculino = np.random.choice([0, 1], p=[0.99, 0.01])
        nombre = fake.name_male() if masculino == 0 else fake.name_female()
        edad = int(bounded_normal(40, 10, 19, 75))
        experiencia = int(bounded_normal(10, 10, 0, edad-18))
        antiguedad = np.random.randint(0, experiencia + 1)
        salario_base = int(bounded_normal(8000, 1000, 6000, 15000))
        distancia_promedio = int(bounded_normal(500, 300, 50, 1500))
        num_viajes = int(bounded_normal(20, 10, 0, min(60, 30000 / distancia_promedio)))
        distancia_recorrida = distancia_promedio * num_viajes
        bono_mensual = np.random.choice([0, 1], p=[0.2, 0.8]) * distancia_recorrida * bounded_normal(0.7, 0.1, 0, 1)
        zona_riesgo = np.random.choice([0, 1], p=[0.2, 0.8])
        tiene_dependientes = np.random.choice([0, 1], p=[0.2, 0.8])
        viaje_urbano = 0 if distancia_promedio < 250 else 1
        descanso_suficiente = np.random.choice([0, 1], p=[0.2, 0.8])
        nivel_estudios = np.random.choice([0, 1, 2, 3], p=[0.1, 0.4, 0.4, 0.1])
        viajes_cancelados = np.random.choice([0, 1], p=[0.8, 0.2])
        espera_excesiva = np.random.choice([0, 1], p=[0.8, 0.2])
        problemas_pago = np.random.choice([0, 1], p=[0.8, 0.2])
        quejas_previas = np.random.choice([0, 1, 2, 3], p=[0.6, 0.2, 0.1, 0.1])

        # Agregar datos a la lista
        datos.append([
            id_conductor,
            nombre,
            celular,
            masculino,
            edad,
            experiencia,
            antiguedad,
            salario_base,
            distancia_recorrida,
            num_viajes,
            bono_mensual,
            zona_riesgo,
            tiene_dependientes,
            viaje_urbano,
            descanso_suficiente,
            nivel_estudios,
            viajes_cancelados,
            espera_excesiva,
            problemas_pago,
            quejas_previas
        ])

    columnas = [
        'id_conductor',
        'nombre',
        'celular',
        'masculino',
        'edad',
        'experiencia',
        'antiguedad',
        'salario_base',
        'distancia_recorrida',
        'num_viajes',
        'bono_mensual',
        'zona_riesgo',
        'tiene_dependientes',
        'viaje_urbano',
        'descanso_suficiente',
        'nivel_estudios',
        'viajes_cancelados',
        'espera_excesiva',
        'problemas_pago',
        'quejas_previas'
    ]

    df = pd.DataFrame(datos, columns=columnas)
    return df

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <output_file.csv> <num_records>")
        sys.exit(1)
    output_file = sys.argv[1]
    num_records = int(sys.argv[2])
    df = generar_datos_sinteticos(num_records)
    df.to_csv(output_file, index=False)
    print(f"File saved to {output_file} with {num_records} records.")

if __name__ == '__main__':
    main()
