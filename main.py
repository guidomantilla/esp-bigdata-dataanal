import pandas as pd
import numpy as np
import math


def calcular_BMI(peso_lb: float, altura_inch: float):
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


def calcular_horario_llegada(hora_salida: int, minuto_salida: int, segundo_salida: int,
                             duracion_horas: int, duracion_minutos: int, duracion_segundos: int):

    segundo_llegada = segundo_salida + duracion_segundos
    minuto_extra, segundo_llegada = divmod(segundo_llegada, 60)

    minuto_llegada = minuto_salida + duracion_minutos + minuto_extra
    hora_extra, minuto_llegada = divmod(minuto_llegada, 60)

    hora_llegada = (hora_salida + duracion_horas + hora_extra) % 24

    return f"{hora_llegada}:{minuto_llegada}:{segundo_llegada}"


if __name__ == "__main__":

    print(calcular_BMI(154,70.86))
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

