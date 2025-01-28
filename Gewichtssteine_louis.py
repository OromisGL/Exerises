
# Gewichtssteine

# Ein Kaufmann besitzt eine Waage mit zwei Waagschalen und sieben Gewichtssteine:
# 1 kg, 2 kg, 4 kg, 8 kg, 16 kg, 32 kg und 64 kg.
# Auf die eine Schale legt der Kaufmann jeweils die Ware,
# während er auf die andere Schale die Gewichtssteine hinstellt.
# Er ist mit seinen sieben Gewichtssteinen in der Lage,
# alle Gewichte von einem Kilo bis zu 127 kg abzuwägen.

# Schreiben Sie ein Programm, das ein Gewicht (0 kg ... 127 kg) entgegennimmt und ausgibt,
# welche Gewichtssteine zu verwenden sind.#

steine = [1, 2, 4, 8, 16, 32, 64]

weight = int(input("Gewicht: "))

if weight <= 127:
    True
else:
    print(f"Overload")


def gewichte(n):
    legen = []
    rest = n
    for i in steine[::-1]:
        if rest >= i:
            legen.append(i)
            rest -= i
        if rest == 0:
            break
              
    return legen
i = gewichte(weight)

print(i)

# Zusatz:
# Der Kaufmann hat seine sieben Gewichtssteine durch die folgenden sechs Gewichte eingetauscht:
# 1 kg, 3 kg, 9 kg, 27 kg, 81 kg und 243 kg.
# Er hat vor, Gewichtssteine auf beide Seiten der Waage zu stellen,
# und hat herausgefunden, dass er nun sogar alle Gewichte von einem Kilo bis zu 364 kg abwiegen kann.
# Die Ware legt er jeweils auf die linke Seite.
# Dein Programm soll nun für jedes Gewicht (0 kg ... 364 kg) angeben,
# welche Steine rechts und welche links aufzustellen sind.
# Beispiel:
# Die Ware wiegt 300 kg.
# Er muss rechts die Steine 243 kg, 81 kg und 3 kg hinstellen,
# während er links das Gewicht mit dem 27-kg-Stein auf 327 kg erhöht.
""" steine2 = [1, 3, 9, 27, 81, 243]
weight = int(input("Gewicht: "))

if weight <= 364:
    True
else:
    print(f"Overload")


def gewichte(n):
    legen = []
    rest = n
    zusatz = 0
    for i in steine2[::-1]:
        if n % 3 == 0:
            if rest >= i:
                legen.append(i)
                rest -= i
            if rest == 0:
                break
        else:
            zusatz += steine2[i:]
            if rest >= i:
                legen.append(i)
                (rest + zusatz) -= i
            if rest == 0:
                break

              
    return legen
i = gewichte(weight)

print(i) """


# Tipp für Zusatzaufgabe:
# Zunächst sollte Ihr Warengewicht durch 3 kg teilbar sein.
# Ist dies nicht der Fall,
# so korrigieren Sie das Gewicht mit dem 1-kg-Stein
# (war z. B. das Warengewicht 13 kg, so kommt der 1-kg-Stein nach rechts,
# und das Warengewicht wird damit auf 12 kg korrigiert).
# Mit dem 3-kg-Stein korrigieren Sie das Warengewicht weiter, sodass es durch 9 kg teilbar wird, usw.