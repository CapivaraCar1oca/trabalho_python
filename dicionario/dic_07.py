produtos = {"Arroz": 20.50, "Feijão": 7.80, "Açúcar": 3.90, "Óleo": 6.50, "Leite": 4.30}
produto = input("Digite o nome do produto: ")
if produto in produtos:
    print(f"O preço de {produto} é R$ {produtos[produto]:.2f}.")
else:
    print(f"{produto} não foi encontrado.")
