def is_palindrome(value: str) -> bool:
    """Check a string as a palindrome, ignoring case and non-alphanumerics."""
    cleaned = ''.join(ch.lower() for ch in value if ch.isalnum())
    return cleaned == cleaned[::-1]
