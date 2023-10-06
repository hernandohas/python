# Biblioteca
import random

# Adivinhe o numero

choice = input("Escolha um numero de 1 até 3: ")
choice = int(choice)
if choice >= 1 and choice <= 3:
    rvalue = random.randint(1, 3)
    if choice == rvalue:
        print("Congratulations, you got the number right ! ;)")
    else:
        print("So close, wrong number. The right number is: ", rvalue )
else:
    print("Invalid Number")