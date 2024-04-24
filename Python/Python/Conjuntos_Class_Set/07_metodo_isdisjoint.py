#METODO Verificar se algum elemento esta presente em outro conjunto
conjunto_a = set({1, 2, 3, 4, 5})
conjunto_b = set({6, 7, 8, 9})
conjunto_c = set({1, 0})

print(conjunto_a.isdisjoint(conjunto_b))
print(conjunto_a.isdisjoint(conjunto_c))
print()	