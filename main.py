print("-------------")
print("bem vindo ao jogo de adivinhação!")
print("-------------")

n_secreto = 100
entrada = int(input("digite um numero:"))
acerto = entrada == n_secreto
entrada_maior = entrada > n_secreto
entrada_menor = entrada < n_secreto
print(type(acerto))

print(f"Você digitou o número: {entrada}")


if(acerto):
    print(f"Parabens você acertou o numero secreto")
else:
    if(entrada_maior):
        print("o numero digitado foi maior do que o numero secreto")
    if(entrada_menor):
        print("o numero digitado foi menor do que o numero secreto")
    print("Fim de jogo!")