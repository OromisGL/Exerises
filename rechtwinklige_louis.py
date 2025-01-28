
# Rechtwinklige Dreiecke

# Gesucht ist die Menge aller rechtwinkligen Dreiecke mit ganzzahligen Seitenlängen jeweils unter 20.
# Jedes Dreieck soll durch ein Tupel mit den drei Seitenlängen dargestellt werden.
# Beispiel: (3, 4, 5)

# Beachte:
# In rechtwinkligen Dreiecken gilt der Satz des Pythagoras:
# a² + b² = c²

from math import sqrt

a = [i for i in range(1,21)]
b = [i for i in range(1,21)]
c = [i for i in range(1,21)]

count = 0
for i in a:
    for j in b:
        for h in c:
            while sqrt(i**2 + j **2 == h**2):
                count += 1
                print(i, j, h)
                break


print(f"Es gibt {count} Dreicke mit ganzzahliger Seitenlänge bis 20.")
