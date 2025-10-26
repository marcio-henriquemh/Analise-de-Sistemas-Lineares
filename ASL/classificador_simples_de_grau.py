
import math
import numpy as np
import matplotlib.pyplot as plt


def funcao_degrau(z):
  return 1 if z >= 0 else 0


# Dados de exemplo (1 característica)
X = np.array([0.5, 0.4, 0.6, 0.3, 5.0])
# Classes esperadas
Y = np.array([0, 0, 1, 1, 1])


w = 1.0
b = -0.5  # ajusta o limiar para o degrau


# Classificação
Y_pred = []
for x in X:
    z = w * x + b
    y_hat = funcao_degrau(z)
    Y_pred.append(y_hat)

print("Entrada X:", X)
print("Classe prevista:", Y_pred)
print("Classe real   :", Y)