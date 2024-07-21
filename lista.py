# n1 = [10,8,5,7,6]
# n2 = [4,9]
# n = n1 + n2
# n.append(11)
# print (n)    
# n.pop(1)
# print (n)
# n.insert(1,21)
# print(n)
# print(33 in n)

lista = []
for i in range(5):
    lista.append(input(f'{i+1}- Bebida favorita: '))
lista.sort()
for i in lista:
    print(i)
