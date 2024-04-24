# Metodo para remover os itens da sequencia sem passa chaver
contatos = {
	"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "gui@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

print(contatos.popitem())
print(contatos)
print(contatos.popitem())
print(contatos)
#print(contatos.popitem()) # Aqui ira da erro pois ja removeu todas as chaves
