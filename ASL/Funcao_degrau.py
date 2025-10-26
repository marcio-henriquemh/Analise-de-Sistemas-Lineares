
import numpy as np
import matplotlib.pyplot as plt

"Um sinal nada mais é que uma função matemática que armazena sinais dos fenomenos naturais e através de "
"um sistema converte ele em um sinal de saída, normalmente avaliamos ao longo do tempo, ou seja, o sinal de entrada"
" é um fenomemo e ele deve ser avaliado em tempos muitos grande, como o infinito."

"Sinais elementares- DEGRAU"
" É um sinal muito utilizado na elétrica para representar por exemplo passagem ou não de correntes. "

"F(x)= se 0,t<0 e 1, t>=0"
import numpy as np
import matplotlib.pyplot as plt

# definindo a função degrau 
def funcao_degrau(x):
    y = []  # armazenar os valores
    for i in x:
        if i < 0:
            y.append(0)
        else:  # considera 1 para i >= 0
            y.append(1)
    return y

# chamando a função
x = np.linspace(-5, 5, 1000)
y = funcao_degrau(x)

# plotando
plt.plot(x, y)
plt.title('Função Degrau Unitário')
plt.xlabel('x')
plt.ylabel('função degrau')
plt.grid(True)
plt.show()

