def second_largest(numbers: list[int]) -> int:
    """Return the second-largest unique number in a list."""
    unique = sorted(set(numbers), reverse=True)
    if len(unique) < 2:
        raise ValueError("at least two unique numbers are required")
    return unique[1]
