
# Ägyptisches Multiplizieren

"""
Die Ägypter hatten einen interessanten Weg gefunden,
zwei große Zahlen miteinander zu multiplizieren.
Zunächst haben sie beiden Zahlen, die es zu multiplizieren galt,
nebeneinander geschrieben, z.B.:
18 x 37
Nun geht es aber etwas anders weiter, als wir das zu tun pflegen.
Die linke Zahl wird nun für jede darunterliegende Zeile halbiert,
Nachkommastellen werden abgeschnitten.
Die rechte Zahl hingegen wird Zeile für Zeile verdoppelt.
Dies wird so lange betrieben, bis die linke Zahl gleich 1 ist.
18    37
 9    74
 4   148
 2   296
 1   592
Nun werden alle die Zeilen durchgestrichen,
bei denen die linke Zahl gerade (also ohne Rest durch 2 teilbar) ist.
18   -37-
 9    74
 4  -148-
 2  -296-
 1   592
Von den verbleibenden Zeilen werden die rechten Zahlen addiert, also:
18    --
 9    74
 4   ---
 2   ---
 1   592
     ====
     666
Und die Summe ist 666 - voilà! - zugleich das Ergebnis des Produkts aus 18 x 37.

Schreibe ein Programm, welches das Ägyptisches Multiplizieren realisiert
"""
import math

def agy(l, r):
    
    links = [l // (2 ** i) for i in range(1, math.ceil(math.log2(l)) + 1) if l // (2 ** i) > 0]
    rechts = [r * (2 ** i) for i in range(len(links) + 1)]
    links.insert(0, l)
    print(links)
    print(rechts)
    answer = 0

    for i, j in zip(rechts, links):
        if j % 2 != 0:
            answer += i

    return answer

print(agy(18, 37))