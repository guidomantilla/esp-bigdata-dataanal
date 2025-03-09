import numpy as np
import sympy as sp
from fractions import Fraction

from matplotlib import pyplot as plt
from sympy import latex
from IPython.display import display, Latex


def print_solution(x, y):
    print(
        f"Solution: x = {Fraction(x).limit_denominator()}, y = { Fraction(y).limit_denominator() }"
    )


def print_determinants(detA, detAx, detAy):
    print(
        f"Determinants: det(A) = {round(detA, 2)}, det(Ax) = {round(detAx, 2)}, det(Ay) = {round(detAy, 2)}"
    )


def print_analysis_square(detA, detAx, detAy):
    print_determinants(detA, detAx, detAy)
    if detA == 0:
        if detAx == 0 and detAy == 0:
            print(
                "The system does not have determinant and also has infinite solutions."
            )
        else:
            print("The system does not have determinant and has no solution.")
    else:
        print("The system does have determinant and has a unique solution.")


def print_analysis_not_square(rankA, rankAB):
    print(f"Rank: rank(A) = {round(rankA, 2)}, rank(AB) = {round(rankAB, 2)}")
    if rankA == rankAB:
        if rankA == 2:
            print("The system has a unique solution.")
        else:
            print("The system has infinite solutions.")
    else:
        print("The system has no solution.")


def print_solution_inequality(label, x, y, expression, relation, result, above=True):
    equation = sp.Rel(expression, result, relation)
    solX, solY = sp.solveset(equation, x, domain=sp.S.Reals), sp.solveset(
        equation, y, domain=sp.S.Reals
    )
    printSolTitle = "Solución de la desigualdad: "
    printSolX = "$${} = {}$$".format(latex(x), latex(solX.doit()))
    printSolY = "$${} = {}$$".format(latex(y), latex(solY.doit()))
    display(Latex(printSolTitle), Latex(printSolX), Latex(printSolY))

    lineY = sp.Eq(expression, result)
    solY = sp.solve(lineY, y, domain=sp.S.Reals)[0]
    x_vals = np.linspace(-10, 10, 50)
    y_vals = [float(solY.subs(x, val)) for val in x_vals]

    plt.plot(x_vals, y_vals, "r", label=label)
    if above:
        plt.fill_between(x_vals, y_vals, 30, alpha=0.3, color="red")
    else:
        plt.fill_between(x_vals, y_vals, -30, alpha=0.3, color="red")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axhline(0, color="black", linewidth=1)
    plt.axvline(0, color="black", linewidth=1)
    plt.legend()
    plt.title(f"Región factible para {label}")
    plt.grid()
    plt.show()
