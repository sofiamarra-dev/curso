# Iteravel -> str,range, etc
# Iterador -> quem sabe entregar um valor por vez
# next -> me entregue o proximo valor 
# iter -> me entregue seu iterador 

texto = iter("Luiz")#__iter__()

print(next(texto))#ou print(texto.__next__())78
print(next(texto))
print(next(texto))
print(next(texto))