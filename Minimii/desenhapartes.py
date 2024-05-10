import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Lista para armazenar os pontos dos polígonos
pontos = []

# Função para desenhar o background
def desenhaBackground():
    glColor3f(0.5, 0.5, 0.5)  # Define a cor para cinza
    glBegin(GL_POLYGON)
    glVertex2f(200, 0)  # Inferior esquerdo
    glVertex2f(200, 200)  # Superior esquerdo
    glVertex2f(300, 200)  # Superior direito
    glVertex2f(300, 0)  # Inferior direito
    glEnd()

# Função para desenhar os polígonos
def desenhaPoligonos():
    if len(pontos) > 2:
        glColor3f(0.5, 0.5, 0.5)  # Define a cor para cinza
        glBegin(GL_POLYGON)
        for ponto in pontos:
            glVertex2f(ponto[0], ponto[1])
        glEnd()

        glColor3f(0.0, 0.0, 0.0)  # Define a cor para preto
        glBegin(GL_LINE_LOOP)
        for ponto in pontos:
            glVertex2f(ponto[0], ponto[1])
        glEnd()

# Função para desenhar os vértices
def desenhaVertices():
    glColor3f(1.0, 0.0, 0.0)  # Define a cor para vermelho
    glPointSize(5.0)  # Define o tamanho do ponto
    glBegin(GL_POINTS)
    for ponto in pontos:
        glVertex2f(ponto[0], ponto[1])
    glEnd()

# Função para lidar com eventos do mouse
def mouseFunc(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        # Converte as coordenadas do mouse para as coordenadas do OpenGL
        x = x
        y = 500 - y
        # Adiciona o ponto clicado à lista de pontos
        pontos.append((x, y))
        # Redesenha a tela
        glutPostRedisplay()

# Função para desenhar na tela
def drawFunc():
    glClear(GL_COLOR_BUFFER_BIT)
    desenhaBackground()
    desenhaPoligonos()
    desenhaVertices()
    glFlush()

# Configurações iniciais
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutCreateWindow("Desenha Poligonos")
glClearColor(1.0, 1.0, 1.0, 1.0)
glOrtho(0.0, 500.0, 0.0, 500.0, -1.0, 1.0)

# Função para lidar com eventos do teclado
def keyboardFunc(key, x, y):
    if key == b'S' or key == b's':
        print(pontos)  # Imprime os pontos no terminal

# Configura a função de teclado
glutKeyboardFunc(keyboardFunc)

# Configura as funções de desenho e mouse
glutDisplayFunc(drawFunc)
glutMouseFunc(mouseFunc)

# Inicia o loop principal
glutMainLoop()