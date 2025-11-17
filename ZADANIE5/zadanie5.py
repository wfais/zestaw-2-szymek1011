import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, sympify, lambdify


# Funkcja rysująca wykres na podstawie eval()
def rysuj_wielomian(wejscie):
    wzor, przedzial = wejscie.split(',')
    wzor = wzor.strip()
    x_min, x_max = map(float, przedzial.split())

    # generowanie wartości x
    x_val = np.linspace(x_min, x_max, 200)

    # Obliczanie wartości y przy użyciu eval()
    # kontekst zawiera zmienną x wskazującą na tablicę NumPy
    y_val = eval(wzor, {"x": x_val, "np": np, "__builtins__": {}})

    # rysowanie wykresu (bez show)
    plt.figure()
    plt.plot(x_val, y_val, label=f"f(x) = {wzor}")
    plt.title("Wielomian - wersja eval()")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()

    # Zwracanie wartości na granicach przedziału
    return y_val[0], y_val[-1]


# Funkcja rysująca wykres na podstawie SymPy i lambdify()
def rysuj_wielomian_sympy(wejscie):
    wzor, przedzial = wejscie.split(',')
    wzor = wzor.strip()
    x_min, x_max = map(float, przedzial.split())

    # def symbolu
    x = symbols('x')

    # SymPy: konwersja tekstu na wyrażenie symboliczne
    expr = sympify(wzor)

    # zamiana na funkcję numeryczną: backend numpy
    f = lambdify(x, expr, "numpy")

    # generowanie wartości x
    x_val = np.linspace(x_min, x_max, 200)

    # obliczanie wartości y
    y_val_sympy = f(x_val)

    # rysowanie wykresu
    plt.figure()
    plt.plot(x_val, y_val_sympy, label=f"f(x) = {wzor}")
    plt.title("Funkcja - wersja SymPy")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()

    # Zwracanie wartości na granicach przedziału
    return y_val_sympy[0], y_val_sympy[-1]


if __name__ == '__main__':
    # Przykładowe wywołanie pierwszej funkcji
    wejscie1 = "x**3 + 3*x + 1, -10 10"

    # Pierwszy wykres z eval
    wynik_eval = rysuj_wielomian(wejscie1)
    print("Wynik (eval):", wynik_eval)

    # Drugie wejście dla funkcji SymPy - bardziej złożona funkcja
    wejscie2 = "x**4 - 5*x**2 + 3*sin(x), -10 10"

    # Drugi wykres z SymPy
    wynik_sympy = rysuj_wielomian_sympy(wejscie2)
    print("Wynik (SymPy):", wynik_sympy)

    # Wyświetlanie obu wykresów
    plt.show()
