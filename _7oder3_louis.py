
numbers = []
count7 = 0
count3 = 0
for i in range(1, 101):
    if i % 3 == 0:
        count3 += 1
        numbers.append(i)
    if i % 7 == 0:
        count7 += 1
        numbers.append(i)

print(f"Die Zahl, der durch 3 teilbaren sind {count3} oder 7 Teilbaren Zahlen sind {count7}")
print(numbers)