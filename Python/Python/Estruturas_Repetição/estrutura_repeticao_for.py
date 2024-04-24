texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto: 
	if letra.upper() in VOGAIS:
		print(letra.upper(), end="")

print()

#FUNÇÂO RANGE
list(range(4))
#>>> [0, 1, 2, 3]

#utilizando range com for
for numero in range(0, 11):
	print(numero, end=" ")
#>>> 0 1 2 3 4 5 6 7  8 9 10

print()
print()


# exibindo a tabuada do 5
# for numero in range(start, stop, step)
for numero in range(0, 51, 5):
	print(numero, end=" ")
#>>> 0 5 10 15 20 25 30 35 40 45 50


