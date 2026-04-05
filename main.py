
import os, sys, time   
import string
import itertools
import random
import re
import hashlib
import requests
from itertools import permutations
from turtle import color
from phonenumbers import carrier
import phonenumbers
import argparse
from threading import Thread
from tqdm import tqdm
from pystyle import Colors, Colorate, Center
banner1 = """
                                                           ₁₀₁₀₁₀₁₀₁₀₁₀₁₀₁ ₀₁₀₁₀０１０１０１０１０010  1010101 0101010101 101010 0101 101"
                                       １０１０１ １０１０１０1010101 10101010 010101010₀₁₀₁ ₁₀₁₀₁₀₁₀₁ ₁₀₁₀₁₀₁ ₁₀₁₀₁₀₁₀₁₀₁₀₁"
              ₁₀₁₀₁₀₁₀₁₀₁₀₁₀₁₀₁₀₁₀₁₀₁₀₁₀１０１０１０１０１０１０１０１０１０１０１０１０１０１０１１０１０１５５"
                                       101010101010１０１０１０１０１０１０101010101010101010101010101010101010１０１０１０１０１０１１０１０１０１０１０１")
                                １０１０１０１1010101010  ██╗    ██╗ ██████╗ ██████╗ ██████╗ ███████╗███╗   ███╗██╗████████╗██╗  ██╗１０１０１０１０１０１１０１０１０１０１０１10101010101010101010101010101
                             ０１０１０10101010１０010    ██║    ██║██╔═══██╗██╔══██╗██╔══██╗██╔════╝████╗ ████║██║╚══██╔══╝██║  ██║１０１０１0101010101010101
                             ₁₀₁₀１０ 01010  ₁₀₁₀₁        ██║ █╗ ██║██║   ██║██████╔╝██║  ██║███████╗██╔████╔██║██║   ██║   ███████║10101010101010101010101010101
                                                   ₁₀₁₀₁  ██║███╗██║██║   ██║██╔══██╗██║  ██║╚════██║██║╚██╔╝██║██║   ██║   ██╔══██║１０１０１０１０１１０１
                                     01010                ╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝███████║██║ ╚═╝ ██║██║   ██║   ██║  ██║１０１０101010101010101
                                                           ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝     ╚═╝╚═╝   ╚═╝   ╚═╝  ╚═╝

                                                                                         CodebindPyth  &  jsvgd7g655
                                    101010101010１０１０１０１０１０１０10101010101010101010101010101010１０１０１０１０１０１１０１０１０１０１010001010101
                                        010101010₁₀₁₀₁₀₁₀₁₀₁₀₁₀₁₀₁₀₁₀₁₀101011010101010101010101１０１０１０１０１０１10101１10101１₁₀₁₀₁₀₁₀₁₀₁₀
                                              ₁₀₁₀₁₀₁₀₁₀₁₀₁₀₁₀₁₀₁₀₁₀₁₀₁₀₁₀₁₀₁₀₁₀₁₀₁₀₁₀₁₀₁₀₁₀₁₀₁₀₁₀₁₀₁₀₁₀₁₀₁₀₁₀₁₀₁₀₁₀₁₀₁₀₂101101010101
                                              """ 
banner = """                                            [ v1.0.0 ]
                                            [ STATUS: updated ] 


                                             DISCLAIMER

                         This software is provided for educational and research purposes only.

                        Use of this tool must comply with all applicable laws and regulations.

            The user is solely responsible for ensuring they have proper authorization before using this software.

        The author is not responsible for any misuse, damage, or legal consequences resulting from the use of this tool.




"""
print(banner1)
print(Colorate.Horizontal(Colors.green_to_yellow, Center.XCenter(banner)))



option = 6
while (option != "5"):
    print("                                                                                  1.generate a random password")
    print("                                                                                    2.generate a random email")
    print("                                                                                 3.generate a random phone number")
    print("                                                                                 4.validate phone/email or check HIBP")
    print("                                                                                               5.exit")
    option = input("                                                                                    give option: ")

    if option == "1":
      #inputs of user for wordlist
        nameTarget = input("give first name of target: ").strip()
        lastnameTarget = input("give last name of target: ").strip()
        passwordLength = int(input("give length of password: "))

        keyword_ans = input("keywords/interests? Y/n: ").strip()
        keywordTarget = input("give keyword (team, hobby, etc): ").strip() if keyword_ans in ("Y", "y") else ""

        partner_ans = input("partner name? Y/n: ").strip()
        partnerTarget = input("give partner name: ").strip() if partner_ans in ("Y", "y") else ""

        bday = input("birthday? Y/n: ").strip()
        if bday in ("Y", "y"):
            dayTarget = input("day (dd): ").strip()
            monthTarget = input("month (mm): ").strip()
            yearTarget = input("year (yyyy): ").strip()
        else:
            dayTarget = monthTarget = yearTarget = ""

        job = input("job? Y/n: ").strip()
        jobTarget = input("give job of target: ").strip() if job in ("Y", "y") else ""

        pet = input("pet? Y/n: ").strip()
        petTarget = input("give pet name of target: ").strip() if pet in ("Y", "y") else ""

        kids = input("kids? Y/n: ").strip()
        kidsTarget = input("give name of target's kids: ").strip() if kids in ("Y", "y") else ""

        city_ans = input("city/zipcode? Y/n: ").strip()
        cityTarget = input("give city or zipcode: ").strip() if city_ans in ("Y", "y") else ""

        lucky_ans = input("lucky number? Y/n: ").strip()
        luckyTarget = input("give lucky number: ").strip() if lucky_ans in ("Y", "y") else ""

        phone_ans = input("phone number? Y/n: ").strip()
        phoneTarget = input("give phone number: ").strip() if phone_ans in ("Y", "y") else ""

        range1 = int(input("give range of counter: "))

        print(f"file saved to: {os.getcwd()}/passwords.txt")

        
        leet_map = {'a':'4','e':'3','i':'1','o':'0','s':'5','t':'7','b':'8','g':'9','l':'1','z':'2'}
        def leet(word):
            return ''.join(leet_map.get(c.lower(), c) for c in word)

        def altcaps(word):
            return ''.join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(word))

        def partial_leet(word):
            return leet(word[0]) + word[1:] if word else word

        vowels = set("aeiouAEIOU" "αεηιουωΑΕΗΙΟΥΩ")
        def no_vowels(word):
            return ''.join(c for c in word if c not in vowels)
        def only_vowels(word):
            return ''.join(c for c in word if c in vowels)
        def only_consonants(word):
            return ''.join(c for c in word if c not in vowels and c.isalpha())
#custom seperators
        separators   = [".", "_", "-", "!", "@", "#", "$", "%", "^", "&", "*", "+", "=", "|", "~", ":"]
        common_suffixes = ["123","1234","12345","!","!!","123!","1!","@1","321",
                           "111","000","007","69","99","2024","2023","01","1","!@","@!","!#","@#","$%"]
        keyboard_patterns = ["qwerty","123456","password","qwerty123","abc123","letmein","welcome"]
        months_en = ["january","february","march","april","may","june",
                     "july","august","september","october","november","december"]
        separator_numbers = ["1","12","123","1234","2024","2023","007","69","99","321","01","55","77","88","99","55555"]
        special_chars = ["!", "@", "#", "$", "%", "^", "&", "*", "+", "="]
        extended_keyboard = ["qwerty","123456","password","qwerty123","abc123","letmein","welcome","admin","root","user","test","123123","111111","000000"]

        initial      = nameTarget[0]
        last_initial = lastnameTarget[0]

        # collect all non-empty extra fields for permutation combos
        extra_fields = [f for f in [petTarget, kidsTarget, partnerTarget,
                                     keywordTarget, jobTarget, cityTarget] if f]

        combos = set()

        def add_combo(value):
            if value:
                combos.add(value)

        def variants(word):
            if not word:
                return []
            return [
                word,
                word.capitalize(),
                word.upper(),
                word.lower(),
                leet(word),
                altcaps(word),
                no_vowels(word),
                word[::-1],
            ]

        def add_variants(word):
            for v in variants(word):
                add_combo(v)

        def add_pair(a, b):
            if not a or not b:
                return
            add_combo(a + b)
            add_combo(b + a)
            add_combo(a.capitalize() + b.capitalize())
            add_combo(b.capitalize() + a.capitalize())
            for sep in separators:
                add_combo(f"{a}{sep}{b}")
                add_combo(f"{b}{sep}{a}")
                for num in separator_numbers:
                    add_combo(f"{a}{sep}{b}{sep}{num}")
                    add_combo(f"{a}{sep}{num}{sep}{b}")
                    add_combo(f"{num}{sep}{a}{sep}{b}")

        def add_field(field):
            if not field:
                return
            add_variants(field)
            for suffix in common_suffixes:
                add_combo(field + suffix)
                add_combo(suffix + field)
            for num in separator_numbers:
                add_combo(field + num)
                add_combo(num + field)

        all_fields = [nameTarget, lastnameTarget] + extra_fields
        all_fields = [f for f in all_fields if f]

        for field in all_fields:
            add_field(field)

        add_pair(nameTarget, lastnameTarget)
        if keywordTarget:
            add_pair(nameTarget, keywordTarget)
            add_pair(lastnameTarget, keywordTarget)
        if partnerTarget:
            add_pair(nameTarget, partnerTarget)
            add_pair(lastnameTarget, partnerTarget)
        if petTarget:
            add_pair(nameTarget, petTarget)
            add_pair(lastnameTarget, petTarget)
        if jobTarget:
            add_pair(nameTarget, jobTarget)
            add_pair(lastnameTarget, jobTarget)
        if cityTarget:
            add_pair(nameTarget, cityTarget)
            add_pair(lastnameTarget, cityTarget)

        for a, b in permutations(all_fields, 2):
            add_pair(a, b)
            for sep in separators:
                for num in separator_numbers:
                    add_combo(f"{a}{sep}{b}{sep}{num}")
                    add_combo(f"{num}{sep}{a}{sep}{b}")
                    if keywordTarget:
                        add_combo(f"{a}{sep}{b}{sep}{keywordTarget}")
                        add_combo(f"{keywordTarget}{sep}{a}{sep}{b}")

        for sp in ["!", "@", "#", "$"]:
            for num in ["1", "12", "123", "1234", "007", "69"]:
                add_combo(f"{nameTarget.capitalize()}{sp}{num}")
                add_combo(f"{lastnameTarget.capitalize()}{sp}{num}")
                add_combo(f"{nameTarget.capitalize()}{sp}{num}{sp}{lastnameTarget}")
                add_combo(f"{lastnameTarget.capitalize()}{sp}{num}{sp}{nameTarget}")
                if keywordTarget:
                    add_combo(f"{nameTarget}{sp}{keywordTarget}{sp}{num}")
                    add_combo(f"{keywordTarget}{sp}{nameTarget}{sp}{num}")
                if partnerTarget:
                    add_combo(f"{nameTarget}{sp}{partnerTarget}{sp}{num}")
                    add_combo(f"{partnerTarget}{sp}{nameTarget}{sp}{num}")

        for i in range(range1):
            for field in [nameTarget, lastnameTarget, keywordTarget, partnerTarget, petTarget, kidsTarget, jobTarget, cityTarget]:
                if field:
                    add_combo(f"{field}{i}")
                    add_combo(f"{i}{field}")
            for sep in separators:
                add_combo(f"{nameTarget}{sep}{i}")
                add_combo(f"{lastnameTarget}{sep}{i}")
                add_combo(f"{nameTarget}{sep}{lastnameTarget}{sep}{i}")
                add_combo(f"{nameTarget}{sep}{i}{sep}{lastnameTarget}")
                add_combo(f"{i}{sep}{nameTarget}{sep}{lastnameTarget}")
                add_combo(f"{nameTarget.capitalize()}{sep}{lastnameTarget.capitalize()}{sep}{i}")
                if keywordTarget:
                    add_combo(f"{nameTarget}{sep}{keywordTarget}{sep}{i}")
                    add_combo(f"{keywordTarget}{sep}{nameTarget}{sep}{i}")
                if partnerTarget:
                    add_combo(f"{nameTarget}{sep}{partnerTarget}{sep}{i}")
                    add_combo(f"{partnerTarget}{sep}{nameTarget}{sep}{i}")
                if petTarget:
                    add_combo(f"{nameTarget}{sep}{petTarget}{sep}{i}")
                    add_combo(f"{petTarget}{sep}{nameTarget}{sep}{i}")

        add_combo(nameTarget + nameTarget)
        add_combo(lastnameTarget + lastnameTarget)
        add_combo(nameTarget + nameTarget + lastnameTarget)
        add_combo(nameTarget[::-1])
        add_combo(lastnameTarget[::-1])
        add_combo(nameTarget[::-1] + lastnameTarget[::-1])
        add_combo(initial + lastnameTarget)
        add_combo(initial + "." + lastnameTarget)
        add_combo(nameTarget + last_initial)
        add_combo(initial + lastnameTarget.capitalize())
        add_combo(nameTarget[0].upper() + nameTarget[1:-1] + nameTarget[-1].upper())

        for pad in ["01", "001", "0001"]:
            add_combo(nameTarget + pad)
            add_combo(nameTarget.capitalize() + pad)
            add_combo(lastnameTarget + pad)

        for year in range(1960, 2010):
            add_combo(nameTarget + str(year))
            add_combo(lastnameTarget + str(year))
            add_combo(nameTarget.capitalize() + str(year))

        for pattern in keyboard_patterns:
            for base in [nameTarget, lastnameTarget, nameTarget.capitalize(), lastnameTarget.capitalize(), nameTarget.upper(), lastnameTarget.upper()]:
                add_combo(base + pattern)
                add_combo(pattern + base)
            add_combo(leet(pattern))
            add_combo(nameTarget + leet(pattern))

        half = len(nameTarget) // 2
        add_combo(nameTarget[:half] + lastnameTarget)
        add_combo(nameTarget[:half] + lastnameTarget[:half])
        add_combo(nameTarget + lastnameTarget[:half])

        if petTarget:
            for base in [petTarget, petTarget.capitalize(), nameTarget + petTarget, petTarget + nameTarget, nameTarget.capitalize() + petTarget.capitalize(), petTarget.capitalize() + nameTarget.capitalize(), leet(petTarget), altcaps(petTarget)]:
                add_combo(base)
                for suffix in common_suffixes:
                    add_combo(base + suffix)
            for i in range(range1):
                add_combo(petTarget + str(i))
                add_combo(petTarget.capitalize() + str(i))
                add_combo(nameTarget + petTarget + str(i))
            for sep in separators:
                add_combo(f"{nameTarget}{sep}{petTarget}")
                add_combo(f"{lastnameTarget}{sep}{petTarget}")
            add_combo(no_vowels(nameTarget) + petTarget)
            add_combo(leet(nameTarget) + "@1")

        if kidsTarget:
            for base in [kidsTarget, kidsTarget.capitalize(), nameTarget + kidsTarget, kidsTarget + nameTarget, nameTarget.capitalize() + kidsTarget.capitalize(), leet(kidsTarget), altcaps(kidsTarget)]:
                add_combo(base)
                for suffix in common_suffixes:
                    add_combo(base + suffix)
            for i in range(range1):
                add_combo(kidsTarget + str(i))
                add_combo(kidsTarget.capitalize() + str(i))
                add_combo(nameTarget + kidsTarget + str(i))

        if jobTarget:
            for base in [jobTarget, jobTarget.capitalize(), nameTarget + jobTarget, jobTarget + nameTarget, leet(jobTarget), altcaps(jobTarget)]:
                add_combo(base)
                for suffix in common_suffixes:
                    add_combo(base + suffix)
            for i in range(range1):
                add_combo(jobTarget + str(i))
                add_combo(jobTarget.capitalize() + str(i))
                add_combo(nameTarget + jobTarget + str(i))

        if petTarget and kidsTarget:
            add_combo(petTarget + kidsTarget)
            add_combo(kidsTarget + petTarget)

        if bday in ("Y", "y"):
            month_word = months_en[int(monthTarget) - 1]
            date_values = [
                dayTarget + monthTarget + yearTarget,
                monthTarget + dayTarget + yearTarget,
                yearTarget + monthTarget + dayTarget,
                yearTarget + dayTarget + monthTarget,
                dayTarget + month_word,
                month_word + dayTarget,
                month_word + yearTarget,
                month_word.capitalize() + yearTarget,
                yearTarget[-2:] + month_word,
                yearTarget[-2:] + dayTarget + monthTarget,
            ]
            for combo in date_values:
                add_combo(combo)
                add_combo(nameTarget + combo)
                add_combo(lastnameTarget + combo)
            for sep in separators:
                add_combo(f"{nameTarget}{sep}{dayTarget}{monthTarget}{yearTarget}")
                add_combo(f"{nameTarget}{sep}{yearTarget}")
            for field in [petTarget, kidsTarget, jobTarget, partnerTarget]:
                if field:
                    add_combo(field + yearTarget)
                    add_combo(field + dayTarget + monthTarget)
                    add_combo(field + monthTarget + yearTarget)
        if bday in ("Y", "y") and partnerTarget:
            add_combo(partnerTarget + yearTarget[-2:])
            add_combo(partnerTarget + month_word)

        if partnerTarget:
            for base in [partnerTarget, partnerTarget.capitalize(), nameTarget + partnerTarget, partnerTarget + nameTarget, nameTarget.capitalize() + partnerTarget.capitalize(), partnerTarget.capitalize() + nameTarget.capitalize(), leet(partnerTarget), altcaps(partnerTarget)]:
                add_combo(base)
                for suffix in common_suffixes:
                    add_combo(base + suffix)
            for i in range(range1):
                add_combo(partnerTarget + str(i))
                add_combo(nameTarget + partnerTarget + str(i))
                add_combo(partnerTarget + nameTarget + str(i))
            for sep in separators:
                add_combo(f"{nameTarget}{sep}{partnerTarget}")
                add_combo(f"{partnerTarget}{sep}{nameTarget}")
            if bday in ("Y", "y"):
                add_combo(partnerTarget + yearTarget)
                add_combo(nameTarget + partnerTarget + yearTarget)

        if keywordTarget:
            for base in [keywordTarget, keywordTarget.capitalize(), keywordTarget.upper(), nameTarget + keywordTarget, keywordTarget + nameTarget, leet(keywordTarget), altcaps(keywordTarget)]:
                add_combo(base)
                for suffix in common_suffixes:
                    add_combo(base + suffix)
            for i in range(range1):
                add_combo(keywordTarget + str(i))
                add_combo(nameTarget + keywordTarget + str(i))
            for sep in separators:
                add_combo(f"{nameTarget}{sep}{keywordTarget}")
                add_combo(f"{keywordTarget}{sep}{nameTarget}")

        if cityTarget:
            for base in [cityTarget, cityTarget.capitalize(), nameTarget + cityTarget, cityTarget + nameTarget, nameTarget.capitalize() + cityTarget.capitalize(), leet(cityTarget)]:
                add_combo(base)
                for suffix in common_suffixes:
                    add_combo(base + suffix)
            for sep in separators:
                add_combo(f"{nameTarget}{sep}{cityTarget}")

        if luckyTarget:
            for base in [nameTarget, lastnameTarget, nameTarget.capitalize(), lastnameTarget.capitalize()]:
                add_combo(base + luckyTarget)
                add_combo(luckyTarget + base)
            if petTarget:
                add_combo(petTarget + luckyTarget)
            if partnerTarget:
                add_combo(partnerTarget + luckyTarget)

        if phoneTarget:
            add_combo(phoneTarget)
            add_combo(nameTarget + phoneTarget)
            add_combo(nameTarget + phoneTarget[-4:])
            add_combo(nameTarget + phoneTarget[-6:])
            add_combo(lastnameTarget + phoneTarget[-4:])
            add_combo(phoneTarget[-4:] + nameTarget)
            add_combo(phoneTarget[:4] + nameTarget)
            for sep in separators:
                add_combo(f"{nameTarget}{sep}{phoneTarget[-4:]}")
                add_combo(f"{lastnameTarget}{sep}{phoneTarget[-4:]}")
                add_combo(f"{phoneTarget[-4:]}{sep}{nameTarget}")

        for field in all_fields:
            if field and len(field) > 1:
                add_combo(only_consonants(field))
                add_combo(only_vowels(field))
                add_combo(no_vowels(field))
                add_combo(leet(field))
                add_combo(altcaps(field))
                add_combo(field + no_vowels(field))
                add_combo(no_vowels(field) + field)
                add_combo(leet(field)[::-1])
                add_combo(altcaps(field)[::-1])

        for l_field in [nameTarget, lastnameTarget, keywordTarget]:
            if l_field:
                for r_field in [petTarget, partnerTarget, kidsTarget]:
                    if r_field:
                        for sep in separators[:8]:
                            for num in separator_numbers[:8]:
                                add_combo(f"{l_field}{sep}{r_field}{sep}{num}")
                                add_combo(f"{num}{sep}{l_field}{sep}{r_field}")
                                add_combo(f"{leet(l_field)}{sep}{r_field}{sep}{num}")
                                add_combo(f"{l_field}{sep}{leet(r_field)}{sep}{num}")

        for field in all_fields:
            if field:
                for i in range(10):
                    add_combo(field + str(i) * 2)
                    add_combo(field + str(i) * 3)
                    add_combo(str(i) * 2 + field)
                    add_combo(str(i) * 3 + field)
                    add_combo(field[0] + str(i) * (len(field)-1) + field[-1:] if len(field) > 1 else field)

        for combo_base in [nameTarget + lastnameTarget, lastnameTarget + nameTarget]:
            add_combo(leet(combo_base))
            add_combo(altcaps(combo_base))
            add_combo(no_vowels(combo_base))
            add_combo(only_consonants(combo_base))
            for sep in separators:
                add_combo(leet(nameTarget) + sep + leet(lastnameTarget))
                add_combo(altcaps(nameTarget) + sep + altcaps(lastnameTarget))

        for sp in special_chars:
            for num in separator_numbers:
                for field in [nameTarget, lastnameTarget, keywordTarget]:
                    if field:
                        add_combo(field + sp + field[::-1] + sp + num)
                        add_combo(num + sp + field + sp + field.upper())
                        add_combo(leet(field) + sp + num + sp + altcaps(field))
                        add_combo(altcaps(field) + sp + leet(field) + sp + num)

        for i in range(1, min(range1, 100)):
            add_combo(nameTarget + str(i).zfill(2))
            add_combo(nameTarget + str(i).zfill(3))
            add_combo(nameTarget + str(i).zfill(4))
            add_combo(lastnameTarget + str(i).zfill(2))
            add_combo(lastnameTarget + str(i).zfill(3))

        if bday in ("Y", "y"):
            month_word = months_en[int(monthTarget) - 1]
            for a, b in [(nameTarget, dayTarget), (dayTarget, nameTarget), (nameTarget, monthTarget), (monthTarget, nameTarget)]:
                if a and b:
                    for sep in separators[:8]:
                        for suffix in common_suffixes[:8]:
                            add_combo(f"{a}{sep}{b}{suffix}")
                            add_combo(f"{suffix}{a}{sep}{b}")
                            add_combo(f"{leet(a)}{sep}{b}{suffix}")

        for a, b, c in [(nameTarget, lastnameTarget, keywordTarget),
                        (nameTarget, keywordTarget, lastnameTarget),
                        (keywordTarget, nameTarget, lastnameTarget),
                        (nameTarget, petTarget, lastnameTarget),
                        (lastnameTarget, partnerTarget, nameTarget)]:
            if a and b and c:
                for sep in separators[:5]:
                    add_combo(f"{leet(a)}{sep}{altcaps(b)}{sep}{no_vowels(c)}")
                    add_combo(f"{altcaps(a)}{sep}{leet(b)}{sep}{altcaps(c)}")
                    add_combo(f"{no_vowels(a)}{sep}{b}{sep}{leet(c)}")
                    add_combo(f"{a}{sep}{b}{sep}{c}")
                    add_combo(f"{c}{sep}{b}{sep}{a}")

        for field in all_fields:
            if field and len(field) >= 3:
                half = len(field) // 2
                add_combo(field[:half] + leet(field[half:]))
                add_combo(altcaps(field[:half]) + field[half:])
                add_combo(field[:half] + field[half:].upper())
                add_combo(leet(field[:half]) + no_vowels(field[half:]))
                for num in separator_numbers[:5]:
                    add_combo(field[:half] + num + field[half:])
                    add_combo(num + field[:half:] + field[half:])

        for item in all_fields:
            if item:
                for sp in special_chars:
                    add_combo(item + sp)
                    add_combo(sp + item)
                    add_combo(item[0] + sp + item)
                    add_combo(item + sp + item[0])
                    for num in separator_numbers[-3:]:
                        add_combo(f"{item}{sp}{num}")
                        add_combo(f"{num}{sp}{item}")

        for field in all_fields:
            if field:
                add_combo(field.upper())
                add_combo(field.lower())
                add_combo(field.capitalize() * 2)
                add_combo(field[0].upper() + field[1:].lower())
                add_combo(field[0].lower() + field[1:].upper())
                if len(field) > 2:
                    add_combo(field[0] + field[-1] + field[1:-1])
                    add_combo(field[-1] + field[:-1])
                    add_combo(field[1:] + field[0])
                    for idx in range(len(field)):
                        if idx > 0 and idx < len(field) - 1:
                            add_combo(field[:idx] + field[idx:].upper())
                            add_combo(field[:idx].upper() + field[idx:])

        for kb_pattern in keyboard_patterns:
            for field in [nameTarget, lastnameTarget, keywordTarget, petTarget]:
                if field:
                    add_combo(field + kb_pattern)
                    add_combo(kb_pattern + field)
                    add_combo(leet(field) + kb_pattern)
                    add_combo(kb_pattern + leet(field))
                    add_combo(field + kb_pattern + field)
                    for sep in separators[:4]:
                        add_combo(f"{field}{sep}{kb_pattern}")
                        add_combo(f"{kb_pattern}{sep}{field}")

        for a, b, c, d in [(nameTarget, lastnameTarget, keywordTarget, petTarget),
                           (nameTarget, keywordTarget, partnerTarget, lastnameTarget),
                           (lastnameTarget, nameTarget, kidsTarget, jobTarget)]:
            if a and b and c and d:
                for sep1, sep2, sep3 in [(separators[i], separators[j], separators[k]) for i in range(min(3, len(separators))) for j in range(min(3, len(separators))) for k in range(min(3, len(separators)))]:
                    add_combo(f"{leet(a)}{sep1}{altcaps(b)}{sep2}{no_vowels(c)}{sep3}{d}")
                    add_combo(f"{a}{sep1}{b}{sep2}{c}{sep3}{d}")
                    add_combo(f"{d}{sep3}{c}{sep2}{b}{sep1}{a}")

        for field in all_fields:
            if field:
                for num in separator_numbers:
                    add_combo(field + num)
                    add_combo(num + field)
                    add_combo(field + num + field)
                    add_combo(num + field + num)
                    add_combo(leet(field) + num)
                    add_combo(num + leet(field))
                    for ch in special_chars:
                        add_combo(f"{field}{ch}{num}")
                        add_combo(f"{num}{ch}{field}")
                        add_combo(f"{field}{ch}{num}{ch}{field}")

        for field1 in all_fields:
            for field2 in all_fields:
                if field1 and field2 and field1 != field2:
                    add_combo(field1.upper() + field2.lower())
                    add_combo(field1.lower() + field2.upper())
                    add_combo(leet(field1) + field2)
                    add_combo(field1 + leet(field2))
                    add_combo(field1 + field2 + field1)
                    add_combo(field2 + field1 + field2)
                    add_combo(field1[::-1] + field2)
                    add_combo(field1 + field2[::-1])
                    add_combo(field1[::-1] + field2[::-1])
                    for num in ["2024", "2023", "2025", "2026"]:
                        add_combo(field1 + num + field2)
                        add_combo(field2 + num + field1)

        for field in all_fields:
            if field and len(field) > 2:
                for i in range(len(field)):
                    for j in range(i+1, len(field)+1):
                        add_combo(field[i:j])
                        add_combo(field[i:j] + nameTarget)
                        add_combo(nameTarget + field[i:j])
                        if len(field[i:j]) > 1:
                            add_combo(leet(field[i:j]))
                            add_combo(altcaps(field[i:j]))

        for bracket_pair in [("(", ")"), ("{", "}"), ("[", "]"), ("<", ">"), ("'", "'"), ('"', '"')]:
            for field in [nameTarget, lastnameTarget, keywordTarget]:
                if field:
                    add_combo(f"{bracket_pair[0]}{field}{bracket_pair[1]}")
                    add_combo(f"{bracket_pair[0]}{field.upper()}{bracket_pair[1]}")
                    add_combo(f"{bracket_pair[0]}{leet(field)}{bracket_pair[1]}")
                    for num in separator_numbers[:5]:
                        add_combo(f"{bracket_pair[0]}{field}{num}{bracket_pair[1]}")

        for mul in range(2, 4):
            for field in all_fields:
                if field:
                    add_combo(field * mul)
                    add_combo((field[0] * mul) + field[1:] if len(field) > 1 else field)
                    add_combo(field + (field[-1] * (mul-1)))
                    for num in separator_numbers[:3]:
                        add_combo((field + num) * mul)

        if bday in ("Y", "y"):
            month_word = months_en[int(monthTarget) - 1]
            for perm in permutations([dayTarget, monthTarget, yearTarget[:2], nameTarget, lastnameTarget], 2):
                if perm[0] and perm[1]:
                    for sep in separators[:6]:
                        add_combo(f"{perm[0]}{sep}{perm[1]}")
                        add_combo(f"{leet(perm[0]) if perm[0] != monthTarget else perm[0]}{sep}{perm[1]}")

        if field:
                for y in range(1960, 2026):
                    add_combo(field + str(y))
                    add_combo(str(y) + field)
                    for month in range(1, 13):
                        add_combo(field + str(month).zfill(2) + str(y % 100))
                        add_combo(str(month).zfill(2) + field + str(y % 100))

        for field in all_fields:
            if field:
                for i in range(1000):
                    if i % 100 == 0:
                        add_combo(field + str(i))
                        add_combo(str(i) + field)
                        add_combo(field + str(i).zfill(4))
                        add_combo(str(i).zfill(4) + field)

        for sp in special_chars:
            for field1 in all_fields:
                for field2 in all_fields:
                    if field1 and field2:
                        add_combo(f"{leet(field1)}{sp}{altcaps(field2)}")
                        add_combo(f"{altcaps(field1)}{sp}{no_vowels(field2)}")
                        add_combo(f"{no_vowels(field1)}{sp}{leet(field2)}")
                        add_combo(f"{field1[::-1]}{sp}{field2[::-1]}")
                        add_combo(f"{field1.upper()}{sp}{field2.lower()}")

        for kb in extended_keyboard:
            for field in all_fields:
                if field:
                    add_combo(leet(kb) + field)
                    add_combo(field + leet(kb))
                    add_combo(altcaps(kb) + field)
                    add_combo(field + altcaps(kb))
                    add_combo(field + kb + field)
                    add_combo(kb + leet(field) + kb)

        for field in all_fields:
            if field and len(field) > 2:
                for i in range(len(field)):
                    for j in range(i+2, len(field)+1):
                        sub = field[i:j]
                        if len(sub) > 1:
                            add_combo(leet(sub) + nameTarget)
                            add_combo(sub + leet(nameTarget))
                            add_combo(altcaps(sub) + lastnameTarget)
                            add_combo(no_vowels(sub) + keywordTarget if keywordTarget else nameTarget)
                            for num in separator_numbers:
                                add_combo(sub + num)

        all_field_pairs = [(a, b) for a in all_fields for b in all_fields if a and b]
        for (f1, f2) in all_field_pairs[:50]:
            for sep in separators:
                add_combo(f"{leet(f1)}{sep}{leet(f2)}")
                add_combo(f"{altcaps(f1)}{sep}{altcaps(f2)}")
                add_combo(f"{f1.upper()}{sep}{f2.lower()}")
                add_combo(f"{no_vowels(f1)}{sep}{no_vowels(f2)}")
                for num in separator_numbers[:5]:
                    add_combo(f"{f1}{sep}{f2}{sep}{num}")
                    add_combo(f"{leet(f1)}{sep}{f2}{sep}{leet(num)}")

        for field in all_fields:
            if field:
                for sp1 in special_chars:
                    for sp2 in special_chars:
                        add_combo(f"{sp1}{field}{sp2}")
                        add_combo(f"{sp1}{leet(field)}{sp2}")
                        add_combo(f"{sp1}{altcaps(field)}{sp2}")
                        add_combo(f"{sp1}{no_vowels(field)}{sp2}")
                        add_combo(f"{sp1}{field}{sp1}{field}{sp2}")

        for i in range(2, 6):
            for field in all_fields:
                if field:
                    repeated = field * i
                    add_combo(repeated)
                    add_combo(leet(field) * i)
                    add_combo(altcaps(field) * i)
                    add_combo((field[0] * 2) + field[1:] if len(field) > 1 else field)
                    add_combo(field + (field[-1] * (i-1)))
                    add_combo((field[0] * i) + field if len(field) > 1 else field)

        for triples in [(nameTarget, lastnameTarget, keywordTarget),
                        (keywordTarget, nameTarget, petTarget),
                        (partnerTarget, lastnameTarget, nameTarget),
                        (nameTarget, petTarget, kidsTarget),
                        (lastnameTarget, keywordTarget, jobTarget)]:
            if all(triples):
                for i in range(len(separators)):
                    for j in range(len(separators)):
                        sep1 = separators[i]
                        sep2 = separators[j]
                        add_combo(f"{leet(triples[0])}{sep1}{altcaps(triples[1])}{sep2}{no_vowels(triples[2])}")
                        add_combo(f"{triples[0]}{sep1}{triples[1]}{sep2}{triples[2]}")
                        add_combo(f"{triples[2]}{sep2}{triples[1]}{sep1}{triples[0]}")
                        add_combo(f"{altcaps(triples[0])}{sep1}{no_vowels(triples[1])}{sep2}{leet(triples[2])}")

        for field in all_fields:
            if field:
                for y_val in ["2024", "2023", "2022", "2021", "2020", "2019"]:
                    for m_val in ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]:
                        for d_val in ["01", "15", "30"]:
                            add_combo(field + d_val + m_val + y_val)
                            add_combo(d_val + m_val + y_val + field)
                            add_combo(y_val + m_val + d_val + field)
                            add_combo(field + y_val[-2:] + m_val + d_val)

        with open("passwords.txt", "w") as f:
            for combo in sorted(combos):
                f.write(combo + "\n")





        
        print("removing duplicates...")
        with open("passwords.txt", "r") as f:
            lines = f.readlines()
        lines = [l.strip() for l in lines if l.strip()]
        unique_lines = list(dict.fromkeys(lines))
        with open("passwords.txt", "w") as f:
            f.write('\n'.join(unique_lines) + '\n')
        print(f"[+] Total unique passwords: {len(unique_lines)}")
    elif option == "2":
        print("name@example.com")
        domain = input("give domain (e.g. gmail.com):")
        keywords = input("give keyword")
        letters2 = string.ascii_lowercase
        digits = string.digits
        letters3 = string.ascii_uppercase
        with open("emails.txt", "w") as f:
            for _ in range(1000):
                local_part = ''.join(random.choices(letters2 + digits + letters3, k=10))
                if keywords:
                    local_part = keywords + local_part
                f.write(f"{local_part}@{domain}\n")
    elif option == "3":
        countryCode = input("give country code e.g. +90): ")
        if countryCode == "+30":
            phonenumbers = int(input("give number of phone numbers to generate: "))
            with open("phonenumbers.txt", "w") as f:
              #generate random numbers from 6970000000 to 6999999999 (GR)
                for i in range(phonenumbers):
                    number = random.randint(6970000000, 6999999999)
                    f.write(f"{countryCode}{number}\n")
        elif countryCode == "+90":
            phonenumbers = int(input("give number of phone numbers to generate: "))
            with open("phonenumbers.txt", "w") as f:
              #GENERATE random numbers tr
                for i in range(phonenumbers):
                    number = random.randint(5300000000, 5539999999)
                    f.write(f"{countryCode}{number}\n")
        else: 
            print("unsupported country code")
    elif option == "4":
        def is_valid_email(email):
            pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            return re.match(pattern, email) is not None
        
        def is_valid_phone(phone):
            try:
                parsed = phonenumbers.parse(phone, None)
                return phonenumbers.is_valid_number(parsed)
            except:
                return False
        
        def check_email_hibp(email):
            try:
                response = requests.get(
                    f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}",
                    headers={"User-Agent": "WordbuildPython/1.0"},
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
        
        val_option = input("1. Validate email\n2. Validate phone\n3. Check email (HIBP)\n4. Batch validate emails (HIBP)\nChoose: ").strip()
        
        if val_option == "1":
            email = input("Enter email to validate: ").strip()
            if is_valid_email(email):
                print(f"[+] {email} is a VALID email format")
            else:
                print(f"[-] {email} is NOT a valid email format")
        
        elif val_option == "2":
            phone = input("Enter phone number to validate (with country code): ").strip()
            if is_valid_phone(phone):
                print(f"[+] {phone} is a VALID phone number")
            else:
                print(f"[-] {phone} is NOT a valid phone number")
        
        elif val_option == "3":
            email = input("Enter email to check (HIBP): ").strip()
            if is_valid_email(email):
                print(f"[*] Checking {email}...")
                check_email_hibp(email)
            else:
                print(f"[-] Invalid email format: {email}")
        
        elif val_option == "4":
            file_path = input("Enter file path with emails (one per line): ").strip()
            if os.path.exists(file_path):
                with open(file_path, 'r') as f:
                    emails = [line.strip() for line in f if line.strip()]
                
                print(f"[*] Checking {len(emails)} emails...")
                pwned_count = 0
                clean_count = 0
                
                for email in emails:
                    if is_valid_email(email):
                        result = check_email_hibp(email)
                        if result:
                            pwned_count += 1
                        elif result is False:
                            clean_count += 1
                        time.sleep(2)
                    else:
                        print(f"[-] Invalid format: {email}")
                
                print(f"\n[*] Summary: {pwned_count} pwned, {clean_count} clean, {len(emails) - pwned_count - clean_count} errors")
            else:
                print(f"[-] File not found: {file_path}")
        else:
            print("[-] Invalid option")

