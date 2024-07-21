import random
lista = []
n = random.randint(1,60)
for i in range(6):
    while n in lista:
        n = random.randint(1,60)
    lista.append(n)
    lista.sort()
print(lista)

print('pronto!')