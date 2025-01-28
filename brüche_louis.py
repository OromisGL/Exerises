# Brüche kürzen

# Normalerweise darf man aus Brüchen nicht einfach einzelne Ziffern kürzen.
# So ist 18/12 natürlich nicht gleich 8/2 (wenn ich die eins kürzen würde).
# Bei einigen Zahlenpaaren funktioniert dies jedoch zufälligerweise.
# So ist (65/26) dasselbe wie 5/2 (einfach die Ziffer 6 im Zählen und Nenner streichen).
# Schreibe ein Programm, dass von allen
# zweistelligen Zahlenpaaren (Paare aus jeweils zwei zweistelligen Zahlen) angibt,
# ob die Zahl «ziffernkürzbar» ist.
# Schliesse alle Brüche aus, die sofort kürzbar sind, wie 13/13 oder 70/10
# und beschränke die Ausgabe auf die Zahlenwerte unter 1.



def kürzer():
    result = []
    for zähler in range(10, 100):
        for nenner in range(10, 100):
            if zähler >= nenner or nenner == 0:
                continue

            z1, z2 = divmod(zähler, 10)
            n1, n2 = divmod(nenner, 10)

            if z2 == n1 and n2 != 0:
                if zähler / nenner == z1 / n2:
                    result.append((zähler, nenner))
    return result
         

ziffernkürzbar = kürzer()
print("Ziffernkürzbare Brüche in 100")

for zähler, nenner in ziffernkürzbar:
    print(f"{zähler}/{nenner}")