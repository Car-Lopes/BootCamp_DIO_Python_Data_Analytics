# Metodo get se chamar uma chave que não existe e não gera erro
contatos = {"gui@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

#print(contatos["chave"]) # >>> KeyError: 'chave' chave não existe 

print(contatos.get("chave")) 
print(contatos.get("chave",{}))
print(contatos.get("gui@gmail.com",{})) # Essa chave contem
print(contatos.get("guilherme@gmail.com",{}))  #Essa chave não contem e retorna vazio


