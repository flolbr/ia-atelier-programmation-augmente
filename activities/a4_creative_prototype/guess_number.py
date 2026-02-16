import random

def parse_int(s: str) -> int | None:
    """Return int if s looks like an integer, else None."""
    try:
        return int(s)
    except ValueError:
        return None

def play() -> None:
    """Console game: guess the number (1..100)."""
    secret = random.randint(1, 100)
    attempts = 0

    print("🎯 Devine le nombre (entre 1 et 100). Tape 'q' pour quitter.")
    while True:
        raw = input("Ton nombre ? ").strip()
        if raw.lower() in {"q", "quit", "exit"}:
            print("À bientôt !")
            return

        n = parse_int(raw)
        if n is None:
            print("➡️ Entre un nombre entier (ou 'q' pour quitter).")
            continue

        attempts += 1
        if n < secret:
            print("Plus grand !")
        elif n > secret:
            print("Plus petit !")
        else:
            print(f"✅ Bravo ! Trouvé en {attempts} essai(s).")
            return

if __name__ == "__main__":
    play()
