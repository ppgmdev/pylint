"""
Este modulo cuenta palabras en un archvio
"""
import sys
import time


def leer_archivo(nombre_archivo):
    """Lee palabras de un archivo, manejando datos inválidos."""
    palabras = []
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                palabras_linea = linea.strip().split()
                for palabra in palabras_linea:
                    if palabra.isalnum():
                        palabras.append(palabra.lower())
                    else:
                        print(f"Advertencia: Palabra inválida '{palabra}' en el archivo.")
    except FileNotFoundError:
        print(f"Error: Archivo '{nombre_archivo}' no encontrado.")
        sys.exit(1)
    return palabras


def contar_palabras(palabras):
    """Cuenta la frecuencia de cada palabra."""
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    return frecuencia


def ordenar_frecuencia(frecuencia):
    """Ordena las palabras por frecuencia de mayor a menor."""
    return sorted(frecuencia.items(), key=lambda x: x[1], reverse=True)


def main():
    """ Funcion principal del programa """
    if len(sys.argv) != 2:
        print("Uso: python word_count.py fileWithData.txt")
        sys.exit(1)

    nombre_archivo = sys.argv[1]
    tiempo_inicio = time.time()

    palabras = leer_archivo(nombre_archivo)

    if not palabras:
        print("Error: No se encontraron palabras válidas en el archivo.")
        sys.exit(1)

    frecuencia = contar_palabras(palabras)
    frecuencia_ordenada = ordenar_frecuencia(frecuencia)

    resultados = "Frecuencia de palabras:\n"
    for palabra, conteo in frecuencia_ordenada:
        resultados += f"{palabra}: {conteo}\n"

    tiempo_fin = time.time()
    tiempo_transcurrido = tiempo_fin - tiempo_inicio

    resultados += f"\nTiempo de ejecución: {tiempo_transcurrido:.4f} segundos"
    resultados += f"\nTotal de palabras distintas: {len(frecuencia)}"
    resultados += f"\nTotal de palabras: {len(palabras)}"

    print(resultados)

    with open("WordCountResults.txt", "w", encoding='utf-8') as f:
        f.write(resultados)

    print("Los resultados han sido guardados en WordCountResults.txt")


if __name__ == "__main__":
    main()
