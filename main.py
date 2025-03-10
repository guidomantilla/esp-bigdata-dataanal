import pandas as pd
import numpy as np

if __name__ == "__main__":
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
