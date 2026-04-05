"""
Password generation module for WordSmith.
"""

import os
import random
import string
from itertools import permutations
from typing import Set, List, Optional
from .config import SEPARATORS, COMMON_SUFFIXES, KEYBOARD_PATTERNS, SEPARATOR_NUMBERS, SPECIAL_CHARS, EXTENDED_KEYBOARD, MONTHS_EN
from .utils import leet, altcaps, no_vowels, only_consonants, variants, reverse_word, capitalize_word, uppercase_word, lowercase_word

class PasswordGenerator:
    """
    Advanced password generator with extensive combination patterns.
    """
    
    def __init__(self):
        self.combos: Set[str] = set()
    
    def add_combo(self, value: str):
        """Add a password combination to the set."""
        if value:
            self.combos.add(value)
    
    def add_variants(self, word: str):
        """Add all transformation variants of a word."""
        for v in variants(word):
            self.add_combo(v)
    
    def add_pair(self, a: str, b: str):
        """Add combinations of two words with separators and numbers."""
        if not a or not b:
            return
        self.add_combo(a + b)
        self.add_combo(b + a)
        self.add_combo(capitalize_word(a) + capitalize_word(b))
        self.add_combo(capitalize_word(b) + capitalize_word(a))
        for sep in SEPARATORS:
            self.add_combo(f"{a}{sep}{b}")
            self.add_combo(f"{b}{sep}{a}")
            for num in SEPARATOR_NUMBERS:
                self.add_combo(f"{a}{sep}{b}{sep}{num}")
                self.add_combo(f"{a}{sep}{num}{sep}{b}")
                self.add_combo(f"{num}{sep}{a}{sep}{b}")
    
    def add_field(self, field: str):
        """Add combinations for a single field."""
        if not field:
            return
        self.add_variants(field)
        for suffix in COMMON_SUFFIXES:
            self.add_combo(field + suffix)
            self.add_combo(suffix + field)
        for num in SEPARATOR_NUMBERS:
            self.add_combo(field + num)
            self.add_combo(num + field)
    
    def generate_passwords(self, 
                          first_name: str, 
                          last_name: str, 
                          password_length: int,
                          keyword: str = "",
                          partner: str = "",
                          birthday: Optional[tuple] = None,  # (day, month, year)
                          job: str = "",
                          pet: str = "",
                          kids: str = "",
                          city: str = "",
                          lucky_number: str = "",
                          phone: str = "",
                          counter_range: int = 100) -> List[str]:
        """
        Generate comprehensive password list based on provided information.
        
        Args:
            first_name: Target's first name
            last_name: Target's last name
            password_length: Desired password length (currently not strictly enforced)
            keyword: Keyword/interests
            partner: Partner's name
            birthday: Tuple of (day, month, year) or None
            job: Job title
            pet: Pet's name
            kids: Children's names
            city: City or zipcode
            lucky_number: Lucky number
            phone: Phone number
            counter_range: Range for counter-based combinations
            
        Returns:
            List of unique generated passwords
        """
        self.combos.clear()
        
        # Basic fields
        extra_fields = [f for f in [pet, kids, partner, keyword, job, city] if f]
        all_fields = [first_name, last_name] + extra_fields
        all_fields = [f for f in all_fields if f]
        
        initial = first_name[0]
        last_initial = last_name[0]
        
        # Add basic field combinations
        for field in all_fields:
            self.add_field(field)
        
        # Add pairs
        self.add_pair(first_name, last_name)
        if keyword:
            self.add_pair(first_name, keyword)
            self.add_pair(last_name, keyword)
        if partner:
            self.add_pair(first_name, partner)
            self.add_pair(last_name, partner)
        if pet:
            self.add_pair(first_name, pet)
            self.add_pair(last_name, pet)
        if job:
            self.add_pair(first_name, job)
            self.add_pair(last_name, job)
        if city:
            self.add_pair(first_name, city)
            self.add_pair(last_name, city)
        
        # Permutations of fields
        for a, b in permutations(all_fields, 2):
            self.add_pair(a, b)
            for sep in SEPARATORS:
                for num in SEPARATOR_NUMBERS:
                    self.add_combo(f"{a}{sep}{b}{sep}{num}")
                    self.add_combo(f"{num}{sep}{a}{sep}{b}")
                    if keyword:
                        self.add_combo(f"{a}{sep}{b}{sep}{keyword}")
                        self.add_combo(f"{keyword}{sep}{a}{sep}{b}")
        
        # Special character combinations
        for sp in ["!", "@", "#", "$"]:
            for num in ["1", "12", "123", "1234", "007", "69"]:
                self.add_combo(f"{capitalize_word(first_name)}{sp}{num}")
                self.add_combo(f"{capitalize_word(last_name)}{sp}{num}")
                self.add_combo(f"{capitalize_word(first_name)}{sp}{num}{sp}{last_name}")
                self.add_combo(f"{capitalize_word(last_name)}{sp}{num}{sp}{first_name}")
                if keyword:
                    self.add_combo(f"{first_name}{sp}{keyword}{sp}{num}")
                    self.add_combo(f"{keyword}{sp}{first_name}{sp}{num}")
                if partner:
                    self.add_combo(f"{first_name}{sp}{partner}{sp}{num}")
                    self.add_combo(f"{partner}{sp}{first_name}{sp}{num}")
        
        # Counter-based combinations
        for i in range(counter_range):
            for field in [first_name, last_name, keyword, partner, pet, kids, job, city]:
                if field:
                    self.add_combo(f"{field}{i}")
                    self.add_combo(f"{i}{field}")
            for sep in SEPARATORS:
                self.add_combo(f"{first_name}{sep}{i}")
                self.add_combo(f"{last_name}{sep}{i}")
                self.add_combo(f"{first_name}{sep}{last_name}{sep}{i}")
                self.add_combo(f"{first_name}{sep}{i}{sep}{last_name}")
                self.add_combo(f"{i}{sep}{first_name}{sep}{last_name}")
                self.add_combo(f"{capitalize_word(first_name)}{sep}{capitalize_word(last_name)}{sep}{i}")
                if keyword:
                    self.add_combo(f"{first_name}{sep}{keyword}{sep}{i}")
                    self.add_combo(f"{keyword}{sep}{first_name}{sep}{i}")
                if partner:
                    self.add_combo(f"{first_name}{sep}{partner}{sep}{i}")
                    self.add_combo(f"{partner}{sep}{first_name}{sep}{i}")
                if pet:
                    self.add_combo(f"{first_name}{sep}{pet}{sep}{i}")
                    self.add_combo(f"{pet}{sep}{first_name}{sep}{i}")
        
        # Additional patterns
        self.add_combo(first_name + first_name)
        self.add_combo(last_name + last_name)
        self.add_combo(first_name + first_name + last_name)
        self.add_combo(reverse_word(first_name))
        self.add_combo(reverse_word(last_name))
        self.add_combo(reverse_word(first_name) + reverse_word(last_name))
        self.add_combo(initial + last_name)
        self.add_combo(initial + "." + last_name)
        self.add_combo(first_name + last_initial)
        self.add_combo(initial + capitalize_word(last_name))
        self.add_combo(first_name[0].upper() + first_name[1:-1] + first_name[-1].upper())
        
        # Padding patterns
        for pad in ["01", "001", "0001"]:
            self.add_combo(first_name + pad)
            self.add_combo(capitalize_word(first_name) + pad)
            self.add_combo(last_name + pad)
        
        # Year-based combinations
        for year in range(1960, 2010):
            self.add_combo(first_name + str(year))
            self.add_combo(last_name + str(year))
            self.add_combo(capitalize_word(first_name) + str(year))
        
        # Keyboard patterns
        for pattern in KEYBOARD_PATTERNS:
            for base in [first_name, last_name, capitalize_word(first_name), capitalize_word(last_name), uppercase_word(first_name), uppercase_word(last_name)]:
                self.add_combo(base + pattern)
                self.add_combo(pattern + base)
            self.add_combo(leet(pattern))
            self.add_combo(first_name + leet(pattern))
        
        # Half combinations
        half = len(first_name) // 2
        self.add_combo(first_name[:half] + last_name)
        self.add_combo(first_name[:half] + last_name[:half])
        self.add_combo(first_name + last_name[:half])
        
        # Pet-specific combinations
        if pet:
            for base in [pet, capitalize_word(pet), first_name + pet, pet + first_name, capitalize_word(first_name) + capitalize_word(pet), capitalize_word(pet) + capitalize_word(first_name), leet(pet), altcaps(pet)]:
                self.add_combo(base)
                for suffix in COMMON_SUFFIXES:
                    self.add_combo(base + suffix)
            for i in range(counter_range):
                self.add_combo(pet + str(i))
                self.add_combo(capitalize_word(pet) + str(i))
                self.add_combo(first_name + pet + str(i))
            for sep in SEPARATORS:
                self.add_combo(f"{first_name}{sep}{pet}")
                self.add_combo(f"{last_name}{sep}{pet}")
            self.add_combo(no_vowels(first_name) + pet)
            self.add_combo(leet(first_name) + "@1")
        
        # Kids-specific combinations
        if kids:
            for base in [kids, capitalize_word(kids), first_name + kids, kids + first_name, capitalize_word(first_name) + capitalize_word(kids), leet(kids), altcaps(kids)]:
                self.add_combo(base)
                for suffix in COMMON_SUFFIXES:
                    self.add_combo(base + suffix)
            for i in range(counter_range):
                self.add_combo(kids + str(i))
                self.add_combo(capitalize_word(kids) + str(i))
                self.add_combo(first_name + kids + str(i))
        
        # Job-specific combinations
        if job:
            for base in [job, capitalize_word(job), first_name + job, job + first_name, leet(job), altcaps(job)]:
                self.add_combo(base)
                for suffix in COMMON_SUFFIXES:
                    self.add_combo(base + suffix)
            for i in range(counter_range):
                self.add_combo(job + str(i))
                self.add_combo(capitalize_word(job) + str(i))
                self.add_combo(first_name + job + str(i))
        
        # Partner-specific combinations
        if partner:
            for base in [partner, capitalize_word(partner), first_name + partner, partner + first_name, capitalize_word(first_name) + capitalize_word(partner), capitalize_word(partner) + capitalize_word(first_name), leet(partner), altcaps(partner)]:
                self.add_combo(base)
                for suffix in COMMON_SUFFIXES:
                    self.add_combo(base + suffix)
            for i in range(counter_range):
                self.add_combo(partner + str(i))
                self.add_combo(first_name + partner + str(i))
                self.add_combo(partner + first_name + str(i))
            for sep in SEPARATORS:
                self.add_combo(f"{first_name}{sep}{partner}")
                self.add_combo(f"{partner}{sep}{first_name}")
            if birthday:
                day, month, year = birthday
                self.add_combo(partner + year)
                self.add_combo(first_name + partner + year)
        
        # Keyword-specific combinations
        if keyword:
            for base in [keyword, capitalize_word(keyword), keyword.upper(), first_name + keyword, keyword + first_name, leet(keyword), altcaps(keyword)]:
                self.add_combo(base)
                for suffix in COMMON_SUFFIXES:
                    self.add_combo(base + suffix)
            for i in range(counter_range):
                self.add_combo(keyword + str(i))
                self.add_combo(first_name + keyword + str(i))
            for sep in SEPARATORS:
                self.add_combo(f"{first_name}{sep}{keyword}")
                self.add_combo(f"{keyword}{sep}{first_name}")
        
        # City-specific combinations
        if city:
            for base in [city, capitalize_word(city), first_name + city, city + first_name, capitalize_word(first_name) + capitalize_word(city), leet(city)]:
                self.add_combo(base)
                for suffix in COMMON_SUFFIXES:
                    self.add_combo(base + suffix)
            for sep in SEPARATORS:
                self.add_combo(f"{first_name}{sep}{city}")
        
        # Lucky number combinations
        if lucky_number:
            for base in [first_name, last_name, capitalize_word(first_name), capitalize_word(last_name)]:
                self.add_combo(base + lucky_number)
                self.add_combo(lucky_number + base)
            if pet:
                self.add_combo(pet + lucky_number)
            if partner:
                self.add_combo(partner + lucky_number)
        
        # Phone-based combinations
        if phone:
            self.add_combo(phone)
            self.add_combo(first_name + phone)
            self.add_combo(first_name + phone[-4:])
            self.add_combo(first_name + phone[-6:])
            self.add_combo(last_name + phone[-4:])
            self.add_combo(phone[-4:] + first_name)
            self.add_combo(phone[:4] + first_name)
            for sep in SEPARATORS:
                self.add_combo(f"{first_name}{sep}{phone[-4:]}")
                self.add_combo(f"{last_name}{sep}{phone[-4:]}")
                self.add_combo(f"{phone[-4:]}{sep}{first_name}")
        
        # Advanced transformations
        for field in all_fields:
            if field and len(field) > 1:
                self.add_combo(only_consonants(field))
                self.add_combo(only_vowels(field))
                self.add_combo(no_vowels(field))
                self.add_combo(leet(field))
                self.add_combo(altcaps(field))
                self.add_combo(field + no_vowels(field))
                self.add_combo(no_vowels(field) + field)
                self.add_combo(leet(reverse_word(field)))
                self.add_combo(altcaps(reverse_word(field)))
        
        # Complex combinations with separators and numbers
        for l_field in [first_name, last_name, keyword]:
            if l_field:
                for r_field in [pet, partner, kids]:
                    if r_field:
                        for sep in SEPARATORS[:8]:
                            for num in SEPARATOR_NUMBERS[:8]:
                                self.add_combo(f"{l_field}{sep}{r_field}{sep}{num}")
                                self.add_combo(f"{num}{sep}{l_field}{sep}{r_field}")
                                self.add_combo(f"{leet(l_field)}{sep}{r_field}{sep}{num}")
                                self.add_combo(f"{l_field}{sep}{leet(r_field)}{sep}{num}")
        
        # Special character patterns
        for combo_base in [first_name + last_name, last_name + first_name]:
            self.add_combo(leet(combo_base))
            self.add_combo(altcaps(combo_base))
            self.add_combo(no_vowels(combo_base))
            self.add_combo(only_consonants(combo_base))
            for sep in SEPARATORS:
                self.add_combo(leet(first_name) + sep + leet(last_name))
                self.add_combo(altcaps(first_name) + sep + altcaps(last_name))
        
        # More complex patterns with special chars
        for sp in SPECIAL_CHARS:
            for num in SEPARATOR_NUMBERS:
                for field in [first_name, last_name, keyword]:
                    if field:
                        self.add_combo(field + sp + reverse_word(field) + sp + num)
                        self.add_combo(num + sp + field + sp + uppercase_word(field))
                        self.add_combo(leet(field) + sp + num + sp + altcaps(field))
                        self.add_combo(altcaps(field) + sp + leet(field) + sp + num)
        
        # Birthday-based combinations
        if birthday:
            day, month, year = birthday
            month_word = MONTHS_EN[int(month) - 1]
            date_values = [
                day + month + year,
                month + day + year,
                year + month + day,
                year + day + month,
                day + month_word,
                month_word + day,
                month_word + year,
                capitalize_word(month_word) + year,
                year[-2:] + month_word,
                year[-2:] + day + month,
            ]
            for combo in date_values:
                self.add_combo(combo)
                self.add_combo(first_name + combo)
                self.add_combo(last_name + combo)
            for sep in SEPARATORS:
                self.add_combo(f"{first_name}{sep}{day}{month}{year}")
                self.add_combo(f"{first_name}{sep}{year}")
            for field in [pet, kids, job, partner]:
                if field:
                    self.add_combo(field + year)
                    self.add_combo(field + day + month)
                    self.add_combo(field + month + year)
        
        # Additional birthday combinations
        if birthday and partner:
            day, month, year = birthday
            self.add_combo(partner + year[-2:])
            self.add_combo(partner + month_word)
        
        # More permutations and patterns
        for i in range(1, min(counter_range, 100)):
            self.add_combo(first_name + str(i).zfill(2))
            self.add_combo(first_name + str(i).zfill(3))
            self.add_combo(first_name + str(i).zfill(4))
            self.add_combo(last_name + str(i).zfill(2))
            self.add_combo(last_name + str(i).zfill(3))
        
        # Complex birthday patterns
        if birthday:
            day, month, year = birthday
            month_word = MONTHS_EN[int(month) - 1]
            for a, b in [(first_name, day), (day, first_name), (first_name, month), (month, first_name)]:
                if a and b:
                    for sep in SEPARATORS[:8]:
                        for suffix in COMMON_SUFFIXES[:8]:
                            self.add_combo(f"{a}{sep}{b}{suffix}")
                            self.add_combo(f"{suffix}{a}{sep}{b}")
                            self.add_combo(f"{leet(a)}{sep}{b}{suffix}")
        
        # Triple combinations
        for a, b, c in [(first_name, last_name, keyword),
                        (first_name, keyword, last_name),
                        (keyword, first_name, last_name),
                        (first_name, pet, last_name),
                        (last_name, partner, first_name)]:
            if a and b and c:
                for sep in SEPARATORS[:5]:
                    self.add_combo(f"{leet(a)}{sep}{altcaps(b)}{sep}{no_vowels(c)}")
                    self.add_combo(f"{altcaps(a)}{sep}{leet(b)}{sep}{altcaps(c)}")
                    self.add_combo(f"{no_vowels(a)}{sep}{b}{sep}{leet(c)}")
                    self.add_combo(f"{a}{sep}{b}{sep}{c}")
                    self.add_combo(f"{c}{sep}{b}{sep}{a}")
        
        # Substring combinations
        for field in all_fields:
            if field and len(field) >= 3:
                half = len(field) // 2
                self.add_combo(field[:half] + leet(field[half:]))
                self.add_combo(altcaps(field[:half]) + field[half:])
                self.add_combo(field[:half] + uppercase_word(field[half:]))
                self.add_combo(leet(field[:half]) + no_vowels(field[half:]))
                for num in SEPARATOR_NUMBERS[:5]:
                    self.add_combo(field[:half] + num + field[half:])
                    self.add_combo(num + field[:half:] + field[half:])
        
        # Special character insertions
        for field in all_fields:
            if field:
                for sp in SPECIAL_CHARS:
                    self.add_combo(field + sp)
                    self.add_combo(sp + field)
                    self.add_combo(field[0] + sp + field)
                    self.add_combo(field + sp + field[0])
                    for num in SEPARATOR_NUMBERS[-3:]:
                        self.add_combo(f"{field}{sp}{num}")
                        self.add_combo(f"{num}{sp}{field}")
        
        # Case variations
        for field in all_fields:
            if field:
                self.add_combo(uppercase_word(field))
                self.add_combo(lowercase_word(field))
                self.add_combo(capitalize_word(field) * 2)
                self.add_combo(field[0].upper() + field[1:].lower())
                self.add_combo(field[0].lower() + field[1:].upper())
                if len(field) > 2:
                    self.add_combo(field[0] + field[-1] + field[1:-1])
                    self.add_combo(field[-1] + field[:-1])
                    self.add_combo(field[1:] + field[0])
                    for idx in range(len(field)):
                        if idx > 0 and idx < len(field) - 1:
                            self.add_combo(field[:idx] + field[idx:].upper())
                            self.add_combo(field[:idx].upper() + field[idx:])
        
        # Keyboard pattern extensions
        for kb_pattern in KEYBOARD_PATTERNS:
            for field in [first_name, last_name, keyword, pet]:
                if field:
                    self.add_combo(field + kb_pattern)
                    self.add_combo(kb_pattern + field)
                    self.add_combo(leet(field) + kb_pattern)
                    self.add_combo(kb_pattern + leet(field))
                    self.add_combo(field + kb_pattern + field)
                    for sep in SEPARATORS[:4]:
                        self.add_combo(f"{field}{sep}{kb_pattern}")
                        self.add_combo(f"{kb_pattern}{sep}{field}")
        
        # Quadruple combinations
        for a, b, c, d in [(first_name, last_name, keyword, pet),
                           (first_name, keyword, partner, last_name),
                           (last_name, first_name, kids, job)]:
            if a and b and c and d:
                for sep1, sep2, sep3 in [(SEPARATORS[i], SEPARATORS[j], SEPARATORS[k]) for i in range(min(3, len(SEPARATORS))) for j in range(min(3, len(SEPARATORS))) for k in range(min(3, len(SEPARATORS)))]:
                    self.add_combo(f"{leet(a)}{sep1}{altcaps(b)}{sep2}{no_vowels(c)}{sep3}{d}")
                    self.add_combo(f"{a}{sep1}{b}{sep2}{c}{sep3}{d}")
                    self.add_combo(f"{d}{sep3}{c}{sep2}{b}{sep1}{a}")
        
        # Number combinations
        for field in all_fields:
            if field:
                for num in SEPARATOR_NUMBERS:
                    self.add_combo(field + num)
                    self.add_combo(num + field)
                    self.add_combo(field + num + field)
                    self.add_combo(num + field + num)
                    self.add_combo(leet(field) + num)
                    self.add_combo(num + leet(field))
                    for ch in SPECIAL_CHARS:
                        self.add_combo(f"{field}{ch}{num}")
                        self.add_combo(f"{num}{ch}{field}")
                        self.add_combo(f"{field}{ch}{num}{ch}{field}")
        
        # Field pair transformations
        for field1 in all_fields:
            for field2 in all_fields:
                if field1 and field2 and field1 != field2:
                    self.add_combo(uppercase_word(field1) + lowercase_word(field2))
                    self.add_combo(lowercase_word(field1) + uppercase_word(field2))
                    self.add_combo(leet(field1) + field2)
                    self.add_combo(field1 + leet(field2))
                    self.add_combo(field1 + field2 + field1)
                    self.add_combo(field2 + field1 + field2)
                    self.add_combo(reverse_word(field1) + field2)
                    self.add_combo(field1 + reverse_word(field2))
                    self.add_combo(reverse_word(field1) + reverse_word(field2))
                    for num in ["2024", "2023", "2025", "2026"]:
                        self.add_combo(field1 + num + field2)
                        self.add_combo(field2 + num + field1)
        
        # Substring extractions
        for field in all_fields:
            if field and len(field) > 2:
                for i in range(len(field)):
                    for j in range(i+1, len(field)+1):
                        sub = field[i:j]
                        self.add_combo(sub)
                        self.add_combo(sub + first_name)
                        self.add_combo(first_name + sub)
                        if len(sub) > 1:
                            self.add_combo(leet(sub))
                            self.add_combo(altcaps(sub))
        
        # Bracket patterns
        for bracket_pair in [("(", ")"), ("{", "}"), ("[", "]"), ("<", ">"), ("'", "'"), ('"', '"')]:
            for field in [first_name, last_name, keyword]:
                if field:
                    self.add_combo(f"{bracket_pair[0]}{field}{bracket_pair[1]}")
                    self.add_combo(f"{bracket_pair[0]}{uppercase_word(field)}{bracket_pair[1]}")
                    self.add_combo(f"{bracket_pair[0]}{leet(field)}{bracket_pair[1]}")
                    for num in SEPARATOR_NUMBERS[:5]:
                        self.add_combo(f"{bracket_pair[0]}{field}{num}{bracket_pair[1]}")
        
        # Repetition patterns
        for mul in range(2, 4):
            for field in all_fields:
                if field:
                    self.add_combo(field * mul)
                    self.add_combo((field[0] * mul) + field[1:] if len(field) > 1 else field)
                    self.add_combo(field + (field[-1] * (mul-1)))
                    for num in SEPARATOR_NUMBERS[:3]:
                        self.add_combo((field + num) * mul)
        
        # Birthday permutations
        if birthday:
            day, month, year = birthday
            month_word = MONTHS_EN[int(month) - 1]
            for perm in permutations([day, month, year[:2], first_name, last_name], 2):
                if perm[0] and perm[1]:
                    for sep in SEPARATORS[:6]:
                        self.add_combo(f"{perm[0]}{sep}{perm[1]}")
                        self.add_combo(f"{leet(perm[0]) if perm[0] != month else perm[0]}{sep}{perm[1]}")
        
        # Year ranges
        for field in all_fields:
            if field:
                for y in range(1960, 2026):
                    self.add_combo(field + str(y))
                    self.add_combo(str(y) + field)
                    for month in range(1, 13):
                        self.add_combo(field + str(month).zfill(2) + str(y % 100))
                        self.add_combo(str(month).zfill(2) + field + str(y % 100))
        
        # Counter thousands
        for field in all_fields:
            if field:
                for i in range(1000):
                    if i % 100 == 0:
                        self.add_combo(field + str(i))
                        self.add_combo(str(i) + field)
                        self.add_combo(field + str(i).zfill(4))
                        self.add_combo(str(i).zfill(4) + field)
        
        # Special char combinations
        for sp in SPECIAL_CHARS:
            for field1 in all_fields:
                for field2 in all_fields:
                    if field1 and field2:
                        self.add_combo(f"{leet(field1)}{sp}{altcaps(field2)}")
                        self.add_combo(f"{altcaps(field1)}{sp}{no_vowels(field2)}")
                        self.add_combo(f"{no_vowels(field1)}{sp}{leet(field2)}")
                        self.add_combo(f"{reverse_word(field1)}{sp}{reverse_word(field2)}")
                        self.add_combo(f"{uppercase_word(field1)}{sp}{lowercase_word(field2)}")
        
        # Extended keyboard patterns
        for kb in EXTENDED_KEYBOARD:
            for field in all_fields:
                if field:
                    self.add_combo(leet(kb) + field)
                    self.add_combo(field + leet(kb))
                    self.add_combo(altcaps(kb) + field)
                    self.add_combo(field + altcaps(kb))
                    self.add_combo(field + kb + field)
                    self.add_combo(kb + leet(field) + kb)
        
        # Substring advanced
        for field in all_fields:
            if field and len(field) > 2:
                for i in range(len(field)):
                    for j in range(i+2, len(field)+1):
                        sub = field[i:j]
                        if len(sub) > 1:
                            self.add_combo(leet(sub) + first_name)
                            self.add_combo(sub + leet(first_name))
                            self.add_combo(altcaps(sub) + last_name)
                            self.add_combo(no_vowels(sub) + keyword if keyword else first_name)
                            for num in SEPARATOR_NUMBERS:
                                self.add_combo(sub + num)
        
        # Field pair limits
        all_field_pairs = [(a, b) for a in all_fields for b in all_fields if a and b]
        for (f1, f2) in all_field_pairs[:50]:
            for sep in SEPARATORS:
                self.add_combo(f"{leet(f1)}{sep}{leet(f2)}")
                self.add_combo(f"{altcaps(f1)}{sep}{altcaps(f2)}")
                self.add_combo(f"{uppercase_word(f1)}{sep}{lowercase_word(f2)}")
                self.add_combo(f"{no_vowels(f1)}{sep}{no_vowels(f2)}")
                for num in SEPARATOR_NUMBERS[:5]:
                    self.add_combo(f"{f1}{sep}{f2}{sep}{num}")
                    self.add_combo(f"{leet(f1)}{sep}{f2}{sep}{leet(num)}")
        
        # Special char brackets
        for field in all_fields:
            if field:
                for sp1 in SPECIAL_CHARS:
                    for sp2 in SPECIAL_CHARS:
                        self.add_combo(f"{sp1}{field}{sp2}")
                        self.add_combo(f"{sp1}{leet(field)}{sp2}")
                        self.add_combo(f"{sp1}{altcaps(field)}{sp2}")
                        self.add_combo(f"{sp1}{no_vowels(field)}{sp2}")
                        self.add_combo(f"{sp1}{field}{sp1}{field}{sp2}")
        
        # Repetition ranges
        for i in range(2, 6):
            for field in all_fields:
                if field:
                    repeated = field * i
                    self.add_combo(repeated)
                    self.add_combo(leet(field) * i)
                    self.add_combo(altcaps(field) * i)
                    self.add_combo((field[0] * 2) + field[1:] if len(field) > 1 else field)
                    self.add_combo(field + (field[-1] * (i-1)))
                    self.add_combo((field[0] * i) + field if len(field) > 1 else field)
        
        # Triple separators
        for triples in [(first_name, last_name, keyword),
                        (keyword, first_name, pet),
                        (partner, last_name, first_name),
                        (first_name, pet, kids),
                        (last_name, keyword, job)]:
            if all(triples):
                for i in range(len(SEPARATORS)):
                    for j in range(len(SEPARATORS)):
                        sep1 = SEPARATORS[i]
                        sep2 = SEPARATORS[j]
                        self.add_combo(f"{leet(triples[0])}{sep1}{altcaps(triples[1])}{sep2}{no_vowels(triples[2])}")
                        self.add_combo(f"{triples[0]}{sep1}{triples[1]}{sep2}{triples[2]}")
                        self.add_combo(f"{triples[2]}{sep2}{triples[1]}{sep1}{triples[0]}")
                        self.add_combo(f"{altcaps(triples[0])}{sep1}{no_vowels(triples[1])}{sep2}{leet(triples[2])}")
        
        # Date combinations
        if birthday:
            day, month, year = birthday
            month_word = MONTHS_EN[int(month) - 1]
            for y_val in ["2024", "2023", "2022", "2021", "2020", "2019"]:
                for m_val in ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]:
                    for d_val in ["01", "15", "30"]:
                        self.add_combo(field + d_val + m_val + y_val)
                        self.add_combo(d_val + m_val + y_val + field)
                        self.add_combo(y_val + m_val + d_val + field)
                        self.add_combo(field + y_val[-2:] + m_val + d_val)
        
        # Return sorted unique passwords
        return sorted(list(self.combos))
    
    def save_to_file(self, passwords: List[str], filename: str = "passwords.txt"):
        """Save generated passwords to a file."""
        with open(filename, "w") as f:
            for pwd in passwords:
                f.write(pwd + "\n")
        print(f"[+] Saved {len(passwords)} passwords to {filename}")
    
    def remove_duplicates(self, passwords: List[str]) -> List[str]:
        """Remove duplicate passwords from list."""
        return list(dict.fromkeys(passwords))