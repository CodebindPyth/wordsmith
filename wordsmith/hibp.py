"""
Have I Been Pwned API integration for checking email breaches.
"""

import time
import requests
from typing import Optional, List, Dict, Any
from .validators import is_valid_email

def check_email_hibp(email: str) -> Optional[bool]:
    """
    Check if an email has been involved in data breaches using HIBP API.
    
    Args:
        email: Email address to check
        
    Returns:
        True if breached, False if clean, None if error
    """
    try:
        response = requests.get(
            f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}",
            headers={"User-Agent": "WordSmith/1.0.0"},
            timeout=5
        )
        if response.status_code == 200:
            breaches = response.json()
            print(f"[!] {email} has been found in {len(breaches)} breach(es):")
            for breach in breaches:
                print(f"    - {breach['Name']} ({breach['BreachDate']})")
            return True
        elif response.status_code == 404:
            print(f"[+] {email} is CLEAN (not found in known breaches)")
            return False
        else:
            print(f"[-] API Error: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"[-] Connection error: {str(e)}")
        return None

def batch_check_emails_hibp(emails: List[str]) -> Dict[str, int]:
    """
    Check multiple emails for breaches with rate limiting.
    
    Args:
        emails: List of email addresses to check
        
    Returns:
        Dictionary with counts of pwned, clean, and errors
    """
    pwned_count = 0
    clean_count = 0
    error_count = 0
    
    print(f"[*] Checking {len(emails)} emails...")
    
    for email in emails:
        if is_valid_email(email):
            result = check_email_hibp(email)
            if result is True:
                pwned_count += 1
            elif result is False:
                clean_count += 1
            else:
                error_count += 1
            time.sleep(2)  # Rate limiting
        else:
            print(f"[-] Invalid format: {email}")
            error_count += 1
    
    print(f"\n[*] Summary: {pwned_count} pwned, {clean_count} clean, {error_count} errors")
    return {"pwned": pwned_count, "clean": clean_count, "errors": error_count}