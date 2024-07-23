# Novo comentário
txt = input('Digite um texto: ')
try:
    a = open('c:\\python\\mov.txt', 'r')
except IOError:
    print('Arquivo inválido!')
else:
    achou = False
    for i, l in enumerate(a):
        if txt in l:
            print(f'Linha {i}: {l}', end='')
            achou = True
    if not achou:
        print('Não encontrei o texto!')
# print(a.readlines())
# print(a.readline())

