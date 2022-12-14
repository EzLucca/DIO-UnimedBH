#!/usr/bin/env python3
"""Aula classes."""


class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Plim plim...")

    def parar(self):
        print("Parando a bicicleta.")
        print("Bicicleta parada.")

    def correr(self):
        print("Vrumm ...")

    def trocar_marcha(self, nro_marcha):
        print("Trocando a marcha ...")

        # def _trocar_marcha(nro_marcha):
        #     if nro_marcha > self.marcha:
        #         print('Marcha trocada ...')
        #     else:
        #         print('Não foi possível trocar de marcha.')

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"


# b1 = Bicicleta("vermelha", "caloi", 2022, 600)
# b1.buzinar()
# b1.parar()
# b1.correr()

# print(b1.cor, b1.modelo, b1.ano, b1.valor)


b2 = Bicicleta("verde", "monark", 2000, 189)
print(b2)
