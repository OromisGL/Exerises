
# Nettopreis
 
"""
Schreibe eine Funktion zum Berechnen des Nettopreises.
Dieser Funktion soll der Bruttopreis übergeben werden
und sie soll den Nettopreis zurückgeben.
Der Mehrwertsteuersatz soll als zweiter Parameter
übergeben werden können.
Der Standardwert des Mehrwertsteuersatzes soll 19 sein.
 



Teste die Funktion:
print(berechne_netto(119))     # 100.0
print(berechne_netto(107, 7))  # 100.0
"""

def berechne_netto(a, b = 19):
    netto = a - (a * (b/(100+b)))
    return f"{netto:.1f}"

print(berechne_netto(119))     
print(berechne_netto(107, 7))  