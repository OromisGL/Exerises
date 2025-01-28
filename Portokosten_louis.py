# Portokosten
 
"""

Die Portokosten (Versandkosten) sind wie folgt festgelegt:

0 - 39.99 € Bestellwert kosten 3.99 € Porto

40 - 69.99 € Bestellwert kosten 2.99 € Porto

70 - 99.99 € Bestellwert kosten 1.99 € Porto

ab 100 € ist portofrei
 
Es soll eine Zufallszahl (bestellwert)

von 1.00 - 130.00 erzeugt werden (z.B. 40.47, 123.78)
 
Dann soll ermittelt werden,

wie hoch die entsprechenden Portokosten sind.

Am Ende sollen der Bestellwert, die Portokosten

und der Gesamtbetrag ausgegeben werden.

"""
from random import uniform

bestellung = round(uniform(1.00, 130.00), 2)

print(f"Bestellwert {bestellung}")

if bestellung < 40:
    print("Porto 3,99€")
elif bestellung >= 40 and bestellung < 70:
    print("Porto 2,99€")
elif bestellung >= 70 and bestellung < 100:
    print("Porto 1,99€")
else:
    print("Portofrei")
