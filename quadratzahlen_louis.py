
# Quadratzahlen

"""
Schreibe ein Skript, welches alle Quadratzahlen von natürlichen
Zahlen (1, 2, 3, ...) ausgibt, die kleiner als 100 sind.
(Die Quadratzahlen sollen kleiner 100 sein!)

Zusatz: Gib auch die Anzahl der gefundenen Quadratzahlen aus
"""

def quadratzahlen(q):
    return q ** 2
count = 0
for i in range(1, 101):
    quatro = quadratzahlen(i)
    if quatro < 100:
        count += 1
        print(quatro)
    else:
        break

print(f"Die Zahl der Quadratzahlen unter 100 sind: {count}")