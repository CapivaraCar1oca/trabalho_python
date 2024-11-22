num = int(input("Digite um número inteiro positivo: "))
if num > 0:
    for i in range(1, num + 1):
        print(i)
else:
    print("Erro: O número deve ser positivo.")
