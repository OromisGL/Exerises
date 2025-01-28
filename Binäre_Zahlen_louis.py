# Binäre Zahlen

# Schreibe ein Skript, das alle Zahlen von 0 bis 255 binär schreibt:
# Beachte die Leerzeichen zwischen den Ziffern!

"""
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1
0 0 0 0 0 0 1 0
0 0 0 0 0 0 1 1
0 0 0 0 0 1 0 0
...
...
...
1 1 1 1 1 0 1 1
1 1 1 1 1 1 0 0
1 1 1 1 1 1 0 1
1 1 1 1 1 1 1 0
1 1 1 1 1 1 1 1
"""
for i in range(0, 256):
    binary = f"{i:0>8b}"
    spaced_binary = ' '.join(binary)
    print(spaced_binary)
