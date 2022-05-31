from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys, os

import numpy as np
from sqlalchemy import null
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'utils'))
from colors import colors


WIDTH = 1200
HEIGHT = 600
TIME = 0
X_AXE = 0
Y_AXE = 0
WINDOW = 0
WINDOW_ANGLE = 0
WINDOW_STATE = 'opening'
X = []

DB = 10
TL2 = 54
STATIC_VERTEXES = [
  #TORRE LATERAL 1
        #1 retangulo 1 esquerdo
        0., 20., 2., #0    
        5., 20., 2., #1 
        5., 0., 2., #2 
        0., 0., 2., #3
        0., 20., 0., #4 
        5., 20., 0., #5 
        5., 0., 0., #6
        0., 0., 0., #7 
        #2retangulo 2 direito
        0. + DB, 20., 2., #8    
        5.+ DB, 20., 2., #9 
        5.+ DB, 0., 2., #10
        0.+ DB, 0., 2., #11
        0.+ DB, 20., 0., #12 
        5.+ DB, 20., 0., #13 
        5.+ DB, 0., 0., #14
        0.+ DB, 0., 0., #15 
        #3 retangulo 3 meio baixo
        0. + DB/2, 5., 2., #8    
        5.+ DB/2, 5., 2., #9 
        5.+ DB/2, 0., 2., #10
        0.+ DB/2, 0., 2., #11
        0.+ DB/2, 5., 0., #12 
        5.+ DB/2, 5., 0., #13 
        5.+ DB/2, 0., 0., #14
        0.+ DB/2, 0., 0., #15
        #4 retangulo 4 meio alto
        0. + DB/2, 10.+DB, 2., #8    
        5.+ DB/2, 10.+DB, 2., #9 
        5.+ DB/2, 2.+DB, 2., #10
        0.+ DB/2, 2.+DB, 2., #11
        0.+ DB/2, 10.+DB, 0., #12 
        5.+ DB/2, 10.+DB, 0., #13 
        5.+ DB/2, 2.+DB, 0., #14
        0.+ DB/2, 2.+DB, 0., #15 
        #5 retangulo 5 entrada direita
        0.+ DB, 20., 4., #8    
        13.+ DB, 20., 4., #9 
        13.+ DB, 0., 4., #10
        0.+ DB, 0., 4., #11
        0.+ DB, 20., 2., #12 
        13.+ DB, 20., 2., #13 
        13.+ DB, 0., 2., #14
        0.+ DB, 0., 2., #15 
        #6 retangulo meio baixo
        20., 5., 4., #8    
        54., 5., 4., #9 
        54., 0., 4., #30
        20., 0., 4., #11
        20., 5., -5., #12 
        54., 5., -5., #13 
        54., 0., -5., #14
        20., 0., -5., #15
        #7 retangulo base escada
        20.,1., -5., #8    
        54.,1., -5., #9 
        54., 0., -5., #30
        20., 0., -5., #11
        20.,1., -10., #12 
        54.,1., -10., #13 
        54., 0., -10., #14
        20., 0., -10., #15
        #8 retangulo escada 2
        20.,2, -5., #8    
        54.,2, -5., #9 
        54., 1., -5., #30
        20., 1., -5., #11
        20.,2, -9., #12 
        54.,2, -9., #13 
        54., 1., -9., #14
        20., 1., -9., #15
        #9 retangulo escada 3
        20., 3, -5., #8    
        54., 3, -5., #9 
        54., 2., -5., #30
        20., 2., -5., #11
        20., 3, -8., #12 
        54., 3, -8., #13 
        54., 2., -8., #14
        20., 2., -8., #15
        #10 retangulo escada 4
        20., 4, -5., #8    
        54., 4, -5., #9 
        54., 3., -5., #30
        20., 3., -5., #11
        20., 4, -7., #12 
        54., 4, -7., #13 
        54., 3., -7., #14
        20., 3., -7., #15
        #11 retangulo escada 5
        20., 5, -5., #8    
        54., 5, -5., #9 
        54., 4., -5., #30
        20., 4., -5., #11
        20., 5, -6., #12 
        54., 5, -6., #13 
        54., 4., -6., #14
        20., 4., -6., #15
        #12 retangulo 5 meio alto ----------------------------
        20., 20., 4., #8    
        54., 20., 4., #9 
        54., 15., 4., #30
        20., 15., 4., #11
        20., 20., -5., #12 
        54., 20., -5., #13 
        54., 15., -5., #14
        20., 15., -5., #15
        #13 retangulo 5 meio alto fino
        20., 20., 4., #8    
        54., 20., 4., #9 
        54., 12., 4., #30
        20., 12., 4., #11
        20., 20., 2., #12 
        54., 20., 2., #13 
        54., 12., 2., #14
        20., 12., 2., #15
        #14 retangulo meio entre portas 1
        28. , 12., 2., #8    
        33, 12., 2., #9 
        33, 5., 2., #10
        28, 5., 2., #11
        28, 12., 0., #12 
        33, 12., 0., #13 
        33, 5., 0., #14
        28, 5., 0., #15
        #15 retangulo meio entre portas 2
        38. , 12., 2., #8    
        43, 12., 2., #9 
        43, 5., 2., #10
        38, 5., 2., #11
        38, 12., 0., #12 
        43, 12., 0., #13 
        43, 5., 0., #14
        38, 5., 0., #15
        #16 retangulo meio entre portas 3
        48. , 12., 2., #8    
        54, 12., 2., #9 
        54, 5., 2., #10
        48, 5., 2., #11
        48, 12., 0., #12 
        54, 12., 0., #13 
        54, 5., 0., #14
        48, 5., 0., #15
        #17 retangulo pilar 1
        20. , 15., -4., #8    
        22, 15., -4., #9 
        22, 5., -4., #10
        20, 5., -4., #11
        20, 15., -2, #12 
        22, 15., -2, #13 
        22, 5., -2, #14
        20, 5., -2, #15
        #18 retangulo pilar 2
        30.5 , 15., -4., #8    
        32.5, 15., -4., #9 
        32.5, 5., -4., #10
        30.5, 5., -4., #11
        30.5, 15., -2, #12 
        32.5, 15., -2, #13 
        32.5, 5., -2, #14
        30.5, 5., -2, #15
        #19 retangulo pilar 3
        41. , 15., -4., #8    
        43, 15., -4., #9 
        43, 5., -4., #10
        41, 5., -4., #11
        41, 15., -2, #12 
        43, 15., -2, #13 
        43, 5., -2, #14
        41, 5., -2, #15
        #20 retangulo pilar 4
        52. , 15., -4., #8    
        54, 15., -4., #9 
        54, 5., -4., #10
        52, 5., -4., #11
        52, 15., -2, #12 
        54, 15., -2, #13 
        54, 5., -2, #14
        52, 5., -2, #15

    #TORRE LATERAL 2
        #21 retangulo entrada esquerda
        0.+ TL2, 20., 4., #8    
        8.+ TL2, 20., 4., #9 
        8.+ TL2, 0., 4., #10
        0.+ TL2, 0., 4., #11
        0.+ TL2, 20., 2., #12 
        8.+ TL2, 20., 2., #13 
        8.+ TL2, 0., 2., #14
        0.+ TL2, 0., 2., #15 
        #22 retangulo 1 esquerda 
        8.+TL2, 20., 2., #0    
        13.+TL2, 20., 2., #1 
        13.+TL2, 0., 2., #2 
        8.+TL2, 0., 2., #3
        8.+TL2, 20., 0., #4 
        13.+TL2, 20., 0., #5 
        13.+TL2, 0., 0., #6
        8.+TL2, 0., 0., #7 
        #23 retangulo 2 direita
        8.+TL2+ DB, 20., 2., #8    
        13.+TL2+ DB, 20., 2., #9 
        13.+TL2+ DB, 0., 2., #10
        8.+TL2+ DB, 0., 2., #11
        8.+TL2+ DB, 20., 0., #12 
        13.+TL2+ DB, 20., 0., #13 
        13.+TL2+ DB, 0., 0., #14
        8.+TL2+ DB, 0., 0., #15 
        #24 retangulo 3 base
        8.+TL2 + DB/2, 5., 2., #8    
        13.+TL2+ DB/2, 5., 2., #9 
        13.+TL2+ DB/2, 0., 2., #10
        8.+TL2+ DB/2, 0., 2., #11
        8.+TL2+ DB/2, 5., 0., #12 
        13.+TL2+ DB/2, 5., 0., #13 
        13.+TL2+ DB/2, 0., 0., #14
        8.+TL2+ DB/2, 0., 0., #15
        #25 retangulo 4 topo
        8.+TL2 + DB/2, 10.+DB, 2., #8    
        13.+TL2+ DB/2, 10.+DB, 2., #9 
        13.+TL2+ DB/2, 2.+DB, 2., #10
        8.+TL2+ DB/2, 2.+DB, 2., #11
        8.+TL2+ DB/2, 10.+DB, 0., #12 
        13.+TL2+ DB/2, 10.+DB, 0., #13 
        13.+TL2+ DB/2, 2.+DB, 0., #14
        8.+TL2+ DB/2, 2.+DB, 0., #15 
        #26 retangulo chão
        0, 5, 50., #8    
        77., 5, 50., #9 
        77., 0, 50., #10
        0, 0, 50., #11
        0, 5, 0., #12 
        77., 5, 0., #77 
        77., 0, 0., #14
        0, 0, 0., #15 
        #27 parede esquerda
        0, 20, 50., #8    
        5., 20, 50., #9 
        5., 5, 50., #10
        0, 5, 50., #11
        0, 20, 0., #12 
        5., 20, 0., #5 
        5., 5, 0., #14
        0, 5, 0., #15
        #28 parede esquerda
       70, 20, 50., #8    
        75, 20, 50., #9 
        75, 5, 50., #10
       70, 5, 50., #11
       70, 20, 0., #12 
        75, 20, 0., #5 
        75, 5, 0., #14
       70, 5, 0., #15 
       #26 retangulo teto
        0, 20, 50., #8    
        77., 20, 50., #9 
        77., 18, 50., #10
        0, 18, 50., #11
        0, 20, 0., #12 
        77., 20, 0., #77 
        77., 18, 0., #14
        0, 18, 0., #15 
        #26 parede fundo teto
        0, 20, 50., #8    
        77., 20, 50., #9 
        77.,0, 50., #10
        0,0, 50., #11
        0, 20, 45., #12 
        77., 20, 45., #77 
        77.,0, 45., #14
        0,0, 45., #15 
        #topo piramide
        36, 25,-5
]
STATIC_VERTEXES_COLORS = [
[ 'gray', '', 'gray', 'gray', 'gray', ''],#1
[ 'gray', '', 'gray', 'gray', 'gray', ''],
[ 'gray', '', 'gray', 'gray', 'gray', ''],
[ 'gray', '', 'gray', 'gray', 'gray', ''],
[ 'gray', '', 'gray', 'gray', 'gray', ''],
[ 'gray', '', 'gray', 'gray', 'gray', ''],
[ 'gray', '', 'gray', 'gray', 'gray', ''],
[ 'gray', '', 'gray', 'gray', 'gray', ''],
[ 'gray', '', 'gray', 'gray', 'gray', ''],
[ 'gray', '', 'gray', 'gray', 'gray', ''],#10
[ 'gray', '', 'gray', 'gray', 'gray', ''],
[ 'gray', '', 'gray', 'gray', 'gray', ''],
[ 'gray', '', 'gray', 'gray', 'gray', ''],
[ 'gray', '', 'gray', 'gray', 'gray', ''],
[ 'gray', '', 'gray', 'gray', 'gray', ''],
[ 'gray', '', 'gray', 'gray', 'gray', ''],
[ 'gray', '', 'gray', 'gray', 'gray', ''],
[ 'gray', '', 'gray', 'gray', 'gray', ''],
[ 'gray', '', 'gray', 'gray', 'gray', ''],
[ 'gray', '', 'gray', 'gray', 'gray', ''],#20
[ 'gray', '', 'gray', 'gray', 'gray', ''],
[ 'gray', '', 'gray', 'gray', 'gray', ''],
[ 'gray', '', 'gray', 'gray', 'gray', ''],
[ 'gray', '', 'gray', 'gray', 'gray', ''],
[ 'gray', '', 'gray', 'gray', 'gray', ''],
[ 'gray', '', 'gray', 'gray', 'gray', ''],
[ 'gray', 'gray', 'gray', 'gray', 'gray', 'gray'],
[ 'gray', '', 'gray', 'gray', 'gray', ''],
[ 'gray', '', 'gray', 'gray', 'gray', ''],
[ 'gray', '', 'gray', 'gray', 'gray', ''],#30
[ 'gray', '', 'gray', 'gray', 'gray', ''],
[ 'gray', '', 'gray', 'gray', 'gray', ''],
[ 'gray', '', 'gray', 'gray', 'gray', ''],
[ 'gray', '', 'gray', 'gray', 'gray', ''],]

STATIC_RECTAGLES = int((len(STATIC_VERTEXES))/(24) )
STATIC_VERTEXES = np.array(STATIC_VERTEXES, dtype=np.float32)

PYRAMID_VERTEXES_VALUE = 8 * 11
PF = [0 + PYRAMID_VERTEXES_VALUE ,1 + PYRAMID_VERTEXES_VALUE,int((len(STATIC_VERTEXES))/(24) )*8]
PL = [4+ PYRAMID_VERTEXES_VALUE,0+ PYRAMID_VERTEXES_VALUE,int((len(STATIC_VERTEXES))/(24) )*8]
PR = [1+ PYRAMID_VERTEXES_VALUE,5+ PYRAMID_VERTEXES_VALUE,int((len(STATIC_VERTEXES))/(24) )*8]
PB = [5+ PYRAMID_VERTEXES_VALUE,4+ PYRAMID_VERTEXES_VALUE,int((len(STATIC_VERTEXES))/(24) )*8]

for i in range(STATIC_RECTAGLES):
  X.append(i*8)

CF = []
for i in range(STATIC_RECTAGLES):
  CF.append([0 + X[i] ,3+ X[i] ,2 + X[i] , 1+ X[i] ])

CBK = []
for i in range(STATIC_RECTAGLES):
  CBK.append([4 + X[i],5 + X[i],6 + X[i],7 + X[i]])

CL = []
for i in range(STATIC_RECTAGLES):
  CL.append([0 + X[i],4 + X[i],7 + X[i],3 + X[i]])

CR = []
for i in range(STATIC_RECTAGLES):
  CR.append([1 + X[i],2 + X[i],6 + X[i],5 + X[i]])

CBM = []
for i in range(STATIC_RECTAGLES):
  CBM.append([2 + X[i],3 + X[i],7 + X[i],6 + X[i]])

CT = []
for i in range(STATIC_RECTAGLES):
  CT.append([0 + X[i],1 + X[i],5 + X[i],4 + X[i]])


DINAMIC_VERTEXES=[
  #janela gira pra direita
        5, 12, 0.5,    
        7.5, 12, 0.5, 
        7.5, 5, 0.5, 
        5 , 5, 0.5, 
        5 , 12, 0.,  
        7.5, 12, 0.,  
        7.5, 5, 0., 
        5 , 5, 0.,
    #janela gira pra esquerda
      7.5, 12, 0.5,    
       10, 12, 0.5, 
       10, 5, 0.5, 
      7.5 , 5, 0.5, 
      7.5 , 12, 0.,  
       10, 12, 0.,  
       10, 5, 0., 
      7.5 , 5, 0.,
    # porta
      20, 12, 0.5,    
       28, 12, 0.5, 
       28, 5, 0.5, 
      20 , 5, 0.5, 
      20 , 12, 0.,  
       28, 12, 0.,  
       28, 5, 0., 
      20 , 5, 0.,  
]
DINAMIC_RECTANGLES = int(len(DINAMIC_VERTEXES)/(24))
DINAMIC_VERTEXES = np.array(DINAMIC_VERTEXES, dtype=np.float32)
def init():
    bg_color = 'black'
    glClearColor(colors[bg_color]
                 [0], colors[bg_color]
                 [1], colors[bg_color]
                 [2], colors[bg_color]
                 [3])  # cor de fundo
    glOrtho (1, -1, -1, 1, -1 , 1)


def reshape(w, h):
    WIDTH = w
    HEIGHT = h
    glViewport(0, 0, WIDTH, HEIGHT)
    gluPerspective(10, WIDTH / HEIGHT, 0, 10)
    gluLookAt (0, 10, -300, #posição
               30, 10, 0, # ponto de foco
               0, 1, 0) # ângulo?

def drawRectagle(f, r, l, bk, bm, t, colorl):
    sc1 = 'gray' if colorl[0] == null or colorl[0] == '' else colorl[0]
    glColor4f (colors[sc1]
                 [0], colors[sc1]
                 [1], colors[sc1]
                 [2], colors[sc1]
                 [3])
    glDrawElements(GL_POLYGON, 4, GL_UNSIGNED_BYTE, f)

    sc2 = 'gray' if colorl[1] == null or colorl[1] == '' else colorl[1]
    glColor4f (colors[sc2]
                 [0], colors[sc2]
                 [1], colors[sc2]
                 [2], colors[sc2]
                 [3])
    glDrawElements(GL_POLYGON, 4, GL_UNSIGNED_BYTE, r)

    sc3 = 'gray' if colorl[2] == null or colorl[2] == '' else colorl[2]
    glColor4f (colors[sc3]
                 [0], colors[sc3]
                 [1], colors[sc3]
                 [2], colors[sc3]
                 [3])
    glDrawElements(GL_POLYGON, 4, GL_UNSIGNED_BYTE, l)

    sc4 = 'gray' if colorl[3] == null or colorl[3] == '' else colorl[3]
    glColor4f(colors[sc4]
                 [0], colors[sc4]
                 [1], colors[sc4]
                 [2], colors[sc4]
                 [3])
    glDrawElements(GL_POLYGON, 4, GL_UNSIGNED_BYTE, bk)

    sc5 = 'gray' if colorl[4] == null or colorl[4] == '' else colorl[4] 
    glColor4f(colors[sc5]
                 [0], colors[sc5]
                 [1], colors[sc5]
                 [2], colors[sc5]
                 [3])
    glDrawElements(GL_POLYGON, 4, GL_UNSIGNED_BYTE, bm)

    sc6 = 'gray' if colorl[5] == null or colorl[5] == '' else colorl[5]
    glColor4f(colors[sc6]
                 [0], colors[sc6]
                 [1], colors[sc6]
                 [2], colors[sc6]
                 [3])
    glDrawElements(GL_POLYGON, 4, GL_UNSIGNED_BYTE, t)

def drawStaticFront():
  glEnableClientState(GL_VERTEX_ARRAY)
  glVertexPointer(3, GL_FLOAT, 0, STATIC_VERTEXES)

  for i in range (STATIC_RECTAGLES):
    drawRectagle(CF[i], CR[i], CL[i], CBK[i],CBM[i], CT[i], STATIC_VERTEXES_COLORS[i])

  pc1 = 'gray'
  glColor4f(colors[pc1]
                 [0], colors[pc1]
                 [1], colors[pc1]
                 [2], colors[pc1]
                 [3])
  glDrawElements(GL_TRIANGLES, 3, GL_UNSIGNED_BYTE, PF)

  pc2 = 'gray'
  glColor4f(colors[pc2]
                 [0], colors[pc2]
                 [1], colors[pc2]
                 [2], colors[pc2]
                 [3])
  glDrawElements(GL_TRIANGLES, 3, GL_UNSIGNED_BYTE, PB)

  pc2 = 'gray'
  glColor4f(colors[pc2]
                 [0], colors[pc2]
                 [1], colors[pc2]
                 [2], colors[pc2]
                 [3])
  glDrawElements(GL_TRIANGLES, 3, GL_UNSIGNED_BYTE, PL)

  pc2 = 'gray'
  glColor4f(colors[pc2]
                 [0], colors[pc2]
                 [1], colors[pc2]
                 [2], colors[pc2]
                 [3])
  glDrawElements(GL_TRIANGLES, 3, GL_UNSIGNED_BYTE, PR)

  glDisableClientState(GL_VERTEX_ARRAY)

def drawDinamicParts():
  glPushMatrix()
  glVertexPointer(3, GL_FLOAT, 0, DINAMIC_VERTEXES)
  glTranslatef(5,5,0.0)
  glRotatef (WINDOW_ANGLE, 0.0, 1.0, 0.0)
  glTranslatef(-5,-5,0.0)
  glEnableClientState(GL_VERTEX_ARRAY)
  drawRectagle(CF[0], CR[0], CL[0], CBK[0],CBM[0], CT[0], ['red','red','red','red','red','red'])
  glDisableClientState(GL_VERTEX_ARRAY)
  glPopMatrix()

  glPushMatrix()
  glVertexPointer(3, GL_FLOAT, 0, DINAMIC_VERTEXES)
  glTranslatef(10,5,0.0)
  glRotatef (WINDOW_ANGLE, 0.0, -1.0, 0.0)
  glTranslatef(-10,-5,0.0)
  glEnableClientState(GL_VERTEX_ARRAY)
  drawRectagle(CF[1], CR[1], CL[1], CBK[1],CBM[1], CT[1], ['red','red','red','red','red','red'])
  glDisableClientState(GL_VERTEX_ARRAY)
  glPopMatrix()

  glPushMatrix()
  glVertexPointer(3, GL_FLOAT, 0, DINAMIC_VERTEXES)
  glTranslatef(20,5,0.0)
  glRotatef (WINDOW_ANGLE, 0.0, 1.0, 0.0)
  glTranslatef(-20,-5,0.0)
  glEnableClientState(GL_VERTEX_ARRAY)
  drawRectagle(CF[2], CR[2], CL[2], CBK[2],CBM[2], CT[2], ['red','red','red','red','red','red'])
  glDisableClientState(GL_VERTEX_ARRAY)
  glPopMatrix()

def display():
    glPushMatrix()
    glEnable(GL_DEPTH_TEST)
    glTranslatef(45,5,0.0)
    glRotatef (Y_AXE, 0.0, 1.0, 0.0)
    glRotatef (X_AXE, 1.0, 0.0, 0.0)
    glTranslatef(-45,-5,0.0)
    glClearDepth(1.0)
    glDepthMask(GL_TRUE)
    glDepthFunc(GL_LEQUAL)
    glDepthRange(0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    drawStaticFront()
    drawDinamicParts()
    glPopMatrix()
    glutSwapBuffers()

def keyboard(key, x, y):
  global Y_AXE, X_AXE, WINDOW, WINDOW_ANGLE, WINDOW_STATE
  # fachada, abrir e fechar janela, visão dos 5 objetos, porta
  if key == b'1':
    if WINDOW_STATE == 'opening':
      if WINDOW_ANGLE < 90:
        WINDOW_ANGLE += 1
      else:
        WINDOW_STATE = 'closing'
    else:
      if WINDOW_ANGLE > 0:
        WINDOW_ANGLE -= 1
      else:
        WINDOW_STATE = 'opening'

    WINDOW = WINDOW + 5
    glutPostRedisplay()
  if key == b'd' or key == b'D':
    Y_AXE = Y_AXE + 5
    glutPostRedisplay()
  elif key == b'a' or key == b'A':
    Y_AXE = Y_AXE - 5
    glutPostRedisplay()
  elif key == b'w' or key == b'W':
    X_AXE = X_AXE + 5
    glutPostRedisplay()
  elif key == b's' or key == b'S':
    X_AXE = X_AXE - 5
    glutPostRedisplay()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)#GLUT_SINGLE
    glutInitWindowSize(WIDTH, HEIGHT)
    glutInitWindowPosition(100, 50)
    glutCreateWindow(b"House | DaniloVFreire")
    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutReshapeFunc(reshape)
    glutMainLoop()

main()