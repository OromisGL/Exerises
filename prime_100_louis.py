# Primzahlen rückwärts

"""
Schreibe ein Programm, das alle Primzahlen bis 1000 ausgibt,
die, wenn man sie rückwärts liest, auch eine Primzahl sind.
"""
primzahlen = []

def isprime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def reverse(n):
    return str(n)[::-1]
   
for i in range(1, 1001):
    if isprime(i) and str(i) == reverse(i):
        primzahlen.append(i)

print(primzahlen)