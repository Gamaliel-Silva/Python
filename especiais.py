from functools import reduce
quadrado = lambda x: x**2 # variável que se comporta como função
par = lambda x: x % 2 == 0
num = [1,2,3,4]
print(num)
r = list(map(quadrado, num)) # aplicar função a todos elementos da sequência
print(r)
r = list(filter(par, num)) # extrair pares
print(r)
r = list(filter(lambda x: x%2 != 0, num))
print(r)
t = reduce(lambda x, y: x**2 + y**2, num) # aplica a função para retornar um valor
print(t)