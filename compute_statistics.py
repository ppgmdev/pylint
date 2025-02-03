"""
Este modulo calcula media, mediana, moda varianza, desviacion estandar
"""
import sys
import time
from typing import List, Union


def leer_archivo(nombre_archivo: str) -> List[float]:
    """Lee números de un archivo, manejando datos inválidos."""
    numeros = []
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                try:
                    numeros.append(float(linea.strip()))
                except ValueError:
                    print(f"Error: Dato inválido '{linea.strip()}' en el archivo.")
    except FileNotFoundError:
        print(f"Error: Archivo '{nombre_archivo}' no encontrado.")
        sys.exit(1)
    return numeros


def calcular_media(numeros: List[float]) -> float:
    """Calcula la media de una lista de números."""
    return sum(numeros) / len(numeros)


def calcular_mediana(numeros: List[float]) -> float:
    """Calcula la mediana de una lista de números."""
    numeros_ordenados = sorted(numeros)
    n = len(numeros_ordenados)
    if n % 2 == 0:
        return (numeros_ordenados[n//2 - 1] + numeros_ordenados[n//2]) / 2
    return numeros_ordenados[n//2]


def calcular_moda(numeros: List[float]) -> Union[float, str]:
    """Calcula la moda de una lista de números."""
    frecuencia = {}
    for num in numeros:
        frecuencia[num] = frecuencia.get(num, 0) + 1
    frecuencia_maxima = max(frecuencia.values())
    modas = [num for num, freq in frecuencia.items() if freq == frecuencia_maxima]
    if len(modas) == len(numeros):
        return "No hay moda única"
    if len(modas) > 1:
        return f"Múltiples modas: {', '.join(map(str, modas))}"
    return modas[0]


def calcular_varianza(numeros: List[float], media: float) -> float:
    """Calcula la varianza de una lista de números."""
    return sum((x - media) ** 2 for x in numeros) / len(numeros)


def calcular_desviacion_estandar(varianza: float) -> float:
    """Calcula la desviación estándar a partir de la varianza."""
    return varianza ** 0.5


def main():
    """ Funcion principal del programa """
    if len(sys.argv) != 2:
        print("Uso: python compute_statistics.py fileWithData.txt")
        sys.exit(1)

    nombre_archivo = sys.argv[1]
    tiempo_inicio = time.time()

    numeros = leer_archivo(nombre_archivo)

    if not numeros:
        print("Error: No se encontraron números válidos en el archivo.")
        sys.exit(1)

    media = calcular_media(numeros)
    mediana = calcular_mediana(numeros)
    moda = calcular_moda(numeros)
    varianza = calcular_varianza(numeros, media)
    desviacion_estandar = calcular_desviacion_estandar(varianza)

    tiempo_fin = time.time()
    tiempo_transcurrido = tiempo_fin - tiempo_inicio

    resultados = f"""
Estadísticas Descriptivas:
Media: {media}
Mediana: {mediana}
Moda: {moda}
Varianza: {varianza}
Desviación Estándar: {desviacion_estandar}
Tiempo de Ejecución: {tiempo_transcurrido:.4f} segundos
"""

    print(resultados)

    with open("StatisticsResults.txt", "w", encoding='utf-8') as f:
        f.write(resultados)

    print("Los resultados han sido guardados en StatisticsResults.txt")


if __name__ == "__main__":
    main()
