#Parametro Keyword and Positional Only (Parametro por posição e nomeados)
def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

                 #Posição                     #Nomeado
criar_carro("Palio", 1999, 'ABC-1234', marca="Fiat", motor="1.0", combustivel="Gasolina")
#criar_carro(modelo="Palio", ano=1999, placa='ABC-1234', marca="Fiat", motor="1.0", combustivel="Gasolina") # Invalido

print()

#Parametro Keyword and Positional Only (Parametro por posição e nomeados)
def criar_carro_2(modelo, ano, /, placa, marca, *, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

                 #Posição                     #Nomeado
criar_carro_2("Palio", 1999, placa='ABC-1234', marca="Fiat", motor="1.0", combustivel="Gasolina")
#criar_carro_2(modelo="Palio", ano=1999, placa='ABC-1234', marca="Fiat", motor="1.0", combustivel="Gasolina") # Invalido
