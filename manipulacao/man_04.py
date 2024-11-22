try:
    with open("numeros.txt", "r") as file:
        numeros = file.readlines()
        soma = sum(int(num.strip()) for num in numeros)
        print(f"A soma dos números é: {soma}")
except FileNotFoundError:
    print("Erro: O arquivo 'numeros.txt' não foi encontrado.")
except ValueError:
    print("Erro: O arquivo contém valores não numéricos.")
