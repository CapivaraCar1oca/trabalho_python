numeros = []
while True:
    entrada = input("Digite um número (ou 'fim' para encerrar): ")
    
    if entrada.lower() == 'fim':
        break
    
    try:
        numero = float(entrada)
        numeros.append(numero)
    except ValueError:
        print("Por favor, digite um número válido ou 'fim' para encerrar.")

if len(numeros) > 0:
    media = sum(numeros) / len(numeros)
    print(f"A média aritmética dos números é {media}")
else:
    print("Nenhum número foi inserido.")
