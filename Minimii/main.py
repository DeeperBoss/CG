from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from olhos import olhos
from cabelos import cabelos
from nariz import narizes
from bocas import bocas
from math import cos, sin, pi
from faces import faces
from cores import cores_cabelo, cores_olho, cores_nariz,  cores_boca, cores_face, cores_sombrancelha
from sombrancelhas import sombrancelhas 
import random
from OpenGL.GLUT import GLUT_BITMAP_HELVETICA_10



# Definindo as variáveis globais para os tipos de rosto, olho, nariz, cabelo, boca e sombrancelha
tipo_face = 0
tipo_olho = 0
tipo_nariz = 0
tipo_cabelo = 0
tipo_boca = 0
tipo_sombrancelha = 0

# Definindo as variáveis globais para os tipos de cores de cabelo, olho, nariz, boca, face e sombrancelha
tipo_cor_cabelo = 0
tipo_cor_olho = 0
tipo_cor_olho2 = 0
tipo_cor_nariz = 0
tipo_cor_boca = 0
tipo_cor_face = 0
tipo_cor_sombrancelha = 0

# Função para desenhar texto na tela
def desenhaTexto(texto, x, y):
    glColor3f(0, 0, 0)  # cor do texto
    glRasterPos2f(x, y)
    for ch in texto:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_10, ctypes.c_int(ord(ch)))

# Função para normalizar os pontos para que eles se ajustem à tela
def normalizar_pontos(pontos, largura, altura):
    if isinstance(pontos, dict):
        centro = pontos['centro']
        raio = pontos['raio']
        centro_normalizado = (
            centro[0] / largura * 2 - 1, centro[1] / altura * 2 - 1)
        raio_normalizado = raio / largura * 2
        return {'centro': centro_normalizado, 'raio': raio_normalizado}
    else:
        if isinstance(pontos[0], float):
            return [(pontos[0] / largura * 2 - 1, pontos[1] / altura * 2 - 1)]
        else:
            return [(x / largura * 2 - 1, y / altura * 2 - 1) for x, y in pontos]

# Função para reduzir os pontos de uma forma
def reduzir_pontos(pontos, fator):
    centro = (sum(x for x, y in pontos) / len(pontos),
              sum(y for x, y in pontos) / len(pontos))
    return [(centro[0] + (x - centro[0]) * fator, centro[1] + (y - centro[1]) * fator) for x, y in pontos]


# Esta função é usada para desenhar uma forma na tela. 
# Ela recebe três argumentos: 
# a forma a ser desenhada, a cor da forma e um booleano que indica se a forma deve ter um contorno.
def desenhaForma(forma, cor, contorno=True):
    if isinstance(forma, dict):
        centro = forma['centro']
        raio = forma['raio']
        glColor3f(*cor)
        glBegin(GL_POLYGON)
        for i in range(100):
            theta = 2.0 * pi * i / 100
            dx = raio * cos(theta)
            dy = raio * sin(theta)
            glVertex2f(centro[0] + dx, centro[1] + dy)
        glEnd()
        if contorno:
            glColor3f(0, 0, 0)
            glBegin(GL_LINE_LOOP)
            for i in range(100):
                theta = 2.0 * pi * i / 100
                dx = raio * cos(theta)
                dy = raio * sin(theta)
                glVertex2f(centro[0] + dx, centro[1] + dy)
            glEnd()
    else:
        glColor3f(*cor)
        glBegin(GL_POLYGON)
        for ponto in forma:
            glVertex2f(*ponto)
        glEnd()
        if contorno:
            glColor3f(0, 0, 0)
            glBegin(GL_LINE_LOOP)
            for ponto in forma:
                glVertex2f(*ponto)
            glEnd()



# Esta função é usada para desenhar um rosto na tela. 
# Ela usa as variáveis globais definidas no início do código para determinar: o tipo e a cor de cada parte do rosto. 

def desenhaRosto():
    global tipo_face, tipo_olho, tipo_nariz, tipo_cabelo, tipo_boca, tipo_sombrancelha  
    global tipo_cor_cabelo, tipo_cor_olho, tipo_cor_nariz, tipo_cor_boca, tipo_cor_face, tipo_cor_sombrancelha  

    glClearColor(209/255, 189/255, 171/255, 1)  
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    face = list(faces.values())[tipo_face]
    desenhaForma(normalizar_pontos(reduzir_pontos(face, 0.95), 500, 500), cores_face[tipo_cor_face])  

    olho = list(olhos.values())[tipo_olho]
    olho_esquerdo = normalizar_pontos(olho, 500, 500)
    olho_direito = [(-x, y) for x, y in olho_esquerdo]
    desenhaForma(olho_esquerdo, cores_olho[tipo_cor_olho])
    desenhaForma(olho_direito, cores_olho[tipo_cor_olho])

    glColor3f(*cores_nariz[tipo_cor_nariz])
    nariz = list(narizes.values())[tipo_nariz]
    desenhaForma(normalizar_pontos(nariz, 500, 500),
                 cores_nariz[tipo_cor_nariz])

    glColor3f(*cores_cabelo[tipo_cor_cabelo])
    cabelo = list(cabelos.values())[tipo_cabelo]
    desenhaForma(normalizar_pontos(cabelo, 500, 500),
                 cores_cabelo[tipo_cor_cabelo], contorno=False)
    
    glColor3f(*cores_sombrancelha[tipo_cor_sombrancelha])  
    sombrancelha = list(sombrancelhas.values())[tipo_sombrancelha]  
    sombrancelha_esquerda = normalizar_pontos(sombrancelha, 500, 500)  
    sombrancelha_direita = [(-x, y) for x, y in sombrancelha_esquerda]  
    desenhaForma(sombrancelha_esquerda, cores_sombrancelha[tipo_cor_sombrancelha])  
    desenhaForma(sombrancelha_direita, cores_sombrancelha[tipo_cor_sombrancelha])  


    glColor3f(*cores_boca[tipo_cor_boca])
    boca = list(bocas.values())[tipo_boca]
    desenhaForma(normalizar_pontos(boca, 500, 500), cores_boca[tipo_cor_boca])
    desenhaTexto('Comandos:', -0.95, -0.95)
    desenhaTexto('Faces: F1...F6 (mudar cor: J)', -0.95, -0.90)
    desenhaTexto('Cabelos: F7...F12 (mudar cor: o)', -0.95, -0.85)
    desenhaTexto('Olhos: 1...6 (mudar cor: k)', -0.95, -0.80)
    desenhaTexto('Bocas: q, w, e, r, t, y (mudar cor: u)', -0.95, -0.75)
    desenhaTexto('Sombrancelhas: a, s, d, f, g, h (mudar cor: p)', -0.95, -0.70)
    desenhaTexto('Narizes: z, x, c, v, b, n (mudar cor: m)', -0.95, -0.65)
    desenhaTexto('Randomizar: -', -0.95, -0.60)

    glutSwapBuffers()


def tecladoFunc(key, x, y):
    global tipo_face, tipo_olho, tipo_nariz, tipo_cabelo, tipo_boca, tipo_sombrancelha
    global tipo_cor_cabelo, tipo_cor_olho, tipo_cor_nariz, tipo_cor_boca, tipo_cor_face, tipo_cor_sombrancelha

    key = key.decode('utf-8')

    # Dicionários para mapear teclas para tipos de partes do rosto
    teclas_olhos = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5}
    teclas_bocas = {'q': 0, 'w': 1, 'e': 2, 'r': 3, 't': 4, 'y': 5}
    teclas_sombrancelhas = {'a': 0, 's': 1, 'd': 2, 'f': 3, 'g': 4, 'h': 5}
    teclas_narizes = {'z': 0, 'x': 1, 'c': 2, 'v': 3, 'b': 4, 'n': 5}

    # Lógica para mudar os tipos de partes do rosto
    if key in teclas_olhos:
        tipo_olho = teclas_olhos[key]
    elif key in teclas_sombrancelhas:
        tipo_sombrancelha = teclas_sombrancelhas[key]
    elif key in teclas_narizes:
        tipo_nariz = teclas_narizes[key]
    elif key in teclas_bocas:
        tipo_boca = teclas_bocas[key]

    # Lógica para mudar as cores das partes do rosto
    elif key == 'o':
        tipo_cor_cabelo = (tipo_cor_cabelo + 1) % len(cores_cabelo)
    elif key == 'p':
        tipo_cor_sombrancelha = (tipo_cor_sombrancelha + 1) % len(cores_sombrancelha)
    elif key == 'k':
        tipo_cor_olho = (tipo_cor_olho + 1) % len(cores_olho)
    elif key == 'm':
        tipo_cor_nariz = (tipo_cor_nariz + 1) % len(cores_nariz)
    elif key == 'u':
        tipo_cor_boca = (tipo_cor_boca + 1) % len(cores_boca)
    elif key == 'j':
        tipo_cor_face = (tipo_cor_face + 1) % len(cores_face)

    # Lógica para randomizar as partes e as cores do rosto
    elif key == '-':  
        tipo_face = random.randint(0, len(faces) - 1)
        tipo_olho = random.randint(0, len(olhos) - 1)
        tipo_sombrancelha = random.randint(0, len(sombrancelhas) - 1)
        tipo_nariz = random.randint(0, len(narizes) - 1)
        tipo_cabelo = random.randint(0, len(cabelos) - 1)
        tipo_boca = random.randint(0, len(bocas) - 1)
        tipo_cor_cabelo = random.randint(0, len(cores_cabelo) - 1)
        tipo_cor_sombrancelha = random.randint(0, len(cores_sombrancelha) - 1)
        tipo_cor_olho = random.randint(0, len(cores_olho) - 1)
        tipo_cor_nariz = random.randint(0, len(cores_nariz) - 1)
        tipo_cor_boca = random.randint(0, len(cores_boca) - 1)
        tipo_cor_face = random.randint(0, len(cores_face) - 1)

    glutPostRedisplay()

def tecladoEspecialFunc(key, x, y):
    global tipo_face, tipo_cabelo

    # Dicionários para mapear teclas para tipos de partes do rosto
    teclas_faces = {GLUT_KEY_F1: 0, GLUT_KEY_F2: 1, GLUT_KEY_F3: 2, GLUT_KEY_F4: 3, GLUT_KEY_F5: 4, GLUT_KEY_F6: 5}
    teclas_cabelos = {GLUT_KEY_F7: 0, GLUT_KEY_F8: 1, GLUT_KEY_F9: 2, GLUT_KEY_F10: 3, GLUT_KEY_F11: 4, GLUT_KEY_F12: 5}

    # Lógica para mudar os tipos de partes do rosto
    if key in teclas_faces:
        tipo_face = teclas_faces[key]
    elif key in teclas_cabelos:
        tipo_cabelo = teclas_cabelos[key]

    glutPostRedisplay()

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(100, 100)
glutCreateWindow("Minimii")
glutDisplayFunc(desenhaRosto)
glutKeyboardFunc(tecladoFunc)
glutSpecialFunc(tecladoEspecialFunc)
glutMainLoop()