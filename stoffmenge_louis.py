
# Stoffmenge

# Frau Schneider muss oft Tischdecken, Tischtücher und Tafeltücher nähen.
# Sie kennt jeweils Länge und Breite des Tisches (oder bei runden Tischen deren Durchmesser).
# Für das Tuch muss Sie jedoch auf allen Seiten noch etwas hinzugeben,
# denn einerseits soll das Tischtuch auf jeder Seite genau 20 cm herunterhängen
# und sie braucht noch 2 cm Zugabe für das Bündchen.
# In der Länge (nicht aber in der Breite) wird der Stoff
# beim 1. Waschen noch um 5 % einlaufen,
# also gibt sie dementsprechend bei der Länge hinzu.
# Runde danach auf den nächsten cm auf.
# Schreibe nun das Programm für Frau Schneider, bei welcher sie erstens eingibt,
# ob es sich um einen runden oder um einen rechteckigen Tisch handelt.
# Beim Runden gibt sie dann den Durchmesser des Tisches ein,
# wohingegen Sie beim Rechteckigen sowohl Länge als auch Breite eingibt.
# Achtung: Gebe Frau Schneider -- sie sollte es zwar wissen -- nochmals an,
# welches Maß (Länge, Breite) wegen des Einlaufens erweitert werden muss.
# Am Schluss gibt dein Programm an,
# wie viel Stoff (Länge x Breite) sie effektiv kaufen muss.
from math import ceil 

def rohmenge_r(r):
    l = (r*2) + 22
    return f'''
    Länge: {ceil((l * 0.05) + l) } cm
    Breite: {ceil(l)} cm
    '''

def rohmenge_qb(h, b):
    b = b + 22
    h = h + 22
    return f'''
    Länge: {ceil(h)} cm 
    Breite: {ceil((b * 0.05) + b)} cm
    ''' 

def rohmenge_ql(h, b):
    b = b + 22
    h = h + 22
    return f'''
    Länge: {ceil((h * 0.05) + h)} cm
    Breite: {ceil(b)} cm
    '''

def main():
    while True:
        print("\nStoffmengen Rechner:")
        print("1. Runder Tisch")
        print("2. Rechteckiger Tisch")
        print("3. Beenden")

        try:
            choice = float(input("\nBitte einer der Optionen wählen: "))
        except ValueError:
            print("Ungültige Eingabe. mögliche Optopnen 1, 2.")
            continue
        if choice == 1:
            try:
                radius = float(input("Radius in cm eingeben: "))
                print(f"Stoffbestellung {rohmenge_r(radius)}")
                break
            except ValueError:
                print("Ungültige Eingabe. Bitte eine Positive Zahl eingeben.")

        elif choice == 2:
            try:
                länge = float(input("Tischlänge in cm: "))
                breite = float(input("Tischebreite in cm: "))
                try:
                    faser = input("Faser Richtung des Stoffs Länge oder Breite (L, B): ").lower()
                except ValueError:
                    print("Ungültige Eingabe.")
                if faser == 'l':
                    try:
                        print(f"Stoffbestellung von {rohmenge_qb(länge, breite)}")
                        break
                    except ValueError:
                        pass
                elif faser == 'b':
                    try:
                        print(f"Stoffbestellung von {rohmenge_ql(länge, breite)}")
                        break
                    except ValueError:
                        pass               
                break
            except ValueError:
                print("Ungültige Eingabe. Bitte Positive Zahlen eingeben.")

        elif choice == 3:
            print("Programm wird Beendet ...")
            break

        else:
            print("Ungültige Eingabe. Bitte Wählen Sie eine Option aus dem Menü.")
            continue

if __name__ == "__main__":
    main()
    while True:
        print("Noch wünsche?")
        main_choice = input("Ja oder Nein? ").lower()
        if main_choice == "ja":
            main()
        elif main_choice == "nein":
            print("Auf Wiedersehen.")
            break
        else:
            print("UNgültige Eingabe, bitte mit Ja oder Nein antworten.")

        


