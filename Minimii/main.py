from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from rostos import rostos
from olhos import olhos  # Importa o módulo olhos
from cabelos import cabelos  # Importa o módulo cabelos
from sombrancelha import desenhaSombrancelhas  # Importa a função desenhaSombrancelhas do módulo sombrancelha
from nariz import narizes
from bocas import bocas  # Importa o módulo bocas
from math import cos, sin, pi
from teclas import tecladoFunc, tecladoFuncEspecial, estado  # Importa as funções e a instância estado do módulo teclas

# Dicionário para mapear cada tipo de olho para uma cor
cores_olhos = {
    'olhos1': (1.0, 0.0, 0.0),  # Vermelho
    'olhos2': (0.0, 1.0, 0.0),  # Verde
    'olhos3': (0.0, 0.0, 1.0),  # Azul
    'olhos4': (1.0, 1.0, 0.0),  # Amarelo
    'olhos5': (0.0, 1.0, 1.0),  # Ciano
    'olhos6': (1.0, 0.0, 1.0),  # Magenta
}

# Dicionário para mapear cada tipo de cabelo para uma cor
cores_cabelos = {
    'cabelo1': (0.5, 0.0, 0.0),  # Marrom
    'cabelo2': (0.0, 0.5, 0.0),  # Verde escuro
    'cabelo3': (0.0, 0.0, 0.5),  # Azul escuro
    'cabelo4': (0.5, 0.5, 0.0),  # Amarelo escuro
    'cabelo5': (0.0, 0.5, 0.5),  # Ciano escuro
    'cabelo6': (0.5, 0.0, 0.5),  # Magenta escuro
}

# Dicionário para mapear cada tipo de nariz para uma cor
cores_narizes = {
    'nariz1': (1.0, 0.5, 0.0),  # Laranja
    'nariz2': (0.5, 1.0, 0.0),  # Verde claro
    'nariz3': (0.0, 0.5, 1.0),  # Azul claro
    'nariz4': (1.0, 1.0, 0.5),  # Amarelo claro
    'nariz5': (0.5, 1.0, 1.0),  # Ciano claro
    'nariz6': (1.0, 0.5, 1.0),  # Magenta claro
}

# Dicionário para mapear cada tipo de boca para uma cor
cores_bocas = {
    'boca1': (1.0, 0.0, 0.0),  # Vermelho
    'boca2': (0.0, 1.0, 0.0),  # Verde
    'boca3': (0.0, 0.0, 1.0),  # Azul
    'boca4': (1.0, 1.0, 0.0),  # Amarelo
    'boca5': (0.0, 1.0, 1.0),  # Ciano
    'boca6': (1.0, 0.0, 1.0),  # Magenta
}

# Função para normalizar os pontos
def normalizar_pontos(pontos, largura, altura):
    return [(x / largura * 2 - 1, y / altura * 2 - 1) for x, y in pontos]

# Função para desenhar o background
def desenhaBackground():
    glColor3f(0.5, 0.5, 0.5)  # Define a cor para cinza
    glBegin(GL_POLYGON)
    for ponto in normalizar_pontos([(200, 0), (200, 200), (300, 200), (300, 0)], 500, 500):
        glVertex2f(*ponto)
    glEnd()

# Função para desenhar o nariz selecionado
def desenhaNariz():
    glColor3f(*cores_narizes[estado.nariz_atual])  # Usa a variável nariz_atual
    glBegin(GL_POLYGON)
    for ponto in narizes[estado.nariz_atual]:  # Usa a variável nariz_atual
        glVertex2f(*ponto)
    glEnd()

# Função para desenhar a boca selecionada
def desenhaBoca():
    glColor3f(*cores_bocas[estado.boca_atual])  # Usa a variável boca_atual
    glBegin(GL_POLYGON)
    for ponto in bocas[estado.boca_atual]:  # Usa a variável boca_atual
        glVertex2f(*ponto)
    glEnd()

# Função para desenhar texto na tela
def desenhaTexto(x, y, texto):
    glRasterPos2f(x, y)
    for char in texto:
        glutBitmapCharacter(GLUT_BITMAP_9_BY_15, ord(char))

# Função para desenhar o rosto selecionado
def desenhaRosto():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    desenhaBackground()

    # Desenha o texto no canto superior da tela
    glColor3f(0.0, 0.0, 0.0)  # Define a cor para preto
    desenhaTexto(-0.9, 0.9, "Teclas:")
    desenhaTexto(-0.9, 0.85, "1-6      Olhos")
    desenhaTexto(-0.9, 0.8, "a-h      Sobrancelhas")
    desenhaTexto(-0.9, 0.75, "z-n      Nariz")
    desenhaTexto(-0.9, 0.7, "q-y      Boca")
    desenhaTexto(-0.9, 0.65, "F1-F6    Rosto")
    desenhaTexto(-0.9, 0.6, "F7-F12   Cabelo")

    # Desenha os olhos
    glColor3f(*cores_olhos[estado.olho_atual])  # Usa a variável olho_atual
    for ponto in olhos[estado.olho_atual]:
        glBegin(GL_POLYGON)
        for i in range(100):  # Desenha um círculo para cada olho
            theta = 2.0 * pi * i / 100
            dx = 0.05 * cos(theta)  # Aumenta o raio do círculo
            dy = 0.05 * sin(theta)  # Aumenta o raio do círculo
            glVertex2f(ponto[0] + dx, ponto[1] + dy)
        glEnd()

    # Desenha o nariz
    desenhaNariz()

    # Desenha a boca
    desenhaBoca()

    # Desenha as sombrancelhas
    desenhaSombrancelhas()  # Chama a função desenhaSombrancelhas

    # Desenha o cabelo
    glColor3f(*cores_cabelos[estado.cabelo_atual])  # Usa a variável cabelo_atual
    glBegin(GL_POLYGON)
    for ponto in cabelos[estado.cabelo_atual]:  # Usa a variável cabelo_atual
        glVertex2f(*ponto)
    glEnd()

    # Desenha o interior do rosto
    glColor3f(1.0, 1.0, 1.0)  # Define a cor para branco
    glBegin(GL_POLYGON)
    for ponto in rostos[estado.rosto_atual]:  # Usa a variável rosto_atual
        glVertex2f(*ponto)
    glEnd()

    # Desenha o contorno do rosto
    glColor3f(0.0, 0.0, 0.0)  # Define a cor para preto
    glLineWidth(10)  # Define a largura da linha para 10
    glBegin(GL_LINE_LOOP)
    for ponto in rostos[estado.rosto_atual]:  # Usa a variável rosto_atual
        glVertex2f(*ponto)
    glEnd()

    glutSwapBuffers()

# Configurações da janela
glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
window = glutCreateWindow(b"Rostos")

# Funções de callback
glutDisplayFunc(desenhaRosto)
glutIdleFunc(desenhaRosto)
glutKeyboardFunc(tecladoFunc)
glutSpecialFunc(tecladoFuncEspecial)  # Adiciona a função para as teclas de função

# Configurações do OpenGL
glEnable(GL_DEPTH_TEST)
glClearColor(1.0, 1.0, 1.0, 1.0)  # Define a cor de fundo para branco

# Inicia o loop principal
glutMainLoop()