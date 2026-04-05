"""
Utility functions for password transformations and manipulations.
"""

import string
from .config import VOWELS

# Leet mapping
LEET_MAP = {'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '5', 't': '7', 'b': '8', 'g': '9', 'l': '1', 'z': '2'}

def leet(word: str) -> str:
    """Convert word to leet speak."""
    return ''.join(LEET_MAP.get(c.lower(), c) for c in word)

def altcaps(word: str) -> str:
    """Alternate capitalization in word."""
    return ''.join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(word))

def partial_leet(word: str) -> str:
    """Apply leet to first character only."""
    return leet(word[0]) + word[1:] if word else word

def no_vowels(word: str) -> str:
    """Remove vowels from word."""
    return ''.join(c for c in word if c not in VOWELS)

def only_vowels(word: str) -> str:
    """Keep only vowels from word."""
    return ''.join(c for c in word if c in VOWELS)

def only_consonants(word: str) -> str:
    """Keep only consonants from word."""
    return ''.join(c for c in word if c not in VOWELS and c.isalpha())

def reverse_word(word: str) -> str:
    """Reverse the word."""
    return word[::-1]

def capitalize_word(word: str) -> str:
    """Capitalize the word."""
    return word.capitalize()

def uppercase_word(word: str) -> str:
    """Convert to uppercase."""
    return word.upper()

def lowercase_word(word: str) -> str:
    """Convert to lowercase."""
    return word.lower()

def variants(word: str) -> list:
    """Generate all transformation variants of a word."""
    if not word:
        return []
    return [
        word,
        capitalize_word(word),
        uppercase_word(word),
        lowercase_word(word),
        leet(word),
        altcaps(word),
        no_vowels(word),
        reverse_word(word),
    ]