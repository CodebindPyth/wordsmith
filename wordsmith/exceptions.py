"""
Custom exceptions for WordSmith.
"""

class WordSmithError(Exception):
    """Base exception for WordSmith errors."""
    pass

class ValidationError(WordSmithError):
    """Raised when validation fails."""
    pass

class APIError(WordSmithError):
    """Raised when API calls fail."""
    pass

class FileNotFoundError(WordSmithError):
    """Raised when required files are not found."""
    pass