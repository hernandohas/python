# Listas
lista = ["josé", "Alves"]
lista_de_numeros = [1, 2, 3]
lista_de_floats = [1.1, 2.2, 3.3]
lista_mesclada = ["String", 1, 4.5]

# Acessando valores 
print(lista_mesclada[1])

# Acessando (inversamente) valores
print(lista_mesclada[-1])

# Sublista
frutas = ["Banana", "Maçã", "Kiwi", "Carambola", "Ameixa", "Pessego"]
print(frutas[1:4])
print(frutas[1:])
print(frutas[:4])

# Substituir valores
frutas[3] = "Ameixa"
print(frutas)

# Substituir varios valores
frutas[1:4] = ["Laranja", "Laranja","Laranja"]
print(frutas)

# Inserir Valores
frutas[1:4] = ["Laranja", "Laranja","Laranja", "Laranja"]
print(frutas)

# Buscar valor 
if "UVA" in frutas:
    print("Temos uva")