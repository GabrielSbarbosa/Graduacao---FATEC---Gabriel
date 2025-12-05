// criar um histograma em python //

import cv2
import numpy as np
from google.colab.patches import cv2_imshow

largura = 3
altura = 3

img = np.zeros([altura, largura, 3])

for py in range(0, altura):
  for px in range(0, largura):
    img[py][px][0] = imagem[py][px][0] # cor azul
    img[py][px][1] = imagem[py][px][0] # cor verde  
    img[py][px][2] = imagem[py][px][0] # cor vermelho

plt.hist(imagem.ravel(), bins = 5, range = [0,3])
plt.ylabel('bins')
plt.xlabel('range')
plt.title("Histograma da Imagem Cinza")
plt.show()
