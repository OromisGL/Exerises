c = 0
for i in dir(__builtins__):
    if i[0].islower():
        print(i, end=', ')
        c += 1

print()
print(f'Zahl der Module {c}')