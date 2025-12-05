// Exercicio de tratamento de imagens em Python, utilizando o google colab ##

// Faça um programa de tratamento de imagem, usando a detecção por Canny, redesenhar o contorno na imagem original.

import cv2
import numpy as np
import matplotlib.pylab as plt
from google.colab.patches import cv2_imshow

imagem = cv2.imread("circulos_1.png") #captura a imagem adicionada

gray = cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (5,5),0)

#pega a imagem original e adapta um novo threshould com outro threshold

thresh = cv2.adaptiveThreshold(blur,200,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,23,3)

#outra função de extração do ponto maxi e min de cada contorno (sem calcular x0, x1 e y0,y1) e posições

cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cnts = cnts[0] if len(cnts) == 2 else cnts[1]

for c in cnts:
    
    area = cv2.contourArea(c)
        
    if (area > 10): #tamanho maior que 10 pixel será desenhado uma borda
 
          cv2.drawContours(imagem,[c], -1,(0,0,0),10)#desenha espessura de 10 na cor preta sobre a imagem
          cv2_imshow(imagem)
