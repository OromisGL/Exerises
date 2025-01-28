# TESTET DIE PERFORMANCE DER EINGEREICHTEN LÖSUNGSVORSCHLÄGE, EINFACH AUSFÜHREN!

def get_num_of_digits(TEST_VALUE):
    shift_dummy = TEST_VALUE
    num_of_bits= 1
    while(shift_dummy > 1):
        shift_dummy >>= 1
        num_of_bits += 1
    return num_of_bits

TEST_VALUE = 10_000
DIGITS = get_num_of_digits(TEST_VALUE)



# Marcel
def marcel():
    for zahl in range(TEST_VALUE):
        # Binärdarstellung mit 8 Stellen
        zahl_binary = f"{zahl:010b}" # VERÄNDERT, WEIL BEI TESTWERT 10_000, 14 Stellen benötigt
        # Leerzeichen zwischen die Ziffern einfügen
        zahl_binary_mit_leerzeichen = " ".join(zahl_binary)
        print(zahl_binary_mit_leerzeichen)

# Rick
def rick():
  """Gibt alle Zahlen von 0 bis 255 in binärer Darstellung mit Leerzeichen aus."""
  for zahl in range(TEST_VALUE):
    # Formatiere die Zahl als 8-stellige Binärzahl mit führenden Nullen
    binär_zahl = format(zahl, '010b')
    # Ersetze jedes Zeichen durch das Zeichen und ein Leerzeichen
    binär_zahl_mit_leerzeichen = binär_zahl.replace("", " ")
    print(binär_zahl_mit_leerzeichen)

# Julien
def julien():
    # determine value and position of highest bit
    num = TEST_VALUE 
    shift_dummy = num
    highest_bit = 1
    num_of_bits= 0
    while(shift_dummy > 1):
        shift_dummy >>= 1
        highest_bit *= 2
        num_of_bits += 1

    # for each number check each bit with controlbit, & and shifting 
    for n in range(num + 1):
        ctrl_bit = highest_bit
        for _ in range(num_of_bits + 1):
            print(int(ctrl_bit & n > 0), end=' ')
            ctrl_bit >>= 1
        print()

# Oemer
def oemer():
    for number in range(TEST_VALUE):
        number_as_binary= f"{number:010b}"
        number_as_binary_with_blank = " ".join(number_as_binary)
        print(number_as_binary_with_blank)

# Robert
def robert():
   #benötigte Werte
    Bits = []
    i = 0
    #Schleife für die Bits von 0 - 255
    for bit in range (TEST_VALUE):
        bitzaehler = []

        #setzt 8 pro Reihe für den Zähler
        for i in range(10):
            bitzaehler.insert(0, bit%2)
            bit //= 2
        Bits.append(bitzaehler)

    #Ausgabe
    for bitzaehler in Bits:
        for i2 in bitzaehler:
            print(i2, end=" ")
        print()

# Louis
def louis():
    for i in range(0, TEST_VALUE):
        binary = f"{i:0>10b}"
        spaced_binary = ' '.join(binary)
        print(spaced_binary)

# Marko 
def marko():
    def print_binary(num: int) -> None:
        binary = bin(num)[2:]
        spaced = " ".join(binary)
        print(spaced)


    for i in range(0, TEST_VALUE):
        print_binary(i)


###############################################
import time

marcel_start = time.time_ns()
marcel()
marcel_stop = time.time_ns()
marcel_duration = marcel_stop - marcel_start


rick_start = time.time_ns()
rick()
rick_stop = time.time_ns()
rick_duration = rick_stop - rick_start


julien_start = time.time_ns()
julien()
julien_stop = time.time_ns()
julien_duration = julien_stop - julien_start

oemer_start = time.time_ns()
oemer()
oemer_stop = time.time_ns()
oemer_duration = oemer_stop - oemer_start

robert_start = time.time_ns()
robert()
robert_stop = time.time_ns()
robert_duration = robert_stop - robert_start

louis_start = time.time_ns()
louis()
louis_stop = time.time_ns()
louis_duration = louis_stop - louis_start

marko_start = time.time_ns()
marko()
marko_stop = time.time_ns()
marko_duration = marko_stop - marko_start


players = {'Marko': marko_duration, 'Marcel': marcel_duration,
                            'Rick': rick_duration, 'Julien': julien_duration,
                            'Oemer': oemer_duration, 'Robert': robert_duration,
                            'Louis': louis_duration}

players = sorted(players.items(), key=lambda x: x[1])


for i in range(len(players)):
    print()
    print(f'{i + 1}. Platz: {players[i][0]} mit {players[i][1]/1000000} Millisekunden')
    if players[i][0] == 'Marko':
        print('\033[91m' 
              'Allerdings hat er die Aufgabe nur ungenau umgesetzt!\n'
               'Man vergleiche die ersten Zeilen seiner Ausgabe' 
               'mit dem Beispiel in der Aufgabenstellung...' 
               '\033[0m')
    