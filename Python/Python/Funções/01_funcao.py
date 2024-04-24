#CRIANDO A FUNÇÃO
def exibir_mensagem():
	print("Ola mundo!")

def exibir_mensagem_2(nome):
	print(f"seja bem vindo {nome}!")

def exibir_mensagem_3(nome="Anonimo"):
	print(f"seja bem vindo {nome}!")

#CHAMANDO A FUNÇÃO
exibir_mensagem()
exibir_mensagem_2(nome="Guilherme")
exibir_mensagem_3()
exibir_mensagem_3(nome="Chappie")


