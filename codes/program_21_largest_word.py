def largest_word(sentence: str) -> str:
    """Return the longest word in a sentence; ties keep the first word."""
    words = sentence.split()
    if not words:
        return ""
    return max(words, key=len)
