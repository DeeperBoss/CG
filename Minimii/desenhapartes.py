import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
from faces import faces

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
from faces import faces

# Listas para armazenar pontos, retas e círculos
pontos = []
retas = []
circulos = []
face_atual = 0

# Função para desenhar o fundo
def desenhaBackground():
    glColor3f(0.5, 0.5, 0.5)  # Define a cor
    glBegin(GL_POLYGON)  # Inicia a primitiva GL_POLYGON
    glVertex2f(200, 0)  # Define os vértices do polígono
    glVertex2f(200, 200)
    glVertex2f(300, 200)
    glVertex2f(300, 0)
    glEnd()  # Termina a primitiva

# Função para desenhar as faces
def desenhaFaces():
    global face_atual
    glColor3f(0.0, 0.0, 0.0)  # Define a cor
    glBegin(GL_POLYGON)  # Inicia a primitiva GL_POLYGON
    if face_atual in faces:
        for ponto in faces[face_atual]:
            glVertex2f(*ponto)  # Define os vértices do polígono
    glEnd()  # Termina a primitiva

# Função para desenhar os vértices
def desenhaVertices():
    glColor3f(1.0, 0.0, 0.0)  # Define a cor
    glPointSize(10.0)  # Define o tamanho do ponto
    glBegin(GL_POINTS)  # Inicia a primitiva GL_POINTS
    for ponto in pontos:
        glVertex2f(ponto[0], ponto[1])  # Define a posição do ponto
    glEnd()  # Termina a primitiva

# Função para desenhar os polígonos
def desenhaPoligonos():
    if len(pontos) > 1:
        glColor3f(0.0, 0.0, 0.0)  # Define a cor
        glBegin(GL_LINE_LOOP)  # Inicia a primitiva GL_LINE_LOOP
        for ponto in pontos:
            glVertex2f(ponto[0], ponto[1])  # Define a posição do ponto
        glEnd()  # Termina a primitiva

# Função para desenhar as retas
def desenhaRetas():
    glColor3f(1.0, 0.0, 0.0)  # Define a cor
    for reta in retas:
        glBegin(GL_LINES)  # Inicia a primitiva GL_LINES
        glVertex2f(*reta[0])  # Define a posição do ponto inicial da reta
        glVertex2f(*reta[1])  # Define a posição do ponto final da reta
        glEnd()  # Termina a primitiva

# Função para desenhar um círculo
def desenhaCirculo(x, y, raio, cor):
    glColor3f(*cor)  # Define a cor
    glBegin(GL_POLYGON)  # Inicia a primitiva GL_POLYGON
    for i in range(100):
        theta = 2.0 * 3.1415926 * i / 100
        dx = raio * math.cos(theta)
        dy = raio * math.sin(theta)
        glVertex2f(x + dx, y + dy)  # Define os vértices do polígono
    glEnd()  # Termina a primitiva

# Função para desenhar os círculos
def desenhaCirculos():
    for x, y in circulos:
        desenhaCirculo(x, y, 50, (0.0, 1.0, 0.0))  

# Função para lidar com eventos do mouse
def mouseFunc(button, state, x, y):
    global pontos, retas, circulos
    x = x
    y = 500 - y
    if button == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:
            pontos.append((x, y))
            if len(pontos) > 1:
                retas.append([pontos[-2], pontos[-1]])
    elif button == GLUT_RIGHT_BUTTON:
        if state == GLUT_DOWN:
            circulos.append((x, y))
    glutPostRedisplay()

# Função para lidar com eventos do teclado
def keyboardFunc(key, x, y):
    global pontos, retas, desenho, face_atual
    if key == b'C' or key == b'c':
        if len(pontos) > 2:
            retas.append([pontos[-1], pontos[0]])
            glutPostRedisplay()
    elif key == b'S' or key == b's':
        desenho = [ponto for reta in retas for ponto in reta] + \
            circulos  # Incluído círculos
        print(desenho)
    elif key == b'Z' or key == b'z':
        if pontos:
            pontos.pop()
            if retas:
                retas.pop()
            glutPostRedisplay()
    elif key == b'F' or key == b'f':
        face_atual = (face_atual + 1) % len(faces)
        glutPostRedisplay()

# Função para lidar com eventos de movimento do mouse
def motionFunc(x, y):
    global retas
    x = x
    y = 500 - y
    if retas:
        retas[-1][1] = (x, y)
    glutPostRedisplay()

# Função para desenhar na tela
def drawFunc():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 0.0)
    desenhaFaces()
    desenhaCirculo(250, 300, 100, (0.0, 0.0, 1.0))  
    desenhaBackground()
    desenhaCirculos()
    glColor3f(1.0, 0.0, 0.0)
    if pontos:
        glPointSize(10.0)
        glBegin(GL_POINTS)
        glVertex2f(*pontos[0])
        glEnd()
        for i in range(1, len(pontos)):
            glBegin(GL_LINES)
            glVertex2f(*pontos[i-1])
            glVertex2f(*pontos[i])
            glEnd()
            glPointSize(10.0)
            glBegin(GL_POINTS)
            glVertex2f(*pontos[i])
            glEnd()
    glFlush()

# Inicialização do GLUT e criação da janela
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutCreateWindow("Desenha Poligonos")
glClearColor(1.0, 1.0, 1.0, 1.0)
glOrtho(0.0, 500.0, 0.0, 500.0, -1.0, 1.0)

desenho = []

# Definição das funções de callback
glutKeyboardFunc(keyboardFunc)
glutDisplayFunc(drawFunc)
glutMouseFunc(mouseFunc)
glutMotionFunc(motionFunc)

# Início do loop principal do GLUT
glutMainLoop()