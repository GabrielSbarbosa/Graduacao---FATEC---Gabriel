// exercicio para construir uma imagem em python // 

import cv2
import numpy as np
from matplotlib import pyplot as plt
from google.colab.patches import cv2_imshow

altura = 100
largura = 100

x0 = int(input("Digite o valor para x0 "))
xf = int(input("Digite o valor para xf "))
y0 = int(input("Digite o valor para y0 "))
yf = int(input("Digite o valor para yf "))

img = np.zeros([altura, largura, 3]) #matriz Tri dimencional

for py in range (0, altura):
  for px in range (0, largura):
    if ( (px > x0) and (px < xf) and (py > y0) and (py < yf) ):
      img[px] [py][0] = 255
      img[px] [py][1] = 255
      img[px] [py][2] = 255
    else:
      img[px] [py][0] = 127
      img[px] [py][1] = 127
      img[px] [py][2] = 127

cv2_imshow(img) #exibe a imagem criada
