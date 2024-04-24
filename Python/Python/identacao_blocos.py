
valor = float(input("Digite o valor a sacar: "))

def sacar(valor):
    saldo = 500
    saldo -= valor
    if saldo >= valor:
        print("Valor sacado!")
        print("retire o dinheiro no caixa.")

    else :
        print("Seu Saldo é menor que o valor a sacar /n")
    
    print()
    print("Novo Saldo", saldo)
    print("Obrigado e volte sempre!")

sacar(valor)    

valor = float(input("Digite o valor a depositar: "))
def depositar(valor):
    saldo = 500
    saldo += valor
    print("Valor Depositado", valor)
    print("Novo saldo", saldo)

depositar(valor)


