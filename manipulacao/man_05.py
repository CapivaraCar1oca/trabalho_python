try:
    with open("texto.txt", "r") as file:
        conteudo = file.read()
        palavras = conteudo.split()
        print(f"O número total de palavras no arquivo é: {len(palavras)}")
except FileNotFoundError:
    print("Erro: O arquivo 'texto.txt' não foi encontrado.")
