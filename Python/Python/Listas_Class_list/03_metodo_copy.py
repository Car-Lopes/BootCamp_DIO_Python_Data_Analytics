#[].copy - Copiar Valores
lista =  [1, 'Python', [40, 30, 20]]
print("Lista 1", lista, 'ID Lista 1', id(lista))

lista2 = lista.copy()
print("Lista 2", lista2, "ID Lista 2",  id(lista2))  #  [1, “Python”, [40, 30, 20]]

print()
print()