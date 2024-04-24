nome = "Carlos"
idade = 28
profissao = "Programador"
linguagem = 'Python'
saldo = 45.435

dados = {"nome": "Calor Lopes", "idade": "30"}

print("Nome: %s Idade: %d" %(nome,idade))

print("Nome: {} Idade: {}" .format(nome,idade))

print("Nome: {0} Idade: {1}" .format(nome,idade))

print("Nome: {1} Idade: {0}" .format(idade,nome))
print("Nome: {1} Idade: {0} {0} {1}" .format(idade,nome))

print("Nome: {nome} Idade: {idade}" .format(nome=nome,idade=idade))
print("Nome: {name} Idade: {age}" .format(name=nome,age=idade))
print("Nome: {nome} Idade: {idade}" .format(**dados))

print(f"nome:{nome} Idade:{idade}")
print(f"nome:{nome} Idade:{idade} Saldo: {saldo:.2f}")
print(f"nome:{nome} Idade:{idade} Saldo:{saldo:10.2f}")
print(f"nome:{nome} Idade:{idade} Saldo:{saldo:10.1f}")



