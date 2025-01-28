
# Zahlenreihen


# 1. Schreibe eine Schleife, die Folgendes ausgibt:
# 1 2 3 4 5
for i in range(1,6):
    print(i, end=' ')

print()
print()

# 2. Schreibe eine Schleife, die Folgendes ausgibt:
# 100 90 80 70 60 50 40 30 20 10
for i in range(100, 0, -10):
    print(i, end=' ')

# 3. Schreibe eine Schleife, die Folgendes ausgibt:
# 2000 3000 4000 5000 6000

print()
print()
for i in range(2000, 7000, 1000):
    print(i, end=' ')

print()
print()

# 4. Schreibe eine Schleife, die Folgendes ausgibt:
# 2.0 1.5 1.0 0.5 0.0 -0.5 -1.0
import numpy as np

for i in np.arange(2, -1.1, -0.5):
    print(i, end=' ')

print()
print()

# 5. Schreibe eine Schleife, die Folgendes ausgibt:
# 13 17 21 25 29

for i in range(13, 30, 4):
    print(i, end=' ')

print()
print()


# 6. Schreibe eine Schleife, die Folgendes ausgibt:
# 1.0 2.2 3.4 4.6 5.8 7.0 8.2 9.4

for i in np.arange(1, 10, 1.2):
    print(round(i, 1), end='  ')