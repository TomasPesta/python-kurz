"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Tomáš Pešta
email: Thomaspe@seznam.cz
"""
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

uzivatel_db = {"bob": "123",
              "ann": "pass123",
              "mike": "password123",
              "liz": "pass123"}

def analyze_text(text):
    slova = text.split()
    pocet_slov = len(slova)
    pocet_titlecase = 0
    pocet_uppercase = 0
    pocet_lowercase = 0
    pocet_cisel = 0
    suma_cisel = 0
    delky_slov = {}

    for slovo in slova:
        if slovo.istitle():
            pocet_titlecase += 1
        if slovo.isupper():
            pocet_uppercase += 1
        if slovo.islower():
            pocet_lowercase += 1
        if slovo.isdigit():
            pocet_cisel += 1
            suma_cisel += int(slovo)
        else:
            for char in slovo:
                if char.isdigit():
                    try:
                        suma_cisel += int(slovo)
                        pocet_cisel += 1
                        break
                    except ValueError:
                        pass

        ciste_slovo = ''.join(c for c in slovo if c.isalpha()) # Odstraníme interpunkci pro délku
        delka = len(ciste_slovo)
        delky_slov[delka] = delky_slov.get(delka, 0) + 1

    print(f"There are {pocet_slov} words in the selected text.")
    print(f"There are {pocet_titlecase} titlecase words.")
    print(f"There are {pocet_uppercase} uppercase words.")
    print(f"There are {pocet_lowercase} lowercase words.")
    print(f"There are {pocet_cisel} numeric strings.")
    print(f"The sum of all the numbers {suma_cisel}")
    print("-" * 40)
    print("LEN|  OCCURENCES   |NR.")
    print("-" * 40)
    for delka in sorted(delky_slov.keys()):
        pocet = delky_slov[delka]
        hvezdicky = "*" * pocet
        print(f"{delka:3}|{hvezdicky:<15}|{pocet}")
    print("-" * 40)

if __name__ == "__main__":
    print("----------------------------------------")
    username = input("Zadejte svoje jméno: ")
    password = input("Zadejte heslo: ")

    if username in uzivatel_db and uzivatel_db[username] == password:
        print(f"Vítej v appce, {username}")
        print("Mame 3 texty k analýze.")
        print("----------------------------------------")

        while True:
            try:
                vyber = int(input("Enter a number btw. 1 and 3 to select: "))
                if 1 <= vyber <= 3:
                    print("-" * 40)
                    analyze_text(TEXTS[vyber - 1])
                    print("-" * 40)
                    break
                else:
                    print("Invalid input. Please enter a number between 1 and 3.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    else:
        print("Neplatné jméno nebo heslo")
        print("Ukončuji program")