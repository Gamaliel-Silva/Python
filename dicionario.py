carro = {
    'Marca': 'VW',
    'Modelo': 'Up!',
    'Ano': 2016
}

carro['Marca'] = 'Volks'
carro['Motor'] = '1.0'
del carro['Motor']
carro['Cor'] = 'preta'
for i, j in carro.items():
    print(f'{i} : {j}')
print(carro.keys())
print(carro.values())
# for i in carro.keys():
#     print(i)
# for i in carro.values():
#     print(i)
carro.clear()
del carro