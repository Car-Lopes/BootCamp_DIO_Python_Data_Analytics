#METODO Verifica se todos elementos de um conjunto não esta em outro conjunto
conjunto_a = set({1, 2, 3})
conjunto_b = set({4, 1, 2, 5, 6, 3})

print(conjunto_a.issuperset(conjunto_b))
print(conjunto_b.issuperset(conjunto_a))
print()	