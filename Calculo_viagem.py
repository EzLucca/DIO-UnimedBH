#!/usr/bin/env python3

valores = input().split()
horas = int(valores[0])
velocidade = int(valores[1])

consumo = 12
distancia = velocidade * horas

litros = distancia / consumo

print(f"{litros:.3f}")
