from typing import Union


class Calculadora:
    def __init__(self) -> None:
        self.__valorA: int = 0
        self.__valorB: int = 0
        self.__operador: str = '+'

    def __testar_valor(self) -> bool:
        if 100 >= self.get_valor_a() >= -100 and 100 >= self.get_valor_b() >= -100:
            return True
        return False

    def __testar_operador(self) -> bool:
        if self.get_operador() in ['+', '-', 'x', '/']:
            return True
        return False

    def get_valor_a(self) -> int:
        return self.__valorA

    def get_valor_b(self) -> int:
        return self.__valorB

    def get_operador(self) -> str:
        return self.__operador

    def set_valor_a(self, valor: int) -> None:
        self.__valorA = valor

    def set_valor_b(self, valor: int) -> None:
        self.__valorB = valor

    def set_operador(self, operador: str) -> None:
        self.__operador = operador

    def calculate(self) -> Union[int, float]:
        while True:
            try:
                if self.get_operador() == '+':
                    return self.get_valor_a() + self.get_valor_b()
                elif self.get_operador() == '-':
                    return self.get_valor_a() - self.get_valor_b()
                elif self.get_operador() == 'x':
                    return self.get_valor_a() * self.get_valor_b()
                else:
                    return self.get_valor_a() / self.get_valor_b()
            except ZeroDivisionError:
                return False

    def exibir_resultado(self):
        resultado = self.calculate()
        if resultado:
            print(f'O resultado de {self.get_valor_a()} {self.get_operador()} {self.get_valor_b()} é {resultado:,}')
        else:
            print("Divisão por 0 não é permitido!")

    def capturar_informacoes(self) -> None:
        while True:
            print("Digite uma operação para ser realizada: ")
            expressao: list[str] = input().split()
            if len(expressao) != 3:
                print("Digite apenas uma operação com número A, operador e número B. Exemplo: 4 + 10.")
                continue
            try:
                self.set_valor_a(int(expressao[0]))
                self.set_valor_b(int(expressao[2]))
                if not self.__testar_valor():
                    print("Insira apenas um valor entre 100 e -100")
                    continue
            except ValueError:
                print("Digite apenas números para realizar as operações!")
                continue
            self.set_operador((expressao[1]))
            if not self.__testar_operador():
                print("Insira um operador válido!")
                continue
            break
