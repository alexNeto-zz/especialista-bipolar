import operator
from functools import reduce


def verifica_conjunto(lista_sintomas, quantidade):
    return 1 if somatorio(lista_sintomas) >= quantidade else 0


def somatorio(lista_sintomas):
    print(reduce(operator.add, map(lambda i: 0 if i is None else i, lista_sintomas)))
    return reduce(operator.add, map(lambda i: 0 if i is None else i, lista_sintomas))


def ask(question):
    return 1 if input(question + " (s/n): ") == 's' else 0
