from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys, os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'utils'))
from colors import colors

WIDTH = 1360
HEIGHT = 720
TIME = 0

def init():
    bg_color = 'black'
    glClearColor(colors[bg_color]
                 [0], colors[bg_color]
                 [1], colors[bg_color]
                 [2], colors[bg_color]
                 [3])  # cor de fundo


def keyboard(key, x, y):
    global TIME
    if key == b'y' or key == b'Y':  # 'y'move the planets
        TIME = (TIME + 1)
        glutPostRedisplay()

def displayPlanets ():
    #sol
    planet_color1 = 'yellow'
    glPushMatrix()
    glColor4f(colors[planet_color1]
              [0], colors[planet_color1]
              [1], colors[planet_color1]
              [2], colors[planet_color1]
              [3])
    glRotatef ( 0.8 * TIME, 0, 1, 0) 
    glutWireSphere(0.6, 16, 16)
    glPopMatrix()
    
    #planeta com movimentação invertida
    planet_color2 = 'red'
    glPushMatrix()
    glColor4f(colors[planet_color2]
              [0], colors[planet_color2]
              [1], colors[planet_color2]
              [2], colors[planet_color2]
              [3])
    glRotatef ( -1.5 * TIME, 0, 1, 0) 
    glTranslatef (2.45, 0.1, 2)
    glutWireSphere(0.3, 16, 16)
    glPopMatrix()
    
    # planeta com luas
    planet_color3 = 'cyan'
    glPushMatrix()
    glColor4f(colors[planet_color3]
              [0], colors[planet_color3]
              [1], colors[planet_color3]
              [2], colors[planet_color3]
              [3])
    glRotatef (TIME, 0, 1.2, 0)
    glTranslatef(2, 0, 0)
    glPushMatrix()
    glutWireSphere(0.2, 16, 16)
    glPopMatrix()

    #lua 1
    moon_color1 = 'gray'
    glPushMatrix()
    glColor4f(colors[moon_color1]
              [0], colors[moon_color1]
              [1], colors[moon_color1]
              [2], colors[moon_color1]
              [3])
    glRotatef (1.7 * TIME, 0, 1, 0)
    glTranslatef(0.3, 0, 0)
    glutWireSphere(0.05, 16, 16)
    glPopMatrix()

    #lua 2
    moon_color2 = 'white'
    glPushMatrix()
    glColor4f(colors[moon_color2]
              [0], colors[moon_color2]
              [1], colors[moon_color2]
              [2], colors[moon_color2]
              [3])
    glRotatef (2.1 * TIME, 1, 1, 0)
    glTranslatef(0.3, 0, 0)
    glutWireSphere(0.03, 16, 16)
    glPopMatrix()
    glPopMatrix()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    displayPlanets()
    glutSwapBuffers()

def reshape(width, height):
    global WIDTH, HEIGHT
    WIDTH = width
    HEIGHT = height
    glViewport(0, 0, WIDTH, HEIGHT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    glMatrixMode(GL_PROJECTION)
    gluPerspective(80, WIDTH / HEIGHT, 0, 1)
    gluLookAt (0, 0, 5, 0, 0, 0, 0, 1, 0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Sistema solar | DaniloVFreire")
    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutReshapeFunc(reshape)
    glutMainLoop()

main()
