import random
a = random.sample(range(20), 13)
b = random.sample(range(20), 13)
c = []
for i in a:
    if i in a and i in b and i not in c :
        c.append(i)
print (*a)
print (*b)
print (*c)        