# Metodo para remover a chave
contatos = {
	"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "gui@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

print(contatos.pop("guilherme@gmail.com"))
print(contatos.pop("guilherme@gmail.com",{}))
print(contatos)
