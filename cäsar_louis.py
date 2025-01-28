# Cäsar-Chiffre bruteforcen

# Schreibe ein Programm, das alle möglichen Lösungen
# eines Cäsar-chiffrierten Strings ausgibt.

# Was bedeutet "vxumxgssokxkt sginz yvgyy"?

# Wer Cäsar-Chiffre nicht kennt: https://de.wikipedia.org/wiki/Caesar-Verschl%C3%BCsselung


def caeser(n):
    for shift in range(1, 9):
        if shift <= 8:
            shifted_text = ""
            for i in n:
                for j in i:
                    if j.isalpha() == True:
                        shifted_text += chr(ord(j) - shift)
                    else:
                        shifted_text += j
            print(f"{shift} {shifted_text}")

verschluesselteNachricht = "vxumxgssokxkt sginz yvgyy"

caeser(verschluesselteNachricht)