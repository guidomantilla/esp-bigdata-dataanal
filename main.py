import pandas as pd
import numpy as np
import math

def calcular_bmi(peso_lb: float, altura_inch: float):
    peso_kg = peso_lb * 0.45
    altura_mts = altura_inch * 0.025
    return round(peso_kg / math.pow(altura_mts,2),2)

def calcular_cambio(cambio: int):
    denominaciones = [500, 200, 100, 50]
    resultado = []
    for d in denominaciones:
        cantidad, cambio = divmod(cambio, d)
        resultado.append(cantidad)
    return "{},{},{},{}".format(*resultado)

def es_divisible(n: int, d: int)->int:
    if d == 0:
        return 0
    if n % (2 * d) == 0:
        return "n es divisible por 2d"
    elif n % d == 0:
        return "n es divisible por d"
    else:
        return "n no es divisible ni por d ni por 2d"

def clasificar_regalo(id: int) -> str:
    id_str = str(id)
    es_palindromo,es_par = id_str == id_str[::-1],(id % 2 == 0)

    if es_palindromo and not es_par:
        return "girl"
    elif es_palindromo and es_par:
        return "boy"
    elif not es_palindromo and es_par:
        return "man"
    else:
        return "woman"

def calcular_horario_llegada(hora_salida: int, minuto_salida: int, segundo_salida: int,
                             duracion_horas: int, duracion_minutos: int, duracion_segundos: int):

    segundo_llegada = segundo_salida + duracion_segundos
    minuto_extra, segundo_llegada = divmod(segundo_llegada, 60)

    minuto_llegada = minuto_salida + duracion_minutos + minuto_extra
    hora_extra, minuto_llegada = divmod(minuto_llegada, 60)

    hora_llegada = (hora_salida + duracion_horas + hora_extra) % 24

    return f"{hora_llegada}:{minuto_llegada}:{segundo_llegada}"

def aplicar_giro(orientacion: str, comando: str):
    direcciones = ["N", "E", "S", "W"]
    idx = direcciones.index(orientacion)
    if comando == "L":
        return direcciones[(idx - 1) % 4]
    elif comando == "R":
        return direcciones[(idx + 1) % 4]
    elif comando == "H":
        return direcciones[(idx + 2) % 4]
    elif comando == ".":
        return orientacion
    else:
        raise ValueError(f"Comando inválido: {comando}")

def movimiento_robot(orientacion_actual: str, giro_1: str, giro_2: str, giro_3: str) -> str:
    orientacion_actual = aplicar_giro(orientacion_actual, giro_1)
    orientacion_actual = aplicar_giro(orientacion_actual, giro_2)
    orientacion_actual = aplicar_giro(orientacion_actual, giro_3)

    return orientacion_actual

def conteo_de_materias(nombre_materia_1: str, nombre_materia_2: str, nombre_materia_3: str) -> int:
    favoritas = ["programacion", "matematica", "filosofia", "literatura"]

    def es_favorita(nombre: str) -> bool:
        return any(fav in nombre for fav in favoritas)

    contador = 0
    for materia in [nombre_materia_1, nombre_materia_2, nombre_materia_3]:
        if es_favorita(materia):
            contador += 1

    return contador


def picas_y_fijas(numero_secreto: int, intento: int) -> dict:
    secreto_str = str(numero_secreto)
    intento_str = str(intento)

    fijas = 0
    picas = 0

    for i in range(4):
        if intento_str[i] == secreto_str[i]:
            fijas += 1

    for i in range(4):
        if intento_str[i] in secreto_str and intento_str[i] != secreto_str[i]:
            picas += 1

    return {"PICAS": picas, "FIJAS": fijas}

def mejor_del_salon(estudiante1: dict, estudiante2: dict, estudiante3: dict,
                    estudiante4: dict, estudiante5: dict) -> str:
    estudiantes = [estudiante1, estudiante2, estudiante3, estudiante4, estudiante5]
    mejor_nombre = None
    mejor_promedio = -1

    for est in estudiantes:
        promedio = (est["matematicas"] + est["español"] +
                    est["ciencias"] + est["literatura"] +
                    est["arte"]) / 5

        if (promedio > mejor_promedio or
            (promedio == mejor_promedio and est["nombre"].lower() < mejor_nombre.lower())):
            mejor_promedio = promedio
            mejor_nombre = est["nombre"]

    return mejor_nombre


if __name__ == "__main__":

    print(calcular_bmi(154,70.86))
    print(calcular_cambio(100))
    print(calcular_horario_llegada(6,52,30,0,55,50))


    print("*****************************")

    print(f"Series en Pandas con Index default:")
    serie01 = pd.Series([1, 2, 3, 4, 5])
    print(serie01)
    print(f"Acceder al index 3 para ver el valor de la serie: {serie01[3]}")
    print(f"Metadata del Index: {serie01.index}")

    print("*****************************")

    print(f"Series en Pandas con Index personalizado:")
    serie02 = pd.Series([1, 2, 3, 4, 5], index=["a", "b", "c", "d", "e"])
    print(serie02)
    print(f"Acceder al index 3 para ver el valor de la serie: {serie02.iloc[3]}")
    print(f"Acceder al index 'c' para ver el valor de la serie: {serie02['c']}")
    print(f"Metadata del Index: {serie02.index}")

    print("*****************************")

    print(f"Maximo y minimo de la serie01: {serie01.max()} y {serie01.min()}")
    print(f"Maximo y minimo de la serie02: {serie02.max()} y {serie02.min()}")

    print("*****************************")

    serie02.index = ["uno", "dos", "tres", "cuatro", "cinco"]
    print(serie02)
    print(f"Acceder al index 3 para ver el valor de la serie: {serie02.iloc[3]}")
    print(f"Acceder al index 'c' para ver el valor de la serie: {serie02['tres']}")
    print(f"Metadata del Index: {serie02.index}")

    print("*****************************")

    serie03 = pd.Series([2, 3, np.nan])
    print(serie03)
    print(f"tiene nan: {np.any(np.isnan(serie03))}")

    print("*****************************")

    serie03 = pd.Series(
        np.random.randn(10), index=pd.date_range("1/1/2000", periods=10)
    )
    print(serie03)

