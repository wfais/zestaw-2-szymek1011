import os
import time
import threading
import sys

# Stałe konfiguracyjne
LICZBA_KROKOW = 80_000_000
LICZBA_WATKOW = sorted({1, 2, 4, os.cpu_count() or 4})


def policz_fragment_pi(pocz: int, kon: int, krok: float, wyniki: list[float], indeks: int) -> None:
    suma = 0.0
    for i in range(pocz, kon):
        x = (i + 0.5) * krok
        suma += 4.0 / (1.0 + x * x)

    wyniki[indeks] = suma


def main():
    print(f"Python: {sys.version.split()[0]}  (tryb bez GIL? {getattr(sys, '_is_gil_enabled', lambda: None)() is False})")
    print(f"Liczba rdzeni logicznych CPU: {os.cpu_count()}")
    print(f"LICZBA_KROKOW: {LICZBA_KROKOW:,}\n")

    # probne wlaczenie
    krok = 1.0 / LICZBA_KROKOW
    wyniki = [0.0]
    w = threading.Thread(target=policz_fragment_pi, args=(0, LICZBA_KROKOW, krok, wyniki, 0))
    w.start()
    w.join()

    # wlacsiwy eksperyment

    czasy = {}

    for liczba_w in LICZBA_WATKOW:
        wyniki = [0.0] * liczba_w
        watki = []

        # wyznaczamy przedzialy
        rozmiar = LICZBA_KROKOW // liczba_w

        start_time = time.perf_counter()

        for idx in range(liczba_w):
            pocz = idx * rozmiar
            kon = LICZBA_KROKOW if idx == liczba_w - 1 else (idx + 1) * rozmiar

            t = threading.Thread(
                target=policz_fragment_pi,
                args=(pocz, kon, krok, wyniki, idx),
            )
            watki.append(t)
            t.start()

        for t in watki:
            t.join()

        # wynik końcowy: suma fragmentow razy krok
        wynik_pi = sum(wyniki) * krok

        elapsed = time.perf_counter() - start_time
        czasy[liczba_w] = elapsed

        print(f"{liczba_w} wątek/ki: pi ≈ {wynik_pi:.12f}, czas = {elapsed:.4f} s")


    # przyspieszenia względem jednego wątku
    print("\nPrzyspieszenie względem 1 wątku:")

    czas1 = czasy[1]

    for liczba_w in LICZBA_WATKOW:
        speedup = czas1 / czasy[liczba_w]
        print(f"{liczba_w} wątki: ×{speedup:.2f}")


if __name__ == "__main__":
    main()

