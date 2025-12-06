
import math
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def funcao_degrau(z):

   return np.where(z >= 0, 1, 0)

imagem=Image.open('/home/marciohenrique/UFS/Analise-de-Sistemas-Lineares/bethoven.jpeg')
imagem.show()

print(f"formato{imagem.format}")
print(f"tamanho{imagem.size}")
print(f"modo:{imagem.mode}")

#converter em tons de cinza

imagem=Image.open('/home/marciohenrique/UFS/Analise-de-Sistemas-Lineares/bethoven.jpeg').convert('L')
img_array = np.array(imagem, dtype=float)
print("Array da imagem",img_array)

#normalizar a imagem para 0 e 1 que será a nossa entrada

imagem_normalizada=((img_array/255)-0.5)
print("Array da imagem normalizada(entrada)",imagem_normalizada)


z=imagem_normalizada
saida= funcao_degrau(z)

# Exibir resultados
plt.figure(figsize=(10,4))

plt.subplot(1,3,1)
plt.title("Imagem Original")
plt.imshow(imagem_normalizada, cmap='gray')
plt.axis('off')


plt.subplot(1,3,3)
plt.title("Saída (Função Degrau)")
plt.imshow(saida, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()