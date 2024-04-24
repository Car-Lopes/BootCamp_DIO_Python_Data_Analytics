#INPUT onde pega a entrada do teclado (espera uma entrada pelo usuario via teclado)
nome = input("Informe seu nome: ")
idade = input("Informe a idade: ")

print(nome,idade)
print('teste', end="")
print(nome,idade, end="...\n")
print(nome,idade, sep="#", end="...\n")
print(nome,idade, sep="#")