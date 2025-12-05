// Formar um X vermelho em python // 

import cv2
import numpy as np
from google.colab.patches import cv2_imshow
import matplotlib.pyplot as plt

largura = input(" Valor da largura: ")
altura = largura

largura = int(largura)
altura = int(altura)

imagem = np.zeros([altura, largura, 3])

if largura >= 3 and altura >= 3:
    for linha in range(altura):
        for coluna in range(largura):
            imagem[linha][coluna][0] = 255
            imagem[linha][coluna][1] = 255
            imagem[linha][coluna][2] = 255

    for linha in range(altura):
        for coluna in range(largura):
            if linha == coluna:
                imagem[linha][coluna][0] = 0
                imagem[linha][coluna][1] = 0
                imagem[linha][coluna][2] = 255
    
    contadora_altura = altura - 1
    contadora_largura = 0
    
    for linha in range(altura):
        for coluna in range(largura):
                imagem[contadora_altura][contadora_largura][0] = 0
                imagem[contadora_altura][contadora_largura][1] = 0
                imagem[contadora_altura][contadora_largura][2] = 255
        contadora_altura = contadora_altura - 1
        if contadora_largura < largura:
            contadora_largura = contadora_largura + 1

cv2_imshow(imagem)
