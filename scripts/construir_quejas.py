import sys
import pandas as pd
from chatlas import ChatOpenAI
from pydantic import BaseModel

prompt = """Eres un experto en lógistica y transporte en México
    Tu trabajo es generar la queja más probable que tenga el operador sobre alguna de estas categorías
    [finanzas, recursos humanos u operaciones] basado unicamente en la información que se te proporciona.
    La queja debe ser redactada como si la redactara el operador, debe ser corta y concisa de máximo 10 palabras.
    La categoría debe ser la que más afecta al operador.
    Por ejemplo salarios [finanzas], exceso de trabajo [recursos humanos] o largos tiempos de espera [operaciones].
    Piensa tu respuesta paso por paso, usando ese razonamiento quiero que le asignes una probabilidad de abandono
    del trabajo entre el 1 y el 5 donde 1 es nada probable y 5 es muy probable."""

chat = ChatOpenAI(
    model = "gpt-4o-mini",
    system_prompt = prompt
)

class Operador(BaseModel):
    categoria: str
    queja: str
    probabilidad: int

def format_operador_info(df, row):
    return (
        f"Edad del conductor: {df.edad[row]}; "
        f"Años en la empresa: {df.antiguedad[row]}; "
        f"Salario base mensual: {df.salario_base[row]}; "
        f"Distancia recorrida mensual: {df.distancia_recorrida[row]}; "
        f"Bono por desempeño mensual: {df.bono_mensual[row]}; "
        f"Dependientes económicos: {df.tiene_dependientes[row]}; "
        f"Viajes cancelados: {df.viajes_cancelados[row]}; "
        f"Tiempo de espera excesivo: {df.espera_excesiva[row]}; "
        f"Problemas de pago: {df.problemas_pago[row]}; "
        f"Quejas previas: {df.quejas_previas[row]}"
    )

def main(input_file, output_file):
    # Load the dataset of operators
    df = pd.read_csv(input_file)

    # List to store the complaints
    quejas = []

    # Loop through the rows of the dataframe and extract complaints using ChatOpenAI
    for i in range(len(df)):
        operador_info = format_operador_info(df, i)
        respuesta = chat.extract_data(
            operador_info,
            data_model=Operador
        )
        quejas.append(respuesta)

    # Convert the results into a DataFrame
    df_quejas = pd.DataFrame(quejas)

    # Concatenate the original dataframe with the complaints and save the result
    result_df = pd.concat([df, df_quejas], axis=1)
    result_df.to_csv(output_file, index=False)

    print("Quejas generadas y guardadas correctamente en el archivo:", output_file)

# Execute the main function when the script is run
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file> <output_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)
