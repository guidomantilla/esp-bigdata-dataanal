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


def calculate_solution_equation(x, y, equation):
    sol_x = sp.solveset(equation, x, domain=sp.S.Reals)
    sol_y = sp.solveset(equation, y, domain=sp.S.Reals)
    return sol_x, sol_y


def print_solution_equation(x, y, equation, sol_x, sol_y):
    print_sol_title = f"Solución de la desigualdad: {equation.doit()}"
    print_sol_x = "$${} = {}$$".format(latex(x), latex(sol_x.doit()))
    print_sol_y = "$${} = {}$$".format(latex(y), latex(sol_y.doit()))
    display(Latex(print_sol_title), Latex(print_sol_x), Latex(print_sol_y))


def plot_solution_equation(x, y, equation):
    return plot_solution_equations(x, y, [equation])


def plot_solution_equations(x, y, equations):

    lines = []
    lim, x_var, y_var = (-10, 10), (x, -10, 10), (y, -10, 10)
    for equation in equations:
        sol_y = sp.solve(equation, y, domain=sp.S.Reals)
        print(sol_y, sol_y.free_symbols)
        if x in sol_y.free_symbols and y in sol_y.free_symbols:
            lines.append(sol_y.rhs)
            continue

        if x in sol_y.free_symbols and y not in sol_y.free_symbols:
            lines.append(sol_y.rhs)
            continue

        if y in sol_y.free_symbols:
            lines.append(sol_y.lhs)
            continue

    print(lines)
    plot_lines = sp.plot(
        *lines,
        x_var,
        ylim=lim,
        show=False,
    )

    system_equation = sp.And(*equations)
    plot = sp.plot_implicit(
        system_equation,
        x_var,
        y_var,
        title=f"Región factible para {system_equation.doit()}",
        line_color="red",
        show=False,
        legend="true",
    )

    for idx, line in enumerate(lines):
        plot.append(plot_lines[idx])

    return plot


"""
    line_y = sp.Eq(right_expression, left_expression)
    sol_y = sp.solve(line_y, y, domain=sp.S.Reals)[0]
    x_vals = np.linspace(-10, 10, 50)
    y_vals = [float(sol_y.subs(x, val)) for val in x_vals]

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
"""
