if __name__ == '__main__':
    vetor: list[int] = []
    posicoes: range = range(1, 13)
    while True:
        print("Digite 12 números inteiros:")
        try:
            for i in posicoes:
                num: int = int(input())
                vetor.append(num)
            break
        except ValueError:
            print("Insira apenas números inteiros!")
            vetor.clear()
    while True:
        print("Digite a posição de 2 dos números digitados:")
        try:
            X: int = int(input())
            Y: int = int(input())
            if X not in posicoes or Y not in posicoes:
                print("Insira apenas posições de 1 a 12!")
                continue
            print(vetor[X - 1] + vetor[Y - 1])
            break
        except ValueError:
            print("Insira apenas números inteiros!")
