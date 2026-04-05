
import os, sys, time   
import string
import itertools
import random
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
while (option != "4"):
    print("                                                                                  1.generate a random password")
    print("                                                                                    2.generate a random email")
    print("                                                                                 3.generate a random phone number")
    print("                                                                                               4.exit")
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
#custom seperators
        separators   = [".", "_", "-", "!", "@", "#", "$"]
        common_suffixes = ["123","1234","12345","!","!!","123!","1!","@1","321",
                           "111","000","007","69","99","2024","2023","01","1"]
        keyboard_patterns = ["qwerty","123456","password","qwerty123","abc123","letmein","welcome"]
        months_en = ["january","february","march","april","may","june",
                     "july","august","september","october","november","december"]
        separator_numbers = ["1","12","123","1234","2024","2023","007","69","99","321","01"]

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
