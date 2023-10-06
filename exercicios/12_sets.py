# Sets
my_set = {1, 2, 3}
# print(my_set)
my_set_empty = set()

# print(my_set)
# print(my_set_empty)

# Adicionando itens

my_set_empty.add("Texto")
my_set_empty.update([4, 78.6])
# print(my_set_empty)

# Removendo itens
my_set_empty.discard("Texto")
# my_set_empty.remove("Texto")

# print(my_set_empty)

# Operadores
set_a = {1, 2, 3}
set_b = {3, 4, 5}

# União
uniao = set_a | set_b
uniao = set_a.union(set_b)


# Intersecção
interseccao = set_a & set_b
interseccao = set_a.intersection(set_b)
# print(interseccao)

# Diferença unitária (set)
dif_unitaria = set_a - set_b
dif_unitaria = set_a.difference(set_b)

# DIferença simétrica
dif_simetrica = set_a ^ set_b
dif_simetrica = set_a.symmetric_difference(set_b)
print(dif_simetrica)