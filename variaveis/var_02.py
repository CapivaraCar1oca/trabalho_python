produto = input("Qual o nome do produto? ")
quantidade = int(input("Qual a quantidade? "))
preco_unitario = float(input("Qual o preço unitário? "))
valor_total = quantidade * preco_unitario
print(f"O valor total da compra de {produto} é R$ {valor_total:.2f}.")
