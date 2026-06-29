#Monitoramento 

# import psutil
# import time

# while True :
#     time.sleep(0.5)
#     T = psutil.sensors_temperatures()

#     sensor = list(T.keys())[0]
#     T_atual = T[sensor][0].current
    
#     if T_atual < 50:
#         print(f"Estado Normal : {T_atual}")
#     elif 50 <= T_atual < 75:
#         print(f"Estado Atenção : {T_atual}")
#     else: 
#         print(f"Estado Critico: {T_atual}")
    

# import psutil

# # Tenta capturar os sensores
# T = psutil.sensors_temperatures()

# if not T:
#     print("ERRO: O psutil não encontrou nenhum sensor de temperatura.")
#     print("Dica: No Windows, o psutil nem sempre consegue ler sensores de temperatura.")
# else:
#     print("Sensores encontrados com sucesso!")
#     print(T)



# import wmi

# w = wmi.WMI(namespace="root\wmi")
# temperature_info = w.MSAcpi_ThermalZoneTemperature()

# for sensor in temperature_info:
#     # A temperatura no WMI geralmente vem em Kelvin (10x)
#     temp_celsius = (sensor.CurrentTemperature - 2732) / 10
#     print(f"Temperatura do sensor: {temp_celsius}°C")

import psutil
import time

# O psutil lê uso de CPU e Memória sem precisar de permissões especiais
while True:
    uso_cpu = psutil.cpu_percent(interval=1)
    uso_ram = psutil.virtual_memory().percent
    
    print(f"Uso de CPU: {uso_cpu}% | Uso de RAM: {uso_ram}%")
    time.sleep(1)