# Metodo para atualizar valor
contatos = {
	"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

contatos.update({"guilherme@gmail.com": {"nome": "Gui"}})
print(contatos)

contatos.update({"giovana@gmail.com": {"nome": "Giovana", "telefone": "3487-8881"}})
print(contatos)