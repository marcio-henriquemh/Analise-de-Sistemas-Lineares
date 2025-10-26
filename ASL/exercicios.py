
#exercicios
#y(t)=u(t)+ 1/2sen(2pi-pi)

import math
import numpy as np
import matplotlib.pyplot as plt


def funcao_degrau(x):

        y = []  # armazenar os valores
        for i in x:
            if i < 0:
                y.append(0)
            else:  # considera 1 para i >= 0
                y.append(1)
        return y


def funcao_y(x):
    # converte degrau em array numpy para poder somar
    u = np.array(funcao_degrau(x))
    seno = 0.5 * np.sin(2 * x - np.pi)
    return u + seno


# Gerar eixo x e calcular
x = np.linspace(-5, 5, 1000)
y = funcao_y(x)

# Plotar
plt.plot(x, y)
plt.title('y(t) = u(t) + 1/2·sen(2x - π)')
plt.xlabel('x')
plt.ylabel('y(t)')
plt.grid(True)
plt.show()