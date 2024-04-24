def salvar_carro(marca, modelo, ano, placa):
 	#salva carro no banco de dados 
	print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
salvar_carro(**{"marca":"Fiat", "modelo":"Palio", "ano":1999, "placa":"ABC-1234"})
print()

def salvar_carro_2(ano, modelo, marca, placa):
 	#salva carro no banco de dados 
	print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


salvar_carro_2("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro_2(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
salvar_carro_2(**{"marca":"Fiat", "modelo":"Palio", "ano":1999, "placa":"ABC-1234"})
print()

#Esse ultimo se muda algum argumento da função ira da erro 
"""def salvar_carro_2(ano, modelox, marca, placa):
 	#salva carro no banco de dados 
	print(f"Carro inserido com sucesso! {marca}/{modelox}/{ano}/{placa}")


salvar_carro_2("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro_2(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
salvar_carro_2(**{"marca":"Fiat", "modelo":"Palio", "ano":1999, "placa":"ABC-1234"})
"""