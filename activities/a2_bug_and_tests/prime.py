def is_prime(n: int) -> bool:
    """Return True if n is prime.

    ⚠️ Cette version contient volontairement un bug pour l'atelier.
    """
    if n <= 1:
        return True  # BUG: 0 et 1 ne sont pas premiers
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
