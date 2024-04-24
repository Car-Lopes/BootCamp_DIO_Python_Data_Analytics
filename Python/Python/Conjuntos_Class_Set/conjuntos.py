#CRIANDO SET
numeros = set([1, 2, 3, 4])
print(numeros)

letras = set("abacaxi")
print(letras)

carro = set(("palio", "celta", "gol", "palio"))
print(carro)
print()

#ACESSANDO OS DADOS DO SET
numeros = {1, 2, 3, 2}
numeros = list(numeros)
print(numeros[0])
print()

#PERCORRENDO(INTERANDO) O SET
carros = {'gol', 'celta', 'palio'}
for carro in carros:
	print(carro)
print()

#FUNÇÂO ENUMERATE
carros = {'gol', 'celta', 'palio'}
for indice, carro in enumerate(carros):
	print(f"{indice}: {carro}")
print()

