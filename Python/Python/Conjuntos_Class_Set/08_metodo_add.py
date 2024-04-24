#METODO Adiciona valor no conjunto mais não repete caso ja exista
sorteio = set({1, 23})

sorteio.add(25)
print(sorteio)

sorteio.add(42)
print(sorteio)

sorteio.add(25)
print(sorteio)
print()	