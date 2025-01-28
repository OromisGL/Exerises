
# Kostenberechnung

"""
Erstelle eine Funktion zur Kostenberechnung.
Dieser wird Preis, Anzahl und Währung als Argumente übergeben
und sie soll daraus die Kosten berechnen und zurückgeben.
Standardmäßig soll die Anzahl 100 betragen
und die Währung Euro sein.

Teste die Funktion:
print(berechne_kosten(2))  # 200 €
print(berechne_kosten(2, 2))  # 4 €
print(berechne_kosten(2, 2, '$'))  # 4 $
print(berechne_kosten(2, waehrung='$'))  # 200 $
"""
def berechne_kosten(a, b = 100, währung = '€'):
    if isinstance(b, str):
        währung = b
        b = 100
    kosten = a * b
    return f"{kosten:,.2f} {währung}"

print(berechne_kosten(2))  # 200 €
print(berechne_kosten(2, 2))  # 4 €
print(berechne_kosten(2, 2, '$'))  # 4 $
print(berechne_kosten(2, währung='$'))  # 200 $