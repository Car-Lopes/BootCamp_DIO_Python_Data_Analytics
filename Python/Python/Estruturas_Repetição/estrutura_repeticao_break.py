
while True:
	numero = int(input("Informe um numero: "))

	if numero == 10:
		break
	print(numero)	

print()

for numero in range(100):
	if numero == 15:
		break
	print(numero, end=" - ")

print()	
print()
for numero in range(20):
	if numero == 10:
		continue
	print(numero, end=" / ")