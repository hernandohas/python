# Dictionaries
# Definição
phones = {
    "João": 12345678,
    "Maria": 12345905
}

# Acessando
# print(phones['Maria'])

# # IF 
# if "João" in phones:
#     print("Tenho o João na lista de contatos")

# # FOR
# for chave, valor in phones.items():
#     print(chave, valor)

# Adicionando Itens
phones["Augusto"] = 96326198

# Removendo Itens
phones.pop("Maria")

# Unindo dois dicionarios
phones_2 = {"Cecilia": 111111111, "Augusto": 222222222}
phones.update(phones_2)
print(phones)
