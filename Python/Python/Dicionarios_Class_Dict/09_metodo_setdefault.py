# Metodo colocar valor padrao em chaves e adicionar novas chaves 
contatos = {
	"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

print(contatos.setdefault("nome", "Giovana"))
print(contatos)
#print(resultado)
#print(contatos["nome"])

contatos.setdefault("idade", 28)
print(contatos)