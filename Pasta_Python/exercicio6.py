## 3.	Como é construído o histograma de uma imagem. ##

import cv2
import numpy as np
from matplotlib import pylab as plt
from google.colab.patches import cv2_imshow

 
 ## Capta a imagem e faz leitura
img = cv2.imread("pequena.jpg")

# cria uma variavel e aplica a função
imagem_result = img

# Mostra a imagem criada e original
cv2_imshow(imagem_result)

# relaciona o histograma com a imagem criada
plt.hist(imagem_result.ravel(), bins = 256, range = [0,250])
plt.ylabel('bins')
plt.xlabel('range')
plt.title("Histograma da Imagem")
plt.show()

