preco = float(input("Digite o preço do produto: "))
desconto_percentual = float(input("Digite a porcentagem de desconto: "))
desconto = (desconto_percentual / 100) * preco
preco_final = preco - desconto
print(f"O valor do desconto é {desconto} e o preço final do produto é {preco_final}")
