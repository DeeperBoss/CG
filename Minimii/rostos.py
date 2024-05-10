rostos = {
    'rosto1': [(174, 296), (201, 200), (299, 201), (313, 291), (299, 350), (191, 356)],
    'rosto2': [(185, 290), (166, 271), (160, 243), (163, 223), (170, 212), (184, 200), (200, 193), (219, 193), (237, 193), (268, 191), (293, 192), (313, 202), (321, 234), (322, 256), (323, 274), (333, 279), (341, 291), (343, 299), (342, 309), (339, 316), (331, 323), (327, 325), (321, 339), (312, 349), (302, 357), (286, 364), (269, 366), (252, 368), (236, 367), (220, 365), (211, 362), (199, 360), (192, 355), (190, 350), (186, 339), (184, 324)],
    'rosto3': [(202, 201), (234, 173), (255, 173), (299, 201), (313, 278), (298, 323), (227, 328), (205, 304)],
    'rosto4': [(189, 212), (209, 185), (243, 183), (291, 185), (308, 211), (318, 244), (320, 298), (292, 326), (214, 333), (191, 313), (185, 244)],
    'rosto5': [(150, 199), (341, 201), (347, 330), (160, 334)],
    'rosto6': [(169, 196), (250, 364), (330, 195)],
}
def normalizar_pontos(pontos, largura, altura):
    return [(x / largura * 2 - 1, y / altura * 2 - 1) for x, y in pontos]

for chave in rostos:
    rostos[chave] = normalizar_pontos(rostos[chave], 500, 500)