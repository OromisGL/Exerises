john = input("String input: ")
count = int(input("Zahl: "))


def URLify(word, lens):
    stripped = word.strip()
    if len(stripped) == lens:
         return stripped.replace(' ', '%20')
    else:
         return None

print(URLify(john, count))