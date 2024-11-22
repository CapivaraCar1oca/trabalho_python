palavras = input("Digite uma lista de palavras separadas por espaço: ").split()
palavra_busca = input("Digite a palavra que deseja buscar: ")

if palavra_busca in palavras:
    print(f"A palavra '{palavra_busca}' está na lista.")
else:
    print(f"A palavra '{palavra_busca}' não está na lista.")
