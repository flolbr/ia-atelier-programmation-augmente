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

    print("Guess the number (between 1 and 100). Type 'q' to quit.")
    while True:
        raw = input("Your guess? ").strip()
        if raw.lower() in {"q", "quit", "exit"}:
            print("Bye.")
            return

        n = parse_int(raw)
        if n is None:
            print("Enter an integer (or 'q' to quit).")
            continue

        attempts += 1
        if n < secret:
            print("Higher!")
        elif n > secret:
            print("Lower!")
        else:
            print(f"Found in {attempts} attempt(s).")
            return


if __name__ == "__main__":
    play()
