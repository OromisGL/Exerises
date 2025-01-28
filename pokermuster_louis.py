# Poker-Muster

# Das Würfelspiel Yahtzee verwendet ähnliche Muster wie das Kartenspiel Poker,
# verzichtet aber auf die verschiedenen Farben.
# Bei Yahtzee werden fünf Spielwürfel (Augenzahlen 1 bis 6) geworfen.
# Verwende dazu Zufallszahlen.

# Schreibe ein Programm, das die fünf Zahlen in einer Liste speichert
# und mittels einer Funktion in der Standardausgabe anzeigt.
#
# Entscheide dann, ob alle Zahlen gleich sind (5-Poker).

# Zusatz:
# Entscheide, ob es sich um ein anderes Poker-Muster handelt:
# Vierling
# Strasse
# Full House
# Drilling
# Zwei Paare
# Paar
from random import randint
from collections import Counter

result = []

def dice():
    return randint(1, 6)

for i in range(5):
    result.append(dice())

ordered = sorted(result)

def is_straight(ordered):
    return ordered == list(range(ordered[0], ordered[0] + 5))

for i in ordered:
    counts = Counter(ordered)
    if is_straight(ordered):
        print("Straße")
        break
    if sorted(counts.values()) == [2,3]:
        print("Full House")
        break  
    if sorted(counts.values()) == [2, 2, 1] or sorted(counts.values()) == [1, 2, 2]:
        print("Zwei Paare")
        break  
    if ordered.count(i) == 5:
        print("Poker")
        break
    elif ordered.count(i) == 4:
        print("Vierling")
        break
    elif ordered.count(i) == 3:
        print("Drilling")
        break
    elif ordered.count(i) == 2: 
        print("Paar")
        break

print(result)


