# Luftlinie

# Um die Länge der Luftlinie zwischen zwei Punkten auf der Landkarte zu berechnen,
# wird ein Programm benötigt.
#
# Schreibe eine Funktion, um den Abstand zweier Punkte in der Ebene zu berechnen.

# P1 = (x1, y1), P2 = (x2, y2).

# Berechnen damit unter anderem den (Kilometer-)Abstand der Orte Zell (704.4, 256.2)
# und Neuburg (693.3, 261.4),
# die hier in Schweizerischen Landeskoordinaten (CH1903) gegeben sind.

# Verifikation:
# P1 = (-4, 2); P2 = (-1, 6) -> Abstand = 5
# P1 = (-1, 6); P2 = (4, 18) -> Abstand = 13
# Zell und Neuburg liegen 12.26 Kilometer auseinander.
import math
def luftlinie(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    abstand = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return abstand

P1 = (-4, 2); P2 = (-1, 6)
#P1 = (-1, 6); P2 = (4, 18)

Zell = (704.4, 256.2)
Neuburg = (693.3, 261.4)

print(luftlinie(P1, P2))
print(round(luftlinie(Zell, Neuburg), 2))