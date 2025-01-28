# Fischers Fritze
# Es steht folgender String zur Verfügung:

# Gib durch String-Slicing des Strings 'satz' die folgenden Strings aus
# 1. ihsrzihf
# 2. sifhrhi
# 3. sche (mit möglichst wenig Zeichen)
# 4. eci hsr hsfziFseci 
# 5. ii i

satz = 'Fischers Fritz fischt frische Fische'
# 1. 
result1 = satz[1] + satz[4] + satz[7] + satz[10] + satz[13] + satz[16] + satz[19] + satz[22]
print(result1)

# 2. 
result2 = satz[2] + satz[11] + satz[15] + satz[19] + satz[23] + satz[27] + satz[31]
print(result2)

# 3. 
result3 = satz[2:6]
print(result3)

# 4. 
result4 = satz[-1] + satz[3] + satz[1] + ' ' + satz[4] + satz[7] + satz[6] + ' ' + satz[4] + satz[7] + satz[15] + satz[13] + satz[1] + satz[0] + satz[7] + satz[5] + satz[3] + satz[1]
print(result4)

# 5.
result5 = satz[1] + satz[1] + " " + satz[1]
print(result5)