LICZBY_RZYMSKIE = [
    ("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
    ("C", 100), ("XC", 90), ("L", 50), ("XL", 40),
    ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)
]

DOZWOLONE_RZYMSKIE = {"I", "V", "X", "L", "C", "D", "M"}
RZYMSKIE_DICT = dict(LICZBY_RZYMSKIE)  # słownik dla szybkiego dostępu


def rzymskie_na_arabskie(rzymskie: str) -> int:
    if not rzymskie or not all(ch in DOZWOLONE_RZYMSKIE for ch in rzymskie):
        raise ValueError(f"Niepoprawna liczba rzymska: {rzymskie}")

    wartosc, i = 0, 0
    while i < len(rzymskie):
        if i + 1 < len(rzymskie) and rzymskie[i:i + 2] in RZYMSKIE_DICT:
            wartosc += RZYMSKIE_DICT[rzymskie[i:i + 2]]
            i += 2
        else:
            wartosc += RZYMSKIE_DICT[rzymskie[i]]
            i += 1

    if arabskie_na_rzymskie(wartosc) != rzymskie:
        raise ValueError(f"Niepoprawny format liczby rzymskiej: {rzymskie}")
    return wartosc


def arabskie_na_rzymskie(arabskie: int) -> str:
    if not isinstance(arabskie, int):
        raise TypeError(f"Liczba musi być typu int, a nie {type(arabskie).__name__}")
    if not (1 <= arabskie <= 3999):
        raise ValueError("Liczba musi być w zakresie 1-3999")

    rzymskie = ""
    for symbol, wartosc in LICZBY_RZYMSKIE:
        while arabskie >= wartosc:
            rzymskie += symbol
            arabskie -= wartosc
    return rzymskie


if __name__ == '__main__':
    try:
        # Przykłady konwersji rzymskiej na arabską
        rzymska = "MCMXCIV"
        print(f"Liczba rzymska {rzymska} to {rzymskie_na_arabskie(rzymska)} w arabskich.")

        # Przykłady konwersji arabskiej na rzymską
        arabska = 1994
        print(f"Liczba arabska {arabska} to {arabskie_na_rzymskie(arabska)} w rzymskich.")

    except (ValueError, TypeError) as e:
        print(f"Błąd: {e}")
