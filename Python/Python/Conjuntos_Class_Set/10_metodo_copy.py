#METODO copia valores de um conjunto
sorteio = set({1, 23})

print(sorteio)

sorteio_1 = sorteio.copy()
print(sorteio_1)

print(id(sorteio), id(sorteio_1))
print()	