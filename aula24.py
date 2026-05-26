# Repetiçoes
# while
# Executa uma açao enquanto uma condicao for verdadeira 
# Loop infinito -> Quando um codigo não tem fim

contador = 0 

while contador <=100:
    contador = contador + 1
    
    if contador == 6:
        print("Nao vou mostrar o 6 ")
        continue
    
    if  10 <= contador <=27:
        print("nao vou mostrar o",contador)
        continue


    print(contador)

    if contador == 40:
        break

print("acabou")