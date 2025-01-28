
# Doppelte Zahl

"""
Schreibe eine Funktion, die überprüft,
ob in einer Liste mit Zahlen zwei Zahlen gleich sind.
Der Funktion wird die Liste übergeben
und sie soll True zurückgeben, wenn es Doppelte gibt
und ansonsten soll die Funktion False zurückgeben.
"""



uni = set()
dopp = set()
def checke_doppelte(list):
    for i in list:
        if i in dopp:
            uni.add(i)
        else:
            dopp.add(i)
    if len(uni) > 1:
        return False
    else:
        return True

# Beispiel:
zahlen1 = [1, 3, 7, 9, 7, 11, 17]
zahlen2 = [1, 3, 7, 9, 11, 17]
print(checke_doppelte(zahlen1))  # True
print(checke_doppelte(zahlen2))  # False