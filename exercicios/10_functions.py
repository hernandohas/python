# Funções
# Definição
def soma(a, b):
    print(a + b)

# Execuçãao (Invocação)
# soma(1, 7)

# Função nome_completo
def nome_completo(*nomes):
    for nome in nomes:
        print(nome)

# nome_completo("José", "Alves", "Pereira", "da", "Silva")

# Keyword Arguments
def divisao(a, b):
    print(a / b)

# divisao(b=1 , a=2)

# Valores padrão
def calcular_exp(a, b=2):
    print(a ** b)

calcular_exp(5 , 5)
