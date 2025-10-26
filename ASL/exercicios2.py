
import math
import numpy as np
import matplotlib.pyplot as plt


def funcao_degrau(x):
    y = []  # armazenar os valores
    for i in x:
        if i < 0:
            y.append(0)
        else:
            y.append(1)
    return y


def funcao_y(x):
    # calcula (sen(x))² * u(x - 1)
    u = np.array(funcao_degrau(x - 1))
    seno2 = np.power(np.sin(x), 2)
    return seno2 * u


# eixo x
x = np.linspace(-5, 5, 1000)

# calcula y(t)
y = funcao_y(x)

# plota o gráfico
plt.plot(x, y)
plt.title('y(t) = (sen(x))² · u(x - 1)')
plt.xlabel('x')
plt.ylabel('y(t)')
plt.grid(True)
plt.show()
