def contar(n, c='X'):
    r = ''
    for i in range(n):
        r = r + c
    return r

if __name__ == '__main__':
    r = contar(4,'M')
    print(f'String: {r} Tamanho: {len(r)}')
