# Großbuchstaben

# Schreibe ein Python-Programm, das sämtliche existierenden Kombinationen
# aus zwei großen Buchstaben auf den Bildschirm schreibt.

"""
AA AB AC AD AE AF AG AH AI AJ AK AL AM AN AO AP AQ AR AS AT AU AV AW AX AY AZ
BA BB BC BD BE BF BG BH BI BJ BK BL BM BN BO BP BQ BR BS BT BU BV BW BX BY BZ
CA CB CC CD CE CF CG CH CI CJ CK CL CM CN CO CP CQ CR CS CT CU CV CW CX CY CZ
...
XA XB XC XD XE XF XG XH XI XJ XK XL XM XN XO XP XQ XR XS XT XU XV XW XX XY XZ
YA YB YC YD YE YF YG YH YI YJ YK YL YM YN YO YP YQ YR YS YT YU YV YW YX YY YZ
ZA ZB ZC ZD ZE ZF ZG ZH ZI ZJ ZK ZL ZM ZN ZO ZP ZQ ZR ZS ZT ZU ZV ZW ZX ZY ZZ
"""
for i in range(ord('A'), ord('Z') + 1):
    for j in range(ord('A'), ord('Z') + 1):
        if  j == ord('Z'):
            print(f"{chr(i)}{chr(j)}", end=' ')
            print()
        else:
            print(f"{chr(i)}{chr(j)}", end=' ')