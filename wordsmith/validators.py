"""
Validation functions for emails and phone numbers.
"""

import re
import phonenumbers

def is_valid_email(email: str) -> bool:
    """
    Validate email format using regex.
    
    Args:
        email: Email address to validate
        
    Returns:
        True if valid format, False otherwise
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def is_valid_phone(phone: str) -> bool:
    """
    Validate phone number using phonenumbers library.
    
    Args:
        phone: Phone number with country code to validate
        
    Returns:
        True if valid number, False otherwise
    """
    try:
        parsed = phonenumbers.parse(phone, None)
        return phonenumbers.is_valid_number(parsed)
    except:
        return False