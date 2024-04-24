#Metodo para deletar chaves
contatos = {
	"gui@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
	"carlos@gmail.com": {"nome": "Carlos", "telefone": "2929-2222"},
	"leticia@gmail.com": {"nome": "Leticia", "telefone": "3350-4452"},
	"bernardo@gmail.com": {"nome": "Bernardo", "telefone": "3325-1111", "extra":{"a":1}},
}

del contatos["gui@gmail.com"]["telefone"]
print(contatos)

del contatos["carlos@gmail.com"]
print(contatos)

# del contatos # Aqui esta deletando o dicionario por completo
