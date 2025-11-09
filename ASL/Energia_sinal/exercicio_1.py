

import math

'Quando vamos analisar a energia de um sinal devemos verificar o tamanho,amplitude e a duração do mesmo medindo sua'
'intensidade ao longo do tempo'


def funcao_sinal(t):
    return t**2

#intervalo de integracao

a=0
b=2
n=6
dt=(a-b)/n

energia=0

for i in range(0,n):
    t = a + i * dt
    energia += funcao_sinal(t)**2 * dt

print("Energia contínua (aproximada):", energia)

