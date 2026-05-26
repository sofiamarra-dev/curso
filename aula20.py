# horario = int(input("informe a hora:"))

# if horario < 0 or horario > 23:
#     print("Hora invalida")
# elif horario <12:
#     print("Bom dia")
# elif horario <18:
#     print("Boa tarde")
# else:
#     ("Boa noite")



try:
  hora = int(input("digite o horario:"))
  
  if  0<= hora <=11:
     print("Bom dia")
  elif 12<= hora <=17:
     print("Boa Tarde")
  elif 18<= hora <=23:
     print("Boa noite")  
  else:
     print("Nao conheco essa hora")
except:
   print("Erro digite apenas numeros inteiros")
    








