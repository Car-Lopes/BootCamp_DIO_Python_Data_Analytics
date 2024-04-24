contatos = {
	"gui@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
	"carlos@gmail.com": {"nome": "Carlos", "telefone": "2929-2222"},
	"leticia@gmail.com": {"nome": "Leticia", "telefone": "3350-4452"},
	"bernardo@gmail.com": {"nome": "Bernardo", "telefone": "3325-1111", "extra":{"a":1}},
}

print(contatos["carlos@gmail.com"]["telefone"]) # “2929-2222”
print(contatos["bernardo@gmail.com"]["extra"])
extra = contatos["bernardo@gmail.com"]["extra"]["a"]
print(extra)
print(contatos["bernardo@gmail.com"]["extra"]["a"])
print()

#INTERAR DICIONARIO
for chave in contatos:
    print(chave, contatos[chave])

print()

for chave in contatos:
    print(chave)

print()

for chave, valor in contatos.items():
    print(chave, valor)

print()
