
# Fakultät

"""
Schreibe ein Skript, dass ermittelt,
welche Zahl möglichst groß ist,
ohne dass ihre Fakultät über 1.000.000.000 ist.

Hinweis:
Fakultät von 5 (Kurzschreibweise: 5!):
1 * 2 * 3 * 4 * 5 = 120
"""
from math import factorial

for i in range(1,1000):
    if factorial(i) < 1000000000:
        print(i, end=' ')
        