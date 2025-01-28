
# Löffelsprache

# (Bitte auch scrollen, da es unten einen Teil 2 gibt)

# Auch für diejenigen, die bereits aus dem Alter heraus sind,
# in dem sie sich mit Freunden gerne in einer Geheimsprache unterhalten,
# sollte die folgende Aufgabe interessant sein:
# Zu schreiben ist eine Funktion, die den String, den sie als Eingabe erhält,
# in die sogenannte Löffelsprache übersetzt.

"""
print(txt2loeffelsprache('Hallo'))  # halefallolefo
print(txt2loeffelsprache('Verstehst du Deutsch?'))  # veleferstelefehst dulefu deulefeutsch?
"""

# Die Codierung erfolgt nach folgenden Regeln:
# Immer, wenn ein Vokal kommt,
# wird dieser verdoppelt und dazwischen ein vorher festgelegter String gesetzt.
# Häufig wird für diesen String „lef” verwendet.
# Diphtonge werden wie ein Vokal betrachtet.
# Damit sieht die Umsetzung wie folgt aus:

"""
e = elefe
a = alefa
i = ilefi
o = olefo
u = ulefu
ü = ülefü
ö = ölefö
ä = älefä
ei = eilefei
au = aulefau
ie = ielefie
eu = eulefeu
äu = äulefau
"""

# Der Einfachheit halber wandeln wir den String vor der Kodierung in Kleinbuchstaben um,
# damit wir keine Großbuchstabenvokale und -diphtonge behandeln müssen.

coding = {
    'e':  'elefe', 
    'a':  'alefa', 
    'i':  'ilefi', 
    'o':  'olefo',
    'u':  'ulefu',
    'ü':  'ülefü',
    'ö':  'ölefö',
    'ä':  'älefä',
    'ei': 'eilefei',
    'au': 'aulefau',
    'ie': 'ielefie',
    'eu': 'eulefeu',
    'äu': 'äulefau'
    }

def txt2loeffelsprache(str):
    output = ''
    n = str.lower()
    i = 0
    while i < len(n):
        # Check for two-letter keys first
        if i + 1 < len(n) and n[i:i+2] in coding:
            output += coding[n[i+1:i+2]]
            i += 2  # Skip the next character
        elif n[i] in coding:
            output += coding[n[i]]
            i += 1
        else:
            # Non-matching characters are added as-is
            output += n[i]
            i += 1
    return output       

print(txt2loeffelsprache('Hallo'))
print(txt2loeffelsprache('Verstehst du Deutsch?'))
# Teil 2

# Schreibe eine Funktion,
# die einen String aus der Löffelsprache wieder in normales Deutsch zurück wandelt.
# Also:

# l = txt2loeffelsprache('Eineiig')
# print(l)  # eilefeineilefeiilefig
# print(loeffelsprache2txt(l))  # eineiig

# Hinweis:
# Zur Lösung dieser Aufgabe kannst du die Stringmethode replace() möglicherweise gut gebrauchen.

input1 = txt2loeffelsprache('Hallo')
input2 = txt2loeffelsprache('Verstehst du Deutsch?')

def decript(n):
    decoded = n
    for key, value in coding.items():
        decoded = decoded.replace(value, key)
    return decoded

print(decript(input1))
