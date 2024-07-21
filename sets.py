planeta_anao = {'Plutão', 'Makemake', 'Ceres', 'Eris', 'Haumea'}
# print('Ceres' not in planeta_anao)
for i in planeta_anao:
    print(i.upper())
planeta_anao.clear()

astros1 = {'Lua', 'Marte', 'Vênus', 'Sirius', 'Io'}
astros1.discard('Io')
astros1.add('Urano')
astros1.pop() #elimina 1 elemento de forma aleatória
astros2 = {'Lua', 'Marte', 'Vênus', 'Sirius', 'Cometa'}
astros2.add('Sol')
print(astros1.union(astros2))
print(astros1.intersection(astros2))
print(astros1 | astros2) #união
print(astros1 & astros2) #interseção
print(astros1.symmetric_difference(astros2))