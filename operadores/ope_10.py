# Solicita a idade em anos
anos = int(input("Digite a sua idade em anos: "))

# Calcula o número de anos bissextos
anos_bissextos = sum(1 for ano in range(1, anos+1) if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0))

# Calcula a idade em dias (365 dias por ano + 1 dia para cada ano bissexto)
dias = (anos * 365) + anos_bissextos

print(f"A sua idade em dias é {dias}")
