
# Primzahlen-Sieb (Siebs des Eratosthenes)

"""
Schreibe ein Programm, das alle Primzahlen bis zur Zahl n ermittelt
und diese ausgibt.
Die Zahl n wird vom Benutzer übergeben.

Die Primzahlen sollen mithilfe des Siebs des Eratosthenes ermittelt werden:

- Lege eine Liste an mit den Indexen von der kleinsten natürlichen Primzahl 2
  bis zur Zahl n mit jeweils dem Wert true.
- Setze den Wert aller Indexe, die ein Vielfaches der Zahl 2 sind, auf false.
- Suche die nächstgrößere Zahl, deren Wert true ist (3)
  und setze wieder alle Vielfachen der Zahl auf false.
- Führe diesen Schritt so lange weiter durch, bis von einer Zahl
  das kleinste Vielfache ausserhalb der Liste liegt.
- Alle Indexe, deren Wert jetzt noch true sind, sind die Primzahlen.
"""

limit = int(input("Eine Posivie Zahl eingebn: "))

primzahlen = []

def isprime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def show(n):
    for i in range (2, n + 1):
        if isprime(i):
            primzahlen.append(i)
        else:
            primzahlen.append('_')

show(limit)

print(primzahlen) 