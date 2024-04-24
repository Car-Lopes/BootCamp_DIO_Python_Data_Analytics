#Metodo para copiar um dicionario existente
contatos = {
	"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
}

contatos1 = contatos.copy()
contatos1["guilherme@gmail.com"] = {"nome": "Gui"}

print(contatos["guilherme@gmail.com"])
print(contatos1["guilherme@gmail.com"])
