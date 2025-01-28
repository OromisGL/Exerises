# Honky-Tonk

# Simuliere das Spiel Honky-Tonk.
# Bei diesem Spiel bezahlt der Spieler pro Runde einen Euro als Einsatz.
# Er darf nun drei Würfel werfen.
# Zeigt mindestens ein Würfel eine sechs,
# so erhält er zunächst den Einsatz zurück.
# Zudem erhält er für jede geworfene Sechs
# einen Euro als Gewinn ausbezahlt.
# Liegt keine Sechs, so verliert er den Einsatz.
# Starte mit einem Kapital von 1000 Euro und simuliere 1000 Runden.
from random import randint

Kapital = 1000
Runden = 1000

for current_round in range(Runden):
    streak = 1
    Kapital -= streak 

    würfel  = [randint(1, 6) for _ in range(3)]
    sechser = würfel.count(6)

    if sechser > 0:
        Kapital += streak 
        Kapital += sechser 

print(f"1000 Runden gespielt das Kapital beträgt noch: {Kapital}€")

