def é_par(n):
    return n % 2 == 0

# Solicitar número ao usuário
numero = int(input("Digite um número: "))
if é_par(numero):
    print(f"{numero} é par.")
else:
    print(f"{numero} é ímpar.")
