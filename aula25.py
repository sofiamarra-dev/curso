# Repeticoes
# while dentro de while

qtd_linhas = 5
qtd_colunas = 5

linha = 1 #contador
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
         print(f"{linha=},{coluna=}")#vai aparecer o nome linha e o valor usando linha=
         coluna +=1

    linha += 1
    
print("Acabou ") 