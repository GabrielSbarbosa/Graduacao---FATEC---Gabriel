## 1.	Desenvolva o código em python que crie uma imagem de largura e altura em pixels, dados pelo usuário. 
E desenhe uma moldura na imagem com 50 pixels com cor vermelha, e o fundo da imagem com cor azul. 
Obs. a largura e altura mínima é 100 pixels. ##


import cv2
import numpy as np
from google.colab.patches import cv2_imshow

Altura = int(input("Escreva a Altura >= 100 pixels: "))
Largura = int(input("\n Escreva a Largura >= 100 pixels: "))

if Altura >= 100 and Largura >= 100:

    moldy = Altura / 2 
    moldx = Largura / 2
    y0 = int(moldy) - 25
    yf = int(moldx) + 25
    x0 = int(moldy) - 25
    xf = int(moldx) + 25

    img = np.zeros([Altura,Largura,3])

    for py in range(0, Altura):
      for px in range(0, Largura):
          img[py][px][0] = 255 # cor azul 
          img[py][px][1] = 0 
          img[py][px][2] = 0 
  
    for py in range(y0, yf):
      for px in range(x0, xf):
          img[py][px][0] = 0 # cor azul
          img[py][px][1] = 0 # cor verde
          img[py][px][2] = 255 # cor vermelho 

    print('\n')
    cv2_imshow(img)
    print('\n')

else:
    print('\nValores incorretos! Insira os valores novamente.')
