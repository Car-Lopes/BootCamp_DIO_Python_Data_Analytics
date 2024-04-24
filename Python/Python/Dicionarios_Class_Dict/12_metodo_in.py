#Metodo para retorna se contem as chaves
contatos = {
	"gui@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
	"carlos@gmail.com": {"nome": "Carlos", "telefone": "2929-2222"},
	"leticia@gmail.com": {"nome": "Leticia", "telefone": "3350-4452"},
	"bernardo@gmail.com": {"nome": "Bernardo", "telefone": "3325-1111", "extra":{"a":1}},
}

print("gui@gmail.com" in contatos)
print("megui@gmail.com" in contatos)
print("idade" in contatos["gui@gmail.com"])
print("telefone" in contatos["bernardo@gmail.com"])