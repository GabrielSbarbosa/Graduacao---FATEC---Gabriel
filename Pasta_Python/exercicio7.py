##Faça um programa em python que mostre a imagem original, a imagem 
##em tons de cinza e plote o histograma em tons de cinza de uma imagem. Mostre 
##na tela, os 10 valores de máximos entre 30 e 220

import cv2
import numpy as np
import matplotlib.pyplot as plt
from google.colab.patches import cv2_imshow

imagem = cv2.imread("pequena.jpg")
gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
cv2_imshow(gray)
cv2_imshow(imagem)

plt.hist(gray.ravel(), bins = 220, range = [30,220])
plt.ylabel('bins')
plt.xlabel('range')
plt.title("Histograma da Imagem Cinza")
plt.show()
