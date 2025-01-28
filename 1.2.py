def permutation(word1, word2):
    count = 0
    res1 = ''.join(sorted(word1))
    res2 = ''.join(sorted(word2))
    if len(res1) == len(res2) and (type(res1) and type(res2)) == str:
        for i in range(len(res1)):
            for j in range(len(res2)):
                if j == i:
                    count += 1
        if count == len(res1):
            return True
    return False

w = "Hello"
q = "Hello"
p = "Hoollooeeff"
x = "Hoollooeeff"

print(permutation(w, q))
print(permutation(w, p))
print(permutation(p, x))

