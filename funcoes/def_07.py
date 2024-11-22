def calcular_preco_final(preco, desconto):
    return preco - (preco * desconto / 100)

# Solicitar preço e desconto ao usuário
preco_produto = float(input("Digite o preço do produto: "))
desconto = float(input("Digite o percentual de desconto: "))
print(f"O preço final do produto com desconto é: {calcular_preco_final(preco_produto, desconto)}")
