
'Outros sinais elementares são os senos e cossenos'
import numpy as np
import matplotlib.pyplot as plt

# parâmetros do sinal
A = 2          # amplitude
f = 5          # frequência (Hz)
phi = np.pi/4  # fase (radianos)
t = np.linspace(0, 1, 1000)  # tempo de 0 a 1 segundo

# função seno
y = A * np.sin(2 * np.pi * f * t + phi)

# gráfico
plt.plot(t, y)
plt.title(f'Sinal senoidal: A={A}, f={f} Hz, fase={phi:.2f} rad')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
