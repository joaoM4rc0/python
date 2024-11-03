velocidade = 80
local_carro = 99

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1 

vel_car_pass_radar_1 = velocidade > RADAR_1
carro_passou_no_radar1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado = carro_passou_no_radar1 and vel_car_pass_radar_1

if vel_car_pass_radar_1: 
    print(f'a velocidade do carro ultrapassou o limite do radar')

if carro_multado: 
    print('o carro vai receber multa')
else: 
    print('não vai receber multa')

