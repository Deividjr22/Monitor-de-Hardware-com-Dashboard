#Monitoramento 

import psutil
import time

while True :
    time.sleep(0.5)
    T = psutil.sensors_temperatures()

    sensor = list(T.keys())[0]
    T_atual = T[sensor][0].current
    
    if T_atual < 50:
        print(f"Estado Normal : {T_atual}")
    elif 50 <= T_atual < 75:
        print(f"Estado Atenção : {T_atual}")
    else: 
        print(f"Estado Critico: {T_atual}")
    