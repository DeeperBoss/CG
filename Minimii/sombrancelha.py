from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from olhos import olhos  # Importa o módulo olhos
from teclas import estado  # Importa a instância estado do módulo teclas

# Dicionário para mapear cada tipo de sombrancelha para uma cor
cores_sombrancelhas = {
    'sombrancelha1': (0.0, 0.0, 0.0),  # Preto
    'sombrancelha2': (0.5, 0.0, 0.0),  # Marrom
    'sombrancelha3': (0.75, 0.75, 0.75),  # Cinza
    'sombrancelha4': (1.0, 1.0, 0.0),  # Amarelo
    'sombrancelha5': (0.0, 0.0, 1.0),  # Azul
    'sombrancelha6': (1.0, 0.0, 0.0),  # Vermelho
}

# Dicionário para mapear cada tipo de sombrancelha para uma forma
# Dicionário para mapear cada tipo de sombrancelha para uma forma
formas_sombrancelhas = {
    'sombrancelha1': [(0.0, 0.1), (0.05, 0.1), (0.05, 0.08), (0.0, 0.08)],  # Forma 1
    'sombrancelha2': [(0.0, 0.1), (0.06, 0.11), (0.06, 0.09), (0.0, 0.08)],  # Forma 2 - Inclinada para cima
    'sombrancelha3': [(0.0, 0.1), (0.04, 0.09), (0.04, 0.07), (0.0, 0.08)],  # Forma 3 - Inclinada para baixo
    'sombrancelha4': [(0.0, 0.1), (0.05, 0.12), (0.05, 0.10), (0.0, 0.08)],  # Forma 4 - Mais alta
    'sombrancelha5': [(0.0, 0.1), (0.05, 0.08), (0.05, 0.06), (0.0, 0.08)],  # Forma 5 - Mais baixa
    'sombrancelha6': [(0.0, 0.1), (0.07, 0.1), (0.07, 0.08), (0.0, 0.08)],  # Forma 6 - Mais larga
}

# Função para desenhar as sombrancelhas
def desenhaSombrancelhas():
    glColor3f(*cores_sombrancelhas[estado.sombrancelha_atual])  # Usa a variável sombrancelha_atual
    for ponto in olhos[estado.olho_atual]:  # Usa a posição dos olhos para determinar a posição das sombrancelhas
        glBegin(GL_POLYGON)
        for forma in formas_sombrancelhas[estado.sombrancelha_atual]:  # Usa a variável sombrancelha_atual
            glVertex2f(ponto[0] + forma[0], ponto[1] + forma[1])  # Desenha a sombrancelha
        glEnd()