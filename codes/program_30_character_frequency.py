def character_frequency(value: str) -> dict[str, int]:
    """Return character counts, preserving case and spaces."""
    counts: dict[str, int] = {}
    for char in value:
        counts[char] = counts.get(char, 0) + 1
    return counts
