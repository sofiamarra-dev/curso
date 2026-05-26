# constante = "Variaveis" que não vão mudar muitas condições 
# no mesmo if(ruim)

velocidade = 61 # velocidade atual do carro
local_carro = 100 #local em que o carro está na estrada

RADAR_1 = 60 #Velocidade máxima do radar 1 
LOCAL_1 = 100 #Local onde o radar 1 está
RADAR_RANGE = 1 # A distancia onde radar pegar

pass_velocidade_maxima_do_radar_1 = velocidade > RADAR_1
carro_no_radar_1 =(          
   local_carro >= (LOCAL_1 - RADAR_RANGE) and
   local_carro <= (LOCAL_1 + RADAR_RANGE)     
)
carro_multado_radar_1 = carro_no_radar_1 and pass_velocidade_maxima_do_radar_1


if pass_velocidade_maxima_do_radar_1:
    print("velocidade carrou passou do radar 1")

if carro_no_radar_1 :
    print("carro passou no radar 1")

if carro_multado_radar_1:
    print("carro multado em radar 1")
