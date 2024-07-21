def fatorial(n):
    if n in [0,1]:
        return 1
    elif n < 0 or n != int(n):
        raise RecursionError
    else:
        return n * fatorial(n-1)

def numero_usuario():
    while True:
        try:
            n = int(input('n = '))
            break
        except ValueError:
            print('Digite um número!')
    return n

if __name__ == '__main__':
    while True:
        n = numero_usuario()
        try:
            f = fatorial(n)
        except RecursionError:
            print('Número inválido ou muito grande!')
        else:
            print(f'Resultado = {f}')
            break