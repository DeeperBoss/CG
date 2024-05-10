from OpenGL.GLUT import *

class Estado:
    def __init__(self):
        self.rosto_atual = 'rosto1'
        self.olho_atual = 'olhos1'
        self.cabelo_atual = 'cabelo1'
        self.sombrancelha_atual = 'sombrancelha1'
        self.nariz_atual = 'nariz1'
        self.boca_atual = 'boca1'  # Adicionado

estado = Estado()

def tecladoFunc(key, x, y):
    key = key.decode('utf-8')
    if key == '1':
        estado.olho_atual = 'olhos1'
    elif key == '2':
        estado.olho_atual = 'olhos2'
    elif key == '3':
        estado.olho_atual = 'olhos3'
    elif key == '4':
        estado.olho_atual = 'olhos4'
    elif key == '5':
        estado.olho_atual = 'olhos5'
    elif key == '6':
        estado.olho_atual = 'olhos6'
    elif key == 'a':
        estado.sombrancelha_atual = 'sombrancelha1'
    elif key == 's':
        estado.sombrancelha_atual = 'sombrancelha2'
    elif key == 'd':
        estado.sombrancelha_atual = 'sombrancelha3'
    elif key == 'f':
        estado.sombrancelha_atual = 'sombrancelha4'
    elif key == 'g':
        estado.sombrancelha_atual = 'sombrancelha5'
    elif key == 'h':
        estado.sombrancelha_atual = 'sombrancelha6'
    elif key == 'z':
        estado.nariz_atual = 'nariz1'
    elif key == 'x':
        estado.nariz_atual = 'nariz2'
    elif key == 'c':
        estado.nariz_atual = 'nariz3'
    elif key == 'v':
        estado.nariz_atual = 'nariz4'
    elif key == 'b':
        estado.nariz_atual = 'nariz5'
    elif key == 'n':
        estado.nariz_atual = 'nariz6'
    elif key == 'q':
        estado.boca_atual = 'boca1'  # Adicionado
    elif key == 'w':
        estado.boca_atual = 'boca2'  # Adicionado
    elif key == 'e':
        estado.boca_atual = 'boca3'  # Adicionado
    elif key == 'r':
        estado.boca_atual = 'boca4'  # Adicionado
    elif key == 't':
        estado.boca_atual = 'boca5'  # Adicionado
    elif key == 'y':
        estado.boca_atual = 'boca6'  # Adicionado
    glutPostRedisplay()

def tecladoFuncEspecial(key, x, y):
    if key == GLUT_KEY_F1:
        estado.rosto_atual = 'rosto1'
    elif key == GLUT_KEY_F2:
        estado.rosto_atual = 'rosto2'
    elif key == GLUT_KEY_F3:
        estado.rosto_atual = 'rosto3'
    elif key == GLUT_KEY_F4:
        estado.rosto_atual = 'rosto4'
    elif key == GLUT_KEY_F5:
        estado.rosto_atual = 'rosto5'
    elif key == GLUT_KEY_F6:
        estado.rosto_atual = 'rosto6'
    elif key == GLUT_KEY_F7:
        estado.cabelo_atual = 'cabelo1'
    elif key == GLUT_KEY_F8:
        estado.cabelo_atual = 'cabelo2'
    elif key == GLUT_KEY_F9:
        estado.cabelo_atual = 'cabelo3'
    elif key == GLUT_KEY_F10:
        estado.cabelo_atual = 'cabelo4'
    elif key == GLUT_KEY_F11:
        estado.cabelo_atual = 'cabelo5'
    elif key == GLUT_KEY_F12:
        estado.cabelo_atual = 'cabelo6'
    glutPostRedisplay()