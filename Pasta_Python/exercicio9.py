## Sequencia de exercicios sobre tratamento de imagens em Python ( redes neurais )## 

## 3.Faça um programa que copie uma parte de uma imagem, dado a posição inicial e a posição final da parte a ser copiada para um novo arquivo.
import cv2
import numpy as np
from matplotlib import pyplot as plt
from google.colab.patches import cv2_imshow

imagem = cv2.imread('pequena.jpg')

altura, largura, bytesPorPixel = np.shape(imagem)

print("altura:",altura,"largura:",largura,end ='\n')

x0 = 50
y0 = 50
x1 = 220
y1 = 200

img_altura = y1 - y0
img_largura = x1 - x0

img = np.zeros([img_altura,img_largura,3])

for py in range(0, img_altura):
        for px in range(0,img_largura):
            img[py][px][0] = imagem [py+y0][px+x0][0]
            img[py][px][1] = imagem [py+y0][px+x0][1]
            img[py][px][2] = imagem [py+y0][px+x0][2]
            
cv2_imshow( img)
cv2_imshow( imagem)

#####################

##1)Faça um programa que aplique o brilho e contraste em uma imagem, note a diferença na imagem e no histograma.

import cv2
import numpy as np
from matplotlib import pylab as plt
from google.colab.patches import cv2_imshow

#Função de contraste e brilho 
def contrasteBrilho(img, alpha, beta ):
        for y in range(img.shape[0]):
            for x in range(img.shape[1]):
                 for c in range(img.shape[2]):
                        img[y,x,c] = np.clip(alpha*img[y,x,c] + beta, 0, 255)
        return img
 
 ## Capta a imagem e faz leitura
img = cv2.imread("pequena.jpg")
original = cv2.imread("pequena.jpg")

# cria uma variavel e aplica a função
imagem_result = contrasteBrilho(img,2,0.1)

# Mostra a imagem criada e original
cv2_imshow(imagem_result )
cv2_imshow( original)
cv2.waitKey()

# relaciona o histograma com a imagem criada
plt.hist(imagem_result.ravel(), bins = 256, range = [0,250])
plt.ylabel('bins')
plt.xlabel('range')
plt.title("Histograma da Imagem Criada")
plt.show()

###################

## 2.Faça um programa que suavize uma imagem para o tipo:
## a)Por kernel
## b)blur
## c)gaussianBlur

## a)Por kernel

import cv2
import numpy as np
from matplotlib import pyplot as plt

imagem = cv2.imread("pequena.jpg")

#gray = cv2.cvtColor(imagem, cv2.COLOR_BAYER_BG2GRAY)
#cv2_imshow(gray)

altura, largura, bytesPorPixel = np.shape(imagem)

kernel = np.ones((5,5),np.float32)/25;
filter2D = cv2.filter2D(imagem,-1,kernel)
cv2_imshow(filter2D)
cv2.waitKey()

kernel = np.ones((9,9),np.float32)/81;
filter2D1 = cv2.filter2D(imagem,-1,kernel) 
cv2_imshow(filter2D1)
cv2.waitKey()


## b)blur

import cv2
import numpy as np
from matplotlib import pyplot as plt

imagem = cv2.imread("pequena.jpg")
cv2.waitKey()

altura, largura, bytesPorPixel = np.shape(imagem)

#gray = cv2.cvtColor(imagem, cv2.COLOR_BAYER_BG2GRAY)
#cv2_imshow(gray)

blur = cv2.blur(imagem,(3,3))
cv2_imshow(blur)
        
blur1 = cv2.blur(imagem,(5,5))
cv2_imshow(blur1)
           
blur2 = cv2.blur(imagem,(9,9))
cv2_imshow(blur2)



## c)gaussianBlur

import cv2
import numpy as np
from matplotlib import pyplot as plt

imagem = cv2.imread("pequena.jpg")
cv2.waitKey()

altura, largura, bytesPorPixel = np.shape(imagem)

gray = cv2.cvtColor(imagem, cv2.COLOR_BAYER_BG2GRAY)
#cv2_imshow(gray)

gaussianBlur = cv2.GaussianBlur(gray,(3,3),0) 
cv2_imshow(gaussianBlur)


gaussianBlur1 = cv2.GaussianBlur(gray,(9,9),0) 
cv2_imshow(gaussianBlur1)


#####################

