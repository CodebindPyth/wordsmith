"""
WordSmith - Advanced Password Generation and Validation Tool

A comprehensive tool for generating secure passwords, validating emails and phone numbers,
and checking for data breaches using the Have I Been Pwned API.
"""

from .generator import PasswordGenerator
from .validators import is_valid_email, is_valid_phone
from .hibp import check_email_hibp, batch_check_emails_hibp
from .cli import main

__version__ = "1.0.0"
__all__ = [
    "PasswordGenerator",
    "is_valid_email",
    "is_valid_phone",
    "check_email_hibp",
    "batch_check_emails_hibp",
    "main"
]