# Iteravel -> str,range, etc
# Iterador -> pega os dados um por um 
# next -> me entregue o proximo valor 
# iter -> me entregue seu iterador 
# for letra in texto
texto = "Luiz"#iteravel
Iterador = iter(texto)#iterador

# while True:
#     try:
#         letra = next(Iterador)
#         print(letra)
#     except StopIteration:
#         break
 
for letra in texto:
    print(letra)