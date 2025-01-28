
# Scheine und Münzen

# Gib für einen Geldbetrag (in Euro und Cent) die nötigen Scheine und Münzen aus.
# In Euro existieren die folgenden Beträge:
# Münzen (in Cent): 1, 2, 5, 10, 20, 50
# Münzen und Noten (in Euro): 1, 2, 5, 10, 20, 50, 100, 200, 500

# Beispiele:
# beträge(99.95) -> 50.00, 20.00, 20.00, 5.00, 2.00, 2.00, 0.50, 0.20, 0.20, 0.05
# beträge(53.26) -> 50.00, 2.00, 1.00, 0.20, 0.05, 0.01


coins = [0.01, 0.02, 0.05, 0.10, 0.20, 0.50]
notes = [1.00, 2.00, 5.00, 10.00, 20.00, 50.00, 100.00, 200.00, 500.00]

def beträge(n):
    change = []
    for note in notes[::-1]:
        while n >= note:
            n -= note
            n = round(n, 2)
            change.append(note)
    for coin in coins[::-1]:
        while n >= coin:
            n -= coin
            n = round(n, 2)
            change.append(coin)

    return(change)

print(beträge(99.95))
print(beträge(53.26))