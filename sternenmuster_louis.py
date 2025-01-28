# Sternenmuster

# Schreibe ein Python-Programm,
# das folgende Sternchen-Muster auf den Bildschirm schreibt:

"""
* * * *
* * * *
* * * *

*
* *
* * *
* * * *
* * * * *

      *
    * * *
  * * * * *
* * * * * * *
"""


wi = 4

for i in range(0, wi):
    for j in range(0, wi):
        print("*", end=' ')
        if j >= wi:
            print(" ", end="")
    print()


print()
print()



m = 5

for i in range(0, m):
    for j in range(0, i + 1):
        print("*", end=' ')
    print()

print()
print()


hei = 4
widt = 7

for i in range(hei):
    for j in range(widt):
        if widt // 2 - i <= j <= widt // 2 + i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
