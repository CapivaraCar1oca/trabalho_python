try:
    with open("original.txt", "r") as file_original:
        conteudo = file_original.read()
    with open("copia.txt", "w") as file_copia:
        file_copia.write(conteudo)
    print("Conteúdo copiado com sucesso para 'copia.txt'.")
except FileNotFoundError:
    print("Erro: O arquivo 'original.txt' não foi encontrado.")
