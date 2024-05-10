import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import cos, sin

# Lista para armazenar os pontos dos círculos
pontos = []

# Lista para armazenar as cores dos círculos
cores = [(0.0, 0.1, 0.1), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0), (2.0, 1.0, 0.0), (1.0, 0.0, 1.0), (0.0, 1.0, 1.0)]

# Função para desenhar o background
def desenhaBackground():
    glColor3f(0.5, 0.5, 0.5)
    glBegin(GL_POLYGON)
    glVertex2f(200, 0)
    glVertex2f(200, 200)
    glVertex2f(300, 200)
    glVertex2f(300, 0)
    glEnd()

# Função para desenhar os círculos
def desenhaCirculos():
    for i, ponto in enumerate(pontos):
        glColor3f(*cores[i % len(cores)])
        glBegin(GL_POLYGON)
        for j in range(100):
            theta = 2.0 * 3.1415926 * j / 100
            dx = 10 * cos(theta)
            dy = 10 * sin(theta)
            glVertex2f(ponto[0] + dx, ponto[1] + dy)
        glEnd()

# Função para lidar com eventos do mouse
def mouseFunc(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        x = x
        y = 500 - y
        pontos.append((x, y))
        glutPostRedisplay()

# Função para lidar com eventos do teclado
def keyboardFunc(key, x, y):
    if key == b's':
        print(pontos)

# Função para desenhar na tela
def drawFunc():
    glClear(GL_COLOR_BUFFER_BIT)
    desenhaBackground()
    desenhaCirculos()
    glFlush()

# Configurações iniciais
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutCreateWindow("Desenha Olhos")
glClearColor(1.0, 1.0, 1.0, 1.0)
glOrtho(0.0, 500.0, 0.0, 500.0, -1.0, 1.0)

# Configura as funções de desenho, mouse e teclado
glutDisplayFunc(drawFunc)
glutMouseFunc(mouseFunc)
glutKeyboardFunc(keyboardFunc)  # Adicione esta linha

# Inicia o loop principal
glutMainLoop()