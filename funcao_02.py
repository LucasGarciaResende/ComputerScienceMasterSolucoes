def media_aluno(nota1: float, nota2: float, nota3: float, operacao: str) -> float:
    if operacao == 'A':
        return (nota1 + nota2 + nota3) / 3
    elif operacao == 'P':
        return ((nota1 * 5) + (nota2 * 3) + (nota3 * 2)) / 10
    elif operacao == 'H':
        return 3 / ((1 / nota1) + (1 / nota2) + (1 / nota3))
    else:
        print("Insira uma operação válida")


n1: float = 9
n2: float = 6
n3: float = 8
print(f'Média Aritimética: {media_aluno(n1, n2, n3, "A")}\n'
      f'Média Ponderada: {media_aluno(n1, n2, n3, "P")}\n'
      f'Média Harmônica: {media_aluno(n1, n2, n3, "H")}\n')
