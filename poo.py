from typing import Any


class Veiculo:
    
    def __init__(self, fabricante, modelo):
        self.__fabricante = fabricante
        self.__modelo = modelo
        self.__num_registro = None

    def set_num_registro(self, nr):
        self.__num_registro = nr

    def get_num_registro(self):
        return self.__num_registro

    def movimentar(self):
        print(f'Deslocando {self.__modelo}...')

class Carro(Veiculo):
    # Método init herdado
    def movimentar(self):
        print(f'Carro deslocando na rua!')

class Motocicleta(Veiculo):
    def movimentar(self):
        print(f'Moto deslocando na rua!')

class Aviao(Veiculo):
    def __init__(self, fabricante, modelo, categoria):
        self.categoria = categoria
        super().__init__(fabricante, modelo)

if __name__ == '__main__':
    c = Carro('GM', 'Cadillac')
    c.movimentar()
    c.set_num_registro(44)
    print(f'Registro {c.get_num_registro()}')
    m = Motocicleta('Honda', '125')
    m.movimentar()
    a = Aviao('Embraer', 'E111', 'Jato comercial')