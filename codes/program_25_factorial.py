def factorial(n: int) -> int:
    """Return n! for a non-negative integer."""
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for number in range(2, n + 1):
        result *= number
    return result
