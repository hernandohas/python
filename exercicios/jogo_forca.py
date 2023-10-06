palavras = {"arroz", "comunidade", "labirinto"}
letras = "a"
max_vidas = 3
erros = 0
palavra_escolhida = palavras.pop()
while erros < max_vidas:
    palavra_underlines = [letra if letra in letras else "_" for letra in palavra_escolhida]
    print("".join(palavra_underlines))
    if "_" not in palavra_underlines:
        print("Parabéns! voce acertou a palavra")
        break
    print("Vidas: ", (max_vidas - erros))
    escolha = input("Digite apenas um caractere: ")
    if len(escolha) == 1:
        if escolha in palavra_escolhida:
            letras = letras + escolha
        else:
            Print("O caractere digitado não está presente.")
            erros += 1
    else:
        print("Digite apenas um caractere.")
else:
    print("que pena, voce perdeu todas as vidas ;/")
