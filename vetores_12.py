def criar_vetor() -> list:
    vetor: list = []
    print("Digite 9 itens:")
    for i in range(0, 9):
        item: str = input()
        vetor.append(item)
    return vetor

if __name__ == '__main__':
    vetor1 = criar_vetor()
    vetor2 = criar_vetor()
    vetor3 = criar_vetor()
    print(vetor1[:3] + vetor2[3:6] + vetor3[6:])
