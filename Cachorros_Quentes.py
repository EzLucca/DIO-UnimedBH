#!/usr/bin/env python3

valores = input(
    "Digite a quantidade de cachorros quentes devorados e o número de participantes: "
).split()

h = int(valores[0])
p = int(valores[1])

if h < 1:
    print("O número de cachorros quentes não pode ser menor que 1.")
elif p > 1000:
    print("O número de participantes deve ser inferior a 1000.")
else:
    cachorro_medio = h / p
    print(f"{cachorro_medio:.2f}")
