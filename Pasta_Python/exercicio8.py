## Sequencia de exercicios sobre portas lógicas em redes neurais ##

import numpy as np
import matplotlib.pyplot as plt
import csv



x1_range = np.linspace(-40,40,200)
Ax1 = np.random.normal(22, 2, 300)
Ax2 = np.random.normal(6, 2, 300)



Bx1 = np.random.normal(6, 2, 300)
Bx2 = np.random.normal(6, 2, 300)



Cx1 = np.random.normal(14, 2, 300)
Cx2 = np.random.normal(14, 2, 300)



plt.plot(Ax1, Ax2,'ro',color = 'red')
plt.plot(Bx1, Bx2,'ro',color = 'blue')
plt.plot(Cx1, Cx2,'ro',color = 'green')
plt.xlabel('x1')



f = open('dataset.csv', 'w', newline='')

with f:

  writer = csv.writer(f)

  row = ["X1","X2","Saida"]

  writer.writerow( row )

  for index in range( 0, len( Ax1)):

    row = str(Ax1[index]), str( Ax2[index]),str(0) #A tera saida = 0 (Vermelho)

    writer.writerow( row )

  for index in range( 0, len( Bx1)):

    row = str(Bx1[index]), str(Bx2[index]),str(1) #B tera saida = 1 (Azul)

    writer.writerow( row )

  for index in range( 0, len( Cx1)):

    row = str(Cx1[index]), str(Cx2[index]),str(2) #C tera saida = 2 (Verde)

    writer.writerow( row )
    
    #############################
    
    #Logica da porta not em redes neurais 

import numpy as np

def calculo_z(lista_w, lista_x):
    tamanho = len(lista_w)
    z = 0
    for index in range( 0, tamanho):
         z= z+ lista_w[index]* lista_x[index]
    return z
    
def f_ativ_indetidade(z):
    return z

valor_A = int(input("entre com valor de A: ")) 

lista_w= [1,-1]
lista_x= [1, valor_A]
  
valor = calculo_z(lista_w,lista_x)
print(valor, end="\n")

################################

#Logica para porta E em redes neurais 

import numpy as np

def calculo_z(lista_w, lista_x):
  tamanho = len(lista_w)
  z= 0
  for index in range( 0, tamanho):
    z= z+ lista_w[index]* lista_x[index]
  return z

def funcao_degrau(z, thres):
   if (z > thres):
     return 1
   else:
     return 0

valor_A = int(input("entre com valor de A: "))
valor_B = int(input("entre com valor de B: "))

lista_w= [0, 1, 1]
lista_x= [1, valor_A, valor_B]

z= calculo_z(lista_w,lista_x)
valor = funcao_degrau(z, 1)
print(valor, end="\n")

#############################

#Logica para porta OU em redes neurais 

import numpy as np

def calculo_z(lista_w, lista_x):
  tamanho = len(lista_w)
  z= 0
  for index in range( 0, tamanho):
    z= z+ lista_w[index]* lista_x[index]
  return z

def funcao_degrau(z, thres):
   if (z > thres):
    return 1
   else:
    return 0

valor_A = int(input("entre com valor de A: "))
valor_B = int(input("entre com valor de B: "))

lista_w= [0, 1, 1]
lista_x= [1, valor_A, valor_B]
z= calculo_z(lista_w,lista_x)
valor = funcao_degrau(z, 0)
print(valor, end="\n")

#############################

#Criação de amostras A e B

import numpy as np
import matplotlib.pyplot as plt
import csv

Ax1 = np.random.normal(3, 5, 300)
Ax2 = np.random.normal(2, 3, 300)

Bx1 = np.random.normal(12, 4, 500)
Bx2 = np.random.normal(12, 3, 500)

plt.plot(Ax1, Ax2,'ro',color = 'red')
plt.plot(Bx1, Bx2,'ro',color = 'blue')
plt.xlabel('x1')
plt.ylabel('x2')

f = open('amostraA.csv', 'w', newline='')

with f:
   writer = csv.writer(f)
   for index in range( 0, len( Ax1)):
      row = str(Ax1[index]), str( Ax2[index])
      writer.writerow( row )
      f = open('amostraB.csv', 'w', newline='')

with f:
  writer = csv.writer(f)
  for index in range( 0, len( Bx1)) :
    row = str(Bx1[index]), str(Bx2[index])
    writer.writerow( row )
    
    ###########################
    
    #Determinação dos parâmetros a e b

import numpy as np
import matplotlib.pyplot as plt
import csv

x1_range = np.linspace(-40,40,200)
f = open('amostraB.csv', 'r')

with f:
      reader = csv.reader(f, delimiter=",")
      rowsA = len(list(reader))
f = open('amostraA.csv', 'r')
with f:
      reader = csv.reader(f, delimiter=",")
      Ax1 = np.zeros(rowsA)
      Ax2 = np.zeros(rowsA)
      cont = 0

      for row in reader: 
          Ax1[cont] = row[0]
          Ax2[cont] = row[1]
          cont = cont + 1

f = open('amostraB.csv', 'r')
with f:
    reader = csv.reader(f, delimiter=",")
    rowsB = len(list(reader))
f = open('amostraB.csv', 'r')
with f:
    reader = csv.reader(f, delimiter=",")
    Bx1 = np.zeros(rowsB)
    Bx2 = np.zeros(rowsB)
    cont = 0
    
    for row in reader: 
      Bx1[cont] = row[0]
      Bx2[cont] = row[1]
      cont = cont + 1
      plt.plot(Ax1, Ax2,'ro',color = 'red')
      plt.plot(Bx1, Bx2,'ro',color = 'blue')
      plt.xlabel('x1')
      plt.ylabel('x2')

a= -1.0
a_delta = 0.001
erro_min = 28
while (a< 1.0):
    b = -14.9
    b_delta = 0.001
    while (b < 15.1):
      contErrA = 0
      for index in range(0, len(Ax1)):
          if (Ax2[index] < (Ax1[index]*a + b) ):
              contErrA = contErrA + 1
              contErrB = 0
      for index in range(0, len(Bx1)):
          if (Bx2[index] > (Bx1[index]*a + b) ):
              contErrB = contErrB + 1
      err_Total = contErrA + contErrB
      if ( err_Total < erro_min ):
           plt.plot(x1_range, a*x1_range + b, '-g')
      erro_min = err_Total
    b = b + b_delta
a = a + a_delta
print(a, " ",b," ", contErrA," ",contErrB," ",err_Total ,end="\n")
print ("Fim\n")

##########################
# Criar um triangulo, circulo e quadrado  #

import cv2
from google.colab.patches import cv2_imshow
import numpy as np
import random

altura = 100
largura = 100
tamanho = altura * largura
img = np.zeros([altura,largura,3])

for py in range(0,altura):
  for px in range(0, largura):
    img[px][py][0] = 255 # cor azul
    img[px][py][1] = 255 # cor verde
    img[px][py][2] = 255 # cor vermelho

x0 = 0
y0 = 0
x1 = 0

y1 = altura
x2 = largura
y2 = int (altura/2)

pts = np.array([[x0,y0],[x1,y1],[x2,y2]])
cv2.fillPoly(img, [pts],(0,0,0))

cv2_imshow(img)

x_centro = int (largura /2)
y_centro = int (altura /2)
raio = int (altura /2)

img = np.zeros([altura,largura,3])

for py in range(0,altura):
  for px in range(0, largura):
    img[px][py][0] = 255 # cor azul
    img[px][py][1] = 255 # cor verde
    img[px][py][2] = 255 # cor vermelho

cv2.circle(img, (x_centro, y_centro), raio ,(0,0,0), -1)
cv2_imshow(img)

img = np.zeros([altura,largura,3])

cv2_imshow(img)

data = img.reshape(-1)



