# operadores logicos
# and (e) or (ou) not(não)
# and - Todas as condicoes precisam ser verdadeiras
# se qualquer valor for considerado falso,a expressão inteira sera avaliada naqule valor
# sao considaerados false (que vc ja viu )
# 0 0 . 0 "" false
# tambem existe  o tipo None que e usado para representar um nao valor 

entrada = input("[E]ntrar [S]air:").upper()
senha_digitada = input("senha:")

senha_permitida = "123456"
if entrada =="E" and senha_digitada == senha_permitida:
  print("Entrar") 
else:
  print("sair")
