if __name__ == '__main__':
    flag: bool = False
    while True:
        print("Digite uma palavra de 4 letras")
        vetor1: list[str] = list(input())
        if len(vetor1) != 4:
            print("Insira somente 4 letras!")
            continue
        for letra in vetor1:
            if not letra.isalpha():
                print("Insira uma palavra com apenas letras!")
                flag = True
                break
        if flag:
            continue
        print("Digite a segunda palavra")
        vetor2: list[str] = list(input())
        if len(vetor2) != 4:
            print("Insira somente 4 letras!")
            continue
        for letra in vetor2:
            if not letra.isalpha():
                print("Digite apenas uma palavra com apenas letras")
                flag = True
                break
        if flag:
            continue
        vetor1.sort()
        vetor2.sort()
        if vetor1 == vetor2:
            print("São anagramas!")
        else:
            print("Não são anagramas!")
        break
