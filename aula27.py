nome =  "Sofia Marra"
tamanho_nome = len(nome)
novo_nome = ""

indice = 0

while indice  < tamanho_nome:
    letra = nome[indice]
    novo_nome += f"*{letra}" # novo_nome += "*" + letra
    indice += 1
print(novo_nome)

