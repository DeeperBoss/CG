# nariz.py
narizes = {
    'nariz1': [(246, 289), (229, 257), (244, 247)],  # Forma 1 v 
    'nariz2': [(236, 249), (242, 258), (251, 261), (255, 252), (255, 249)],  # Forma 2 v
    'nariz3': [(242, 259), (236, 235), (245, 225), (250, 233)],  # Forma 3 v
    'nariz4': [(242, 265), (237, 264), (233, 260), (228, 256), (226, 250), (228, 246), (234, 247), (239, 248), (243, 248), (248, 248), (247, 255)],  # Forma 4 v
    'nariz5': [(238, 262), (234, 256), (225, 250), (203, 243), (195, 239), (194, 234), (200, 235), (207, 237), (215, 239), (222, 240), (231, 240), (240, 238), (244, 245)],  # Forma 5 v
    'nariz6': [(250, 250), (260, 240), (240, 240)],  # Forma 6
}

def normalizar_pontos(pontos, largura, altura):
    return [(x / largura * 2 - 1, y / altura * 2 - 1) for x, y in pontos]

for chave in narizes:
    narizes[chave] = normalizar_pontos(narizes[chave], 500, 500)