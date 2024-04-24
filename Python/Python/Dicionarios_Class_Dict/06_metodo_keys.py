# Retorna as chaves do dicionaios 
contatos = {
	"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "gui@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}
print(contatos.keys())
resultado = contatos["guilherme@gmail.com"]
print(resultado.keys())
print(contatos["guilherme@gmail.com"].keys())

novo_dicionario = {"nota":10, "materia":"desenvolvomento Python", "curso":"python"}
print(novo_dicionario.keys())