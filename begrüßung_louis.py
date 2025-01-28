# Begrüßung

# Es soll eine Begrüßung in Abhängigkeit zur Uhrzeit ausgegeben werden.

# Zwischen 22Uhr und 5Uhr: Gute Nacht
# Vor 11Uhr: Guten Morgen
# Vor 15Uhr: Mahlzeit
# Vor 18Uhr: Guten Nachmittag
# Vor 22Uhr: Guten Abend

# Benutze zum Testen randint(0, 23),
# um eine Zahl von 0 bis 23 zu erzeug
from random import randint

Uhrzeit = randint(0, 24)

if Uhrzeit < 11:
    print(f"Vor {Uhrzeit}: Guten Morgen")
elif Uhrzeit < 15 and Uhrzeit > 11:
    print(f"Vor {Uhrzeit}: Mahlzeit")
elif Uhrzeit < 18 and Uhrzeit > 15:
    print(f"Vor {Uhrzeit}: Guten Nachmittag")
else:
    print(f"Vor {Uhrzeit}: Guten Abend")