from fractions import Fraction
from scipy import linalg


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
