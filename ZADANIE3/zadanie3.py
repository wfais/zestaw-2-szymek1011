import requests, re, time, sys
from collections import Counter

URL = "https://pl.wikipedia.org/api/rest_v1/page/random/summary"
N = 100  # liczba losowań

#nagłówki
HEADERS = {
    "User-Agent": "wp-edu-wiki-stats/0.1 (kontakt: twoj-email@domena)",
    "Accept": "application/json",
}

WORD_RE = re.compile(r"[^\W\d_]+", re.UNICODE)  # wyrażenie do dopasowania słów


def selekcja(text: str):
    """ zwraca liste slow - tylko litery male"""
    slowa = WORD_RE.findall(text)
    return [s.lower() for s in slowa if len(s) > 3]


def ramka(text: str, width: int = 80) -> str:
    """ zwraca tekst w ramce """
    max_len = width - 2
    if len(text) > max_len:
        text = text[: max_len - 3] + "..."
    return f"[{text.center(max_len)}]"


def main():
    cnt = Counter()
    licznik_slow = 0
    pobrane = 0

    print(ramka("Start"), end="", flush=True)

    while pobrane < N:
        try:
            response = requests.get(URL, headers=HEADERS, timeout=10) # pobiranie losowego art
            data = response.json()
        except Exception:
            time.sleep(0.1)
            continue

        #tytuł wyswietlamy w ramce
        title = data.get("title", "")
        print("\r" + ramka(title, 80), end="", flush=True)

        #przetwarzanie streszczenia na liste
        extract = data.get("extract", "")
        slowa = selekcja(extract)
        cnt.update(slowa)
        licznik_slow += len(slowa)
        pobrane += 1

        time.sleep(0.05)  # przerwa żeby nie spamować serwera

    print(f"\nPobrano: {pobrane}")
    print(f"#Słowa:  {licznik_slow}")
    print(f"Unikalne:  {len(cnt)}\n")

    print("Najczęstsze 15 słów:")
    for slowo, liczba in cnt.most_common(15):
        print(f"{slowo}: {liczba}")


if __name__ == "__main__":
    main()

