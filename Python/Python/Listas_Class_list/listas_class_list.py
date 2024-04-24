# CRIANDO LISTA
frutas = ["laranja", "maca", "uva"]
#frutas = []
letras = list("python")
números = list(range(10))
carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]

#ACESSANDO LISTA
print(frutas[1]) #maça
print(frutas[2]) #uva
print(frutas[-1]) #uva
print(frutas[-3]) #laranja
print()
print()


#LISTA ANINHADA (Matriz)
matriz = [
	[1, 'a', 2],
	['b', 3, 4],
	[6,  5, "c"]
]

print(matriz[0])           # [1, “a”, 2]
print(matriz[0][0])     # 1
print(matriz[0][-1])    #2
print(matriz[-1][-1])   #c

print()
print()


#LISTA FATIAMENTO
lista = ['P', 'y', 't', 'h', 'o', 'n']
print(lista[2:])  #[“t”, “h”, “o”, “n”]]
print(lista[:2])  #[“P”, “y”]
print(lista[1:3]) #[“y”, “t”]
print(lista[0:3:2]) # [“p”, “t”]
print(lista[::])  #[“P”, “y”, “t”, “h”, “o”, “n”]
print(lista[::-1]) #[“n”, “o”, “h”, “t”, “y”, “p”]
print()

#ITERAR(PERCORRER) A LISTA 
carros = ["gol", "celta", "palio"]

for car in carros:
    print(car)
    
print()

#FUNÇÃO ENUMERATE
carros = ["gol", "celta", "palio"]

for indice, car in enumerate(carros):
    print(f"{indice}: {car}")
    
print()

#COMPREENSÃO DE LISTAS
numeros = [1, 20, 22, 2, 9, 45, 33]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)
print()

#(COMP RANGE) outra forma de fazer
numeros = [1, 30, 21, 2, 9, 65, 34]	    
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)
print()

#MODIFICANDO O VALOR
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)

print(quadrado)    
print()
#com COMP RANGE
numeros = [1, 3, 25, 22, 15, 68, 30]
quadrado = [numero ** 2 for numero in numeros]

print(quadrado)