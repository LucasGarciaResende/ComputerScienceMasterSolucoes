def calc_esfera(raio) -> float:
    pi: float = 3.14
    return 4 / 3 * pi * raio

raio = 4
print(f'Volume da esfera: {calc_esfera(raio):.4f}')