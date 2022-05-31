from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys, os

import numpy as np
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'utils'))
from colors import colors


WIDTH = 500
HEIGHT = 500
TIME = 0
X_AXE = 0
Y_AXE = 0

CF = [3,2,1,0]
CBK = [4,5,6,7]
CL = [0,4,7,3]
CR = [1,2,6,5]
CBM = [2,3,7,6]

PF = [0,1,8]
PL = [4,0,8]
PR = [1,5,8]
PB = [5,4,8]

vertices = np.array([
        -3., 3., 3., #0
        3., 3., 3., #1 
        3., -3., 3., #2 
        -3., -3., 3., #3 
        -3., 3., -3., #4 
        3., 3., -3., #5 
        3., -3., -3., #6
        -3., -3., -3., #7 
        0., 6, 0., #8 
], dtype=np.float32)

def init():
    bg_color = 'black'
    glClearColor(colors[bg_color]
                 [0], colors[bg_color]
                 [1], colors[bg_color]
                 [2], colors[bg_color]
                 [3])  # cor de fundo
    glOrtho (1, -1, -1, 1, -1 , 1)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_CULL_FACE)


def reshape (w, h):
    WIDTH = w
    HEIGHT = h
    glViewport(0, 0, WIDTH, HEIGHT)
    gluPerspective(10, WIDTH / HEIGHT, 0, 3)
    gluLookAt (0, 0, -200, 0, 0, 0, 0, 1, 0)

def drawHouse():
    sc1 = 'blue'
    glColor4f (colors[sc1]
                 [0], colors[sc1]
                 [1], colors[sc1]
                 [2], colors[sc1]
                 [3])
    glDrawElements(GL_POLYGON, 4, GL_UNSIGNED_BYTE, CF)

    sc2 = 'yellow'
    glColor4f (colors[sc2]
                 [0], colors[sc2]
                 [1], colors[sc2]
                 [2], colors[sc2]
                 [3])
    glDrawElements(GL_POLYGON, 4, GL_UNSIGNED_BYTE, CL)

    sc3 = 'red'
    glColor4f(colors[sc3]
                 [0], colors[sc3]
                 [1], colors[sc3]
                 [2], colors[sc3]
                 [3])
    glDrawElements(GL_POLYGON, 4, GL_UNSIGNED_BYTE, CBK)

    sc4 = 'green'
    glColor4f(colors[sc4]
                 [0], colors[sc4]
                 [1], colors[sc4]
                 [2], colors[sc4]
                 [3])
    glDrawElements(GL_POLYGON, 4, GL_UNSIGNED_BYTE, CR)

    sc4 = 'orange'
    glColor4f(colors[sc4]
                 [0], colors[sc4]
                 [1], colors[sc4]
                 [2], colors[sc4]
                 [3])
    glDrawElements(GL_POLYGON, 4, GL_UNSIGNED_BYTE, CBM)

    pc1 = 'gray'
    glColor4f(colors[pc1]
                 [0], colors[pc1]
                 [1], colors[pc1]
                 [2], colors[pc1]
                 [3])
    glDrawElements(GL_TRIANGLES, 3, GL_UNSIGNED_BYTE, PF)

    pc2 = 'white'
    glColor4f(colors[pc2]
                 [0], colors[pc2]
                 [1], colors[pc2]
                 [2], colors[pc2]
                 [3])
    glDrawElements(GL_TRIANGLES, 3, GL_UNSIGNED_BYTE, PB)

    pc2 = 'cyan'
    glColor4f(colors[pc2]
                 [0], colors[pc2]
                 [1], colors[pc2]
                 [2], colors[pc2]
                 [3])
    glDrawElements(GL_TRIANGLES, 3, GL_UNSIGNED_BYTE, PL)

    pc2 = 'light_blue'
    glColor4f(colors[pc2]
                 [0], colors[pc2]
                 [1], colors[pc2]
                 [2], colors[pc2]
                 [3])
    glDrawElements(GL_TRIANGLES, 3, GL_UNSIGNED_BYTE, PR)

def display():
    glPushMatrix()
    glRotatef (Y_AXE, 0.0, 1.0, 0.0)
    glRotatef (X_AXE, 1.0, 0.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
    glEnableClientState(GL_VERTEX_ARRAY)
    glVertexPointer(3, GL_FLOAT, 0, vertices)

    drawHouse()

    glDisableClientState(GL_VERTEX_ARRAY)

    glPopMatrix()
    glutSwapBuffers()

def keyboard(key, x, y):
    global Y_AXE, X_AXE
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