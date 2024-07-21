def numero_usuario(i=1):
    while True:
        try:
            n = int(input(f'n{i} = '))
            break
        except ValueError:
            print('Digite um número!')
    return n

n1 = numero_usuario()
while True:
    n2 = numero_usuario(2)
    try:
        r = n1/n2
    except ZeroDivisionError:
        print('Erro de divisão por zero!')
    else:
        print(r)
        break
