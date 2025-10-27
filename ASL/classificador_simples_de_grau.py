
import math
import numpy as np



x_entrada = []
pesos_rede = []

def funcao_degrau(z):
    if z < 0:
        return 0
    else:
        return 1

def neuronio():
    # Entradas e pesos
    for i in range(3):
        entrada = float(input(f"Informe o valor da entrada {i+1}: "))
        peso = float(input(f"Informe o valor do peso {i+1}: "))
        x_entrada.append(entrada)
        pesos_rede.append(peso)
    
    # Bias
    bias = float(input("Informe o valor do bias: "))

    # Produto escalar 
    soma = np.dot(x_entrada, pesos_rede) + bias

    # Aplicar a função degrau
    saida = funcao_degrau(soma)

    print("\n--- Resultados ---")
    print(f"Entradas: {x_entrada}")
    print(f"Pesos: {pesos_rede}")
    print(f"Soma (x·w + b): {soma}")
    print(f"Saída do neurônio (função degrau): {saida}")

# Executar
neuronio()
