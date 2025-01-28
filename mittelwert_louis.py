# Mittelwert

"""
Schreibe eine Funktion, die drei Zahlen entgegennimmt,
den Mittelwert (Durchschnitt) berechnet und diesen zurückgibt.
"""

def average(a, b, c):
    return (a + b + c) / 3


a = int(input("Erste Zahl: "))
b = int(input("Zweite Zahl: "))
c = int(input("Dritte Zahl: "))

print(f"Der durchschnitt ist: {average(a, b, c)}")
