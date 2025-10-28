import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def sigmoid_derivada(z):
    return sigmoid(z) * (1 - sigmoid(z))

def carregar_img(caminho, tamanho=(64, 64)):
    img = Image.open(caminho).convert('L').resize(tamanho)
    return np.array(img, dtype=float).flatten() / 255.0

# 🔹 Duas imagens para classificar
x1 = carregar_img('/home/marciohenrique/UFS/ASL/bethoven.jpeg')  # Beethoven → 1
x2 = carregar_img('/home/marciohenrique/UFS/ASL/albert-einstein.jpg')  # Einstein → 0
x3=carregar_img('/home/marciohenrique/UFS/ASL/caramelo.jpg')#caramelo
# 🔹 Agrupando as entradas e saídas desejadas
X = np.array([x1, x2, x3])
y = np.array([1, 0,0])

#  Inicialização
np.random.seed(42)
w = np.random.randn(X.shape[1]) * 0.01  # um peso por pixel
b = -3.0
alpha = 0.1  # taxa de aprendizado

#  Treinamento
for epoca in range(100):
    erro_total = 0
    for i in range(len(X)):
        z = np.dot(w, X[i]) + b
        y_pred = sigmoid(z)
        erro = y[i] - y_pred
        erro_total += abs(erro)

        # Gradientes
        dw = erro * sigmoid_derivada(z) * X[i]
        db = erro * sigmoid_derivada(z)

        # Atualização
        w += alpha * dw
        b += alpha * db

    if epoca % 10 == 0:
        print(f"Época {epoca:02d} | Erro médio = {erro_total/len(X):.6f}")

print(" Treinamento concluído!")

# Teste com uma das imagens
z_final = np.dot(w, X[1]) + b
y_final = sigmoid(z_final)
print(f"Saída para Beethoven: {y_final:.3f}")

# 🔹 Visualização
plt.figure(figsize=(10,4))

plt.subplot(1,3,1)
plt.title("Imagem (Beethoven)")
plt.imshow(X[1].reshape(64,64), cmap='gray')
plt.axis('off')


plt.subplot(1,3,2)
plt.title(f"Soma ponderada z = {z_final:.3f}")
plt.text(0.5, 0.5, f"z = {z_final:.3f}", fontsize=12, ha='center')
plt.axis('off')

plt.subplot(1,3,3)
plt.title(f"Saída sigmoide = {y_final:.3f}")
plt.text(0.5, 0.5, f"{y_final:.3f}", fontsize=16, ha='center')
plt.axis('off')

plt.show()