"""
Este módulo convierte números de un archivo a sus representaciones binarias y hexadecimales.
"""
import sys
import time


def leer_archivo(nombre_archivo):
    """Lee números de un archivo, manejando datos inválidos."""
    numeros = []
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                try:
                    num = float(linea.strip())
                    numeros.append(num)
                except ValueError:
                    print(f"Error: Dato inválido '{linea.strip()}' en el archivo.")
    except FileNotFoundError:
        print(f"Error: Archivo '{nombre_archivo}' no encontrado.")
        sys.exit(1)
    return numeros


def a_binario(num):
    """Convierte un número a representación binaria."""
    if num == 0:
        return "0"
    parte_entera = int(abs(num))
    parte_fraccionaria = abs(num) - parte_entera
    # Convertir parte entera
    binario_entero = ""
    while parte_entera > 0:
        binario_entero = str(parte_entera % 2) + binario_entero
        parte_entera //= 2
    # Convertir parte fraccionaria
    binario_fraccionario = ""
    precision = 10  # Número de bits fraccionarios
    while parte_fraccionaria > 0 and len(binario_fraccionario) < precision:
        parte_fraccionaria *= 2
        bit = int(parte_fraccionaria)
        binario_fraccionario += str(bit)
        parte_fraccionaria -= bit
    # Combinar partes
    if binario_fraccionario:
        resultado = binario_entero + "." + binario_fraccionario
    else:
        resultado = binario_entero
    return "-" + resultado if num < 0 else resultado

def a_hexadecimal(num):
    """Convierte un número a representación hexadecimal."""
    caracteres_hex = "0123456789ABCDEF"
    if num == 0:
        return "0"
    parte_entera = int(abs(num))
    parte_fraccionaria = abs(num) - parte_entera
    # Convertir parte entera
    hex_entero = ""
    while parte_entera > 0:
        hex_entero = caracteres_hex[parte_entera % 16] + hex_entero
        parte_entera //= 16
    # Convertir parte fraccionaria
    hex_fraccionario = ""
    precision = 10  # Número de dígitos fraccionarios
    while parte_fraccionaria > 0 and len(hex_fraccionario) < precision:
        parte_fraccionaria *= 16
        digito = int(parte_fraccionaria)
        hex_fraccionario += caracteres_hex[digito]
        parte_fraccionaria -= digito
    # Combinar partes
    if hex_fraccionario:
        resultado = hex_entero + "." + hex_fraccionario
    else:
        resultado = hex_entero
    return "-" + resultado if num < 0 else resultado


def main():
    """Funcion principal del programa"""
    if len(sys.argv) != 2:
        print("Uso: python convertNumbers.py fileWithData.txt")
        sys.exit(1)

    nombre_archivo = sys.argv[1]
    tiempo_inicio = time.time()

    numeros = leer_archivo(nombre_archivo)

    if not numeros:
        print("Error: No se encontraron números válidos en el archivo.")
        sys.exit(1)

    resultados = []
    for num in numeros:
        binario = a_binario(num)
        hexadecimal = a_hexadecimal(num)
        resultados.append(f"Número: {num}\nBinario: {binario}\nHexadecimal: {hexadecimal}\n")

    tiempo_fin = time.time()
    tiempo_transcurrido = tiempo_fin - tiempo_inicio

    salida = "\n".join(resultados)
    salida += f"\nTiempo de Ejecución: {tiempo_transcurrido:.4f} segundos"

    print(salida)

    with open("ConversionResults.txt", "w", encoding='utf-8') as f:
        f.write(salida)

    print("Los resultados han sido guardados en ConversionResults.txt")


if __name__ == "__main__":
    main()
