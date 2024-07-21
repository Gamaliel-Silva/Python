import random as r
v = []
valor = None
for i in range(6):
    while(valor == None or valor in v):
        valor = r.randint(1,100)
    v.append(valor)
v.sort()
print(v)
r.shuffle(v)
print(v)
