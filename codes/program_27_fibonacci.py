def fibonacci(count: int) -> list[int]:
    """Return the first count Fibonacci numbers, starting with 0, 1."""
    if isinstance(count, bool) or not isinstance(count, int):
        raise TypeError("count must be an integer")
    if count < 0:
        raise ValueError("count must be non-negative")
    sequence = []
    a, b = 0, 1
    for _ in range(count):
        sequence.append(a)
        a, b = b, a + b
    return sequence
