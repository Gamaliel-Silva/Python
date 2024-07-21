n = [x for x in range(11) if x%2 != 0]
print(n)
q = list(map(lambda x: x**2, n))
q = [x**2 for x in n]
print(q)

frase = 'A lógica é apenas'
vogais = 'aeiouáéíóúàèìòùãõ'
r = [x for x in frase if x in vogais or x in vogais.upper()]
print(r)
r = [x*y for x in range(1,4) for y in range(1,3)]
print(r)