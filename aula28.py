# Calculadora com while
while True:
   numero_1 = input("Informe um valor:")
   numero_2 = input("Informe um segundo valor:")
   operador = input("informe o operador (+-/*):")
   
   numeros_validos = None
   num_1_float = 0
   num_2_float = 0
   
   try:
    num_1_float = float(numero_1)
    num_2_float = float(numero_2)
    numeros_validos = True #numero e valido
   except:
    numeros_validos = False #numero nao e valido 

   if not numeros_validos :
    print("Um ou ambos os numeros digitados  sao invalidos")
    continue 

   operadores_permitidos = "+-/*"

   if operador not in operadores_permitidos:
     print("Operador invalido")
     continue

   if len(operador) > 1:
    print("Digite apenas um operador")
    continue
   
   print("Realizando sua conta ...")
   if operador == "+":
     print(f"{num_1_float}+{num_2_float}=",num_1_float + num_2_float)
   elif operador  == "-":
     print(f"{num_1_float}-{num_2_float}=",num_1_float - num_2_float)
   elif operador == "/":
     print(f"{num_1_float}/{num_2_float}=",num_1_float / num_2_float)
   elif operador == "*":
     print(f"{num_1_float}*{num_2_float}=",num_1_float * num_2_float)
   
   sair = str(input("Quer sair? [s]im:")).lower().startswith("s")
  
   if sair:
     break
   

                  