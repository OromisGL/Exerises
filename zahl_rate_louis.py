
# Zahl raten

"""
Schreibe ein Programm, das sich eine Zahl ausdenkt
und den Benutzer diese Zahl raten lässt.
Nach jedem Versuch gibt die Funktion aus,
ob zu hoch, zu niedrig oder richtig geraten wurde.
"""
from random import randint

def zufall():
    return randint(1, 100)

def differ(a, b):
    if a > b:
    
        return f"zu niedrig, hier die differenz {a - b}"
    else:
        return f"zu hoch, hier die differenz {b - a}"

user = int(input("Rate die Zahl: "))
zahl = zufall()
diff = differ(zahl, user)

while user != zahl:
    zufall()
    print(f"Die Zahl war {diff}")
    user = int(input("Rate die Zahl: "))
    diff = differ(zahl, user)

if user == zahl:

    print(f"Die Zahl war {zahl}")
