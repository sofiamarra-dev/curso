# Repeticoes
# While (enquanto)
# executa uma acão enquanto uma condicãi for verdadeira

condicao = True

while condicao:
    nome = input("qual seu nome:")
    print(f"seu nome e {nome}")
    
    if nome == "sair":
       break 

print("acabou")