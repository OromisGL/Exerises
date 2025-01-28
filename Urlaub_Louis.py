#  Urlaubsanspruch
#
#  Für die Bestimmung des Urlaubsanspruchs der Beschäftigten einer Firma
#  soll ein Programm entwickelt werden.
#  Die Grundlage für die Berechnung des Urlaubsanspruchs
#  bildet die Betriebsvereinbarung.
#  Das Programm soll die Anzahl der Urlaubstage für
#  jeweils einen Beschäftigten berechnen.
#
#  Betriebsvereinbarung:
#  Allen Beschäftigten stehen 26 Tage Urlaub zu.
#  Minderjährige Beschäftigte erhalten 30 Tage Urlaub.
#  Beschäftigte, die älter als 55 Jahre sind, erhalten 28 Tage Urlaub.
#  Beschäftigte mit einer Behinderung ab 50 % erhalten
#  zusätzlich 5 weitere Tage Urlaub.
#  Beschäftigte mit einer Betriebszugehörigkeit von mehr als 10 Jahren
#  erhalten 2 zusätzliche Tage Urlaub.

alter = int(input("Bitte Ihr alter eingeben: "))
handycap = int(input("Grad der Behinderung in Prozent: "))
arbeit = int(input("Dauer im Betrieb: "))

jung = 30
normal = 26
alt = 28
dauer = 10

if handycap >= 50:
      jung += 5
      normal += 5
      alt += 5

if arbeit > 10:
      normal += 2
      alt += 2
      jung += 2

while 55 > alter > 18:
        print(f"Urlaubsanstpuch {normal}  Tage/Jahr")
        if alter > 55:
            print(f"Urlaubsanstpuch {alt} Tage/Jahr")
        elif alter < 18:
            print(f"Urlaubsanstpuch {jung} Tage/Jahr")
        break