
# Zwei Zahlen genau vergleichen

# Schreibe ein Programm, das testet und ausgibt,
# welche von zwei Zahlen größer ist oder ob beide Zahlen gleich groß sind.
# Die beiden Zahlen sollen zufällig erzeugt werden.
from random import randint

zahl1 = randint(1, 100)
zahl2 = randint(1, 100)

if zahl1 == zahl2:
    print(f"{zahl1} und {zahl2} sind gleich.")
elif zahl1 > zahl2:
    print(f"{zahl1} ist größer als {zahl2}.")
else:
    print(f"{zahl2} ist größer als {zahl1}.")
