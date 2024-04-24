# CRIANDO TUPLA
frutas = ('laranja', 'Pera', 'uva',)
letras = tuple("python")
números = tuple([1, 2, 3, 4])
pais = ('Brasil',)


#ACESSANDO TUPLA
frutas = ("maça", "laranja", "Pera", "uva",)
print(frutas[0])  # maça
print(frutas[2])  # uva
print(frutas[-1])  #pera
print(frutas[-3]) #laranja

print()
print()


#TUPLA ANINHADA (Matriz)
matriz = (
	(1, 'a', 2),
	('b', 3, 4),
	(6,  5, "c"),
)

print(matriz[0])           # [1, “a”, 2]
print(matriz[0][0])     # 1
print(matriz[0][-1])    #2
print(matriz[-1][-1])   #c

print()
print()


#TUPLA FATIAMENTO
lista = ('P', 'y', 't', 'h', 'o', 'n')
print(lista[2:])  #[“t”, “h”, “o”, “n”]]
print(lista[:2])  #[“P”, “y”]
print(lista[1:3]) #[“y”, “t”]
print(lista[0:3:2]) # [“p”, “t”]
print(lista[::])  #[“P”, “y”, “t”, “h”, “o”, “n”]
print(lista[::-1]) #[“n”, “o”, “h”, “t”, “y”, “p”]
print()
print()
