#Metodo para criar atributos com valores vazios
contato = dict.fromkeys(["nome","telefone"])
print(contato)

contato2 = dict.fromkeys(["nome","telefone"], "vazio")
print(contato2)