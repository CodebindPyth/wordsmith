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

        separators   = [".", "_", "-", "!", "@", "#", "$"]
        common_suffixes = ["123","1234","12345","!","!!","123!","1!","@1","321",
                           "111","000","007","69","99","2024","2023","01","1"]
        keyboard_patterns = ["qwerty","123456","password","qwerty123","abc123","letmein","welcome"]
        months_en = ["january","february","march","april","may","june",
                     "july","august","september","october","november","december"]

        initial      = nameTarget[0]
        last_initial = lastnameTarget[0]

        # collect all non-empty extra fields for permutation combos
        extra_fields = [f for f in [petTarget, kidsTarget, partnerTarget,
                                     keywordTarget, jobTarget, cityTarget] if f]

        with open("passwords.txt", "w") as f:

            
            for w in [nameTarget, lastnameTarget,
                      nameTarget+lastnameTarget, lastnameTarget+nameTarget,
                      nameTarget.capitalize(), lastnameTarget.capitalize(),
                      nameTarget.upper(), lastnameTarget.upper(),
                      nameTarget.lower(), lastnameTarget.lower(),
                      nameTarget.capitalize()+lastnameTarget.capitalize(),
                      lastnameTarget.capitalize()+nameTarget.capitalize()]:
                f.write(w + "\n")

            
            for sep in separators:
                f.write(f"{nameTarget}{sep}{lastnameTarget}\n")
                f.write(f"{lastnameTarget}{sep}{nameTarget}\n")
                f.write(f"{nameTarget.capitalize()}{sep}{lastnameTarget.capitalize()}\n")

            
            for w in [leet(nameTarget), leet(lastnameTarget),
                      leet(nameTarget)+leet(lastnameTarget),
                      altcaps(nameTarget), altcaps(lastnameTarget),
                      altcaps(nameTarget)+altcaps(lastnameTarget),
                      partial_leet(nameTarget), partial_leet(lastnameTarget),
                      partial_leet(nameTarget)+partial_leet(lastnameTarget),
                      no_vowels(nameTarget), no_vowels(lastnameTarget),
                      no_vowels(nameTarget)+no_vowels(lastnameTarget)]:
                f.write(w + "\n")

            
            for suffix in common_suffixes:
                for base in [nameTarget, lastnameTarget,
                             nameTarget.capitalize(), lastnameTarget.capitalize(),
                             nameTarget.upper(), lastnameTarget.upper(),
                             nameTarget+lastnameTarget, lastnameTarget+nameTarget,
                             leet(nameTarget), leet(lastnameTarget),
                             altcaps(nameTarget), no_vowels(nameTarget),
                             no_vowels(lastnameTarget),
                             initial+lastnameTarget, initial+"."+lastnameTarget]:
                    f.write(f"{base}{suffix}\n")

            
            for sp in ["!", "@", "#", "$"]:
                for num in ["1", "12", "123", "1234"]:
                    f.write(f"{nameTarget.capitalize()}{sp}{num}\n")
                    f.write(f"{lastnameTarget.capitalize()}{sp}{num}\n")

            
            for i in range(range1):
                for base in [nameTarget, lastnameTarget,
                             nameTarget+lastnameTarget, lastnameTarget+nameTarget,
                             nameTarget.capitalize(), lastnameTarget.capitalize(),
                             nameTarget.upper(), nameTarget.lower(),
                             leet(nameTarget), altcaps(nameTarget),
                             nameTarget.capitalize()+lastnameTarget.capitalize()]:
                    f.write(f"{base}{i}\n")
                    f.write(f"{i}{base}\n")
                for sep in separators:
                    f.write(f"{nameTarget}{sep}{i}\n")
                    f.write(f"{lastnameTarget}{sep}{i}\n")
                    f.write(f"{nameTarget}{sep}{lastnameTarget}{sep}{i}\n")

            
            for w in [nameTarget[::-1], lastnameTarget[::-1],
                      nameTarget[::-1]+lastnameTarget[::-1]]:
                f.write(w + "\n")
                for suffix in common_suffixes:
                    f.write(f"{w}{suffix}\n")

            
            for w in [initial+lastnameTarget, initial+"."+lastnameTarget,
                      nameTarget+last_initial, initial+lastnameTarget.capitalize(),
                      nameTarget[0].upper()+nameTarget[1:-1]+nameTarget[-1].upper()]:
                f.write(w + "\n")

            
            f.write(f"{nameTarget}{nameTarget}\n")
            f.write(f"{lastnameTarget}{lastnameTarget}\n")
            f.write(f"{nameTarget}{nameTarget}{lastnameTarget}\n")

            
            for pad in ["01", "001", "0001"]:
                f.write(f"{nameTarget}{pad}\n")
                f.write(f"{nameTarget.capitalize()}{pad}\n")
                f.write(f"{lastnameTarget}{pad}\n")

            
            for year in range(1960, 2010):
                f.write(f"{nameTarget}{year}\n")
                f.write(f"{lastnameTarget}{year}\n")
                f.write(f"{nameTarget.capitalize()}{year}\n")

            
            for pattern in keyboard_patterns:
                for base in [nameTarget, lastnameTarget,
                             nameTarget.capitalize(), lastnameTarget.capitalize(),
                             nameTarget.upper(), lastnameTarget.upper()]:
                    f.write(f"{base}{pattern}\n")
                    f.write(f"{pattern}{base}\n")
                f.write(f"{leet(pattern)}\n")
                f.write(f"{nameTarget}{leet(pattern)}\n")

            
            half = len(nameTarget) // 2
            f.write(f"{nameTarget[:half]}{lastnameTarget}\n")
            f.write(f"{nameTarget[:half]}{lastnameTarget[:half]}\n")
            f.write(f"{nameTarget}{lastnameTarget[:half]}\n")

            
            if petTarget:
                for base in [petTarget, petTarget.capitalize(),
                             nameTarget+petTarget, petTarget+nameTarget,
                             nameTarget.capitalize()+petTarget.capitalize(),
                             petTarget.capitalize()+nameTarget.capitalize(),
                             leet(petTarget), altcaps(petTarget)]:
                    f.write(base + "\n")
                    for suffix in common_suffixes:
                        f.write(f"{base}{suffix}\n")
                for i in range(range1):
                    f.write(f"{petTarget}{i}\n")
                    f.write(f"{petTarget.capitalize()}{i}\n")
                    f.write(f"{nameTarget}{petTarget}{i}\n")
                for sep in separators:
                    f.write(f"{nameTarget}{sep}{petTarget}\n")
                    f.write(f"{lastnameTarget}{sep}{petTarget}\n")

            
            if kidsTarget:
                for base in [kidsTarget, kidsTarget.capitalize(),
                             nameTarget+kidsTarget, kidsTarget+nameTarget,
                             nameTarget.capitalize()+kidsTarget.capitalize(),
                             leet(kidsTarget), altcaps(kidsTarget)]:
                    f.write(base + "\n")
                    for suffix in common_suffixes:
                        f.write(f"{base}{suffix}\n")
                for i in range(range1):
                    f.write(f"{kidsTarget}{i}\n")
                    f.write(f"{kidsTarget.capitalize()}{i}\n")
                    f.write(f"{nameTarget}{kidsTarget}{i}\n")

            
            if jobTarget:
                for base in [jobTarget, jobTarget.capitalize(),
                             nameTarget+jobTarget, jobTarget+nameTarget,
                             leet(jobTarget), altcaps(jobTarget)]:
                    f.write(base + "\n")
                    for suffix in common_suffixes:
                        f.write(f"{base}{suffix}\n")
                for i in range(range1):
                    f.write(f"{jobTarget}{i}\n")
                    f.write(f"{jobTarget.capitalize()}{i}\n")
                    f.write(f"{nameTarget}{jobTarget}{i}\n")

            
            if petTarget and kidsTarget:
                f.write(f"{petTarget}{kidsTarget}\n")
                f.write(f"{kidsTarget}{petTarget}\n")

            
            if bday in ("Y", "y"):
                month_word = months_en[int(monthTarget) - 1]
                bday_combos = [
                    nameTarget+dayTarget+monthTarget+yearTarget,
                    nameTarget+yearTarget,
                    nameTarget+dayTarget+monthTarget,
                    nameTarget+monthTarget+yearTarget,
                    lastnameTarget+yearTarget,
                    lastnameTarget+dayTarget+monthTarget,
                    nameTarget.capitalize()+yearTarget,
                    nameTarget.capitalize()+dayTarget+monthTarget+yearTarget,
                    yearTarget+nameTarget,
                    dayTarget+monthTarget+nameTarget,
                    dayTarget+monthTarget+yearTarget,
                    yearTarget[-2:]+nameTarget,
                    nameTarget+yearTarget[-2:],
                    nameTarget+month_word,
                    nameTarget+month_word.capitalize(),
                    nameTarget+month_word+yearTarget,
                    nameTarget.capitalize()+month_word.capitalize()+yearTarget,
                    nameTarget+month_word+yearTarget[-2:],
                ]
                for combo in bday_combos:
                    f.write(combo + "\n")
                for sep in separators:
                    f.write(f"{nameTarget}{sep}{dayTarget}{monthTarget}{yearTarget}\n")
                    f.write(f"{nameTarget}{sep}{yearTarget}\n")
                for field in [petTarget, kidsTarget, jobTarget, partnerTarget]:
                    if field:
                        f.write(f"{field}{yearTarget}\n")
                        f.write(f"{field}{dayTarget}{monthTarget}\n")
                        f.write(f"{field}{monthTarget}{yearTarget}\n")

            
            if partnerTarget:
                for base in [partnerTarget, partnerTarget.capitalize(),
                             nameTarget+partnerTarget, partnerTarget+nameTarget,
                             nameTarget.capitalize()+partnerTarget.capitalize(),
                             partnerTarget.capitalize()+nameTarget.capitalize(),
                             leet(partnerTarget), altcaps(partnerTarget)]:
                    f.write(base + "\n")
                    for suffix in common_suffixes:
                        f.write(f"{base}{suffix}\n")
                for i in range(range1):
                    f.write(f"{partnerTarget}{i}\n")
                    f.write(f"{nameTarget}{partnerTarget}{i}\n")
                    f.write(f"{partnerTarget}{nameTarget}{i}\n")
                for sep in separators:
                    f.write(f"{nameTarget}{sep}{partnerTarget}\n")
                    f.write(f"{partnerTarget}{sep}{nameTarget}\n")
                if bday in ("Y", "y"):
                    f.write(f"{partnerTarget}{yearTarget}\n")
                    f.write(f"{nameTarget}{partnerTarget}{yearTarget}\n")

            
            if keywordTarget:
                for base in [keywordTarget, keywordTarget.capitalize(),
                             keywordTarget.upper(),
                             nameTarget+keywordTarget, keywordTarget+nameTarget,
                             leet(keywordTarget), altcaps(keywordTarget)]:
                    f.write(base + "\n")
                    for suffix in common_suffixes:
                        f.write(f"{base}{suffix}\n")
                for i in range(range1):
                    f.write(f"{keywordTarget}{i}\n")
                    f.write(f"{nameTarget}{keywordTarget}{i}\n")
                for sep in separators:
                    f.write(f"{nameTarget}{sep}{keywordTarget}\n")
                    f.write(f"{keywordTarget}{sep}{nameTarget}\n")

            
            if cityTarget:
                for base in [cityTarget, cityTarget.capitalize(),
                             nameTarget+cityTarget, cityTarget+nameTarget,
                             nameTarget.capitalize()+cityTarget.capitalize(),
                             leet(cityTarget)]:
                    f.write(base + "\n")
                    for suffix in common_suffixes:
                        f.write(f"{base}{suffix}\n")
                for sep in separators:
                    f.write(f"{nameTarget}{sep}{cityTarget}\n")

            
            if luckyTarget:
                for base in [nameTarget, lastnameTarget,
                             nameTarget.capitalize(), lastnameTarget.capitalize()]:
                    f.write(f"{base}{luckyTarget}\n")
                    f.write(f"{luckyTarget}{base}\n")
                if petTarget:
                    f.write(f"{petTarget}{luckyTarget}\n")
                if partnerTarget:
                    f.write(f"{partnerTarget}{luckyTarget}\n")

            
            if phoneTarget:
                f.write(f"{phoneTarget}\n")
                f.write(f"{nameTarget}{phoneTarget}\n")
                f.write(f"{nameTarget}{phoneTarget[-4:]}\n")
                f.write(f"{nameTarget}{phoneTarget[-6:]}\n")
                f.write(f"{lastnameTarget}{phoneTarget[-4:]}\n")
                f.write(f"{phoneTarget[-4:]}{nameTarget}\n")
                f.write(f"{phoneTarget[:4]}{nameTarget}\n")

            
            all_fields = [nameTarget, lastnameTarget] + extra_fields
            for a, b in permutations(all_fields, 2):
                f.write(f"{a.capitalize()}{b.capitalize()}\n")
                f.write(f"{a}{b}123\n")
                f.write(f"{a}{b}!\n")

        
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
                for i in range(phonenumbers):
                    number = random.randint(6970000000, 6999999999)
                    f.write(f"{countryCode}{number}\n")
        elif countryCode == "+90":
            phonenumbers = int(input("give number of phone numbers to generate: "))
            with open("phonenumbers.txt", "w") as f:
                for i in range(phonenumbers):
                    number = random.randint(5300000000, 5539999999)
                    f.write(f"{countryCode}{number}\n")
        else: 
            print("unsupported country code")
