def count_vowels(value: str) -> int:
    """Count English vowels in a string, case-insensitively."""
    return sum(1 for ch in value.lower() if ch in 'aeiou')
