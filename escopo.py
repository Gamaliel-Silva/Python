# Novo comentário
vg = 'global'

def variavel ():
    global vg
    vg = 'global alterado'
    vl = 'local'
    print(f'{vg} - {vl}')

if __name__ == '__main__':
    variavel()
    print(vg)