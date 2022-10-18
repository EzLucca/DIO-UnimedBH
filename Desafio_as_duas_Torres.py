#!/usr/bin/env python3

entrada = input(
    "Digite a distância entre os palantíres, seguido do diametro do palantír de Sauron e de Saruman:"
).split()

distancia = int(entrada[0])
diametro1 = int(entrada[1])
diametro2 = int(entrada[2])

if distancia > 10000:
    print("O valor da distância deve ser menor que 10000.")

elif diametro2 > 100:
    print("O valor do diametro do palantir de Saruman deve ser menor que 100.")
# O Cálculo do ICM deve ser feito dividindo a distância pela soma dos diametros dos palantir

# Calculando do ICM

else:
    icm = distancia / (diametro1 + diametro2)
    print(f"{icm:.2f}")
