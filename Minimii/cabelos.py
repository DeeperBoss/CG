# cabelos.py
cabelos = {
    'cabelo1': [(210, 329), (229, 292), (251, 330), (274, 295), (287, 336), (310, 298), (321, 328), (342, 324), (338, 361), (354, 396), (311, 396), (307, 432), (271, 408), (251, 448), (229, 409), (189, 431), (186, 392), (155, 378), (169, 350), (163, 309)],
    'cabelo2': [(219, 321), (188, 328), (171, 359), (165, 402), (169, 431), (175, 459), (194, 418), (214, 406), (218, 432), (228, 450), (236, 416), (255, 405), (268, 402), (264, 428), (271, 445), (281, 418), (295, 401), (307, 394), (320, 426), (340, 433), (349, 394), (345, 362), (356, 347), (345, 333), (340, 316), (337, 305), (332, 297), (300, 307)],
    'cabelo3': [(192, 331), (223, 302), (280, 299), (312, 328), (335, 361), (335, 397), (324, 432), (301, 390), (282, 401), (276, 444), (244, 391), (225, 432), (212, 381), (195, 420), (192, 374), (172, 415)],
    'cabelo4': [(236, 335), (191, 325), (156, 333), (135, 354), (123, 388), (142, 378), (160, 372), (180, 370), (206, 375), (177, 396), (166, 419), (172, 444), (182, 459), (196, 469), (196, 453), (200, 439), (212, 423), (224, 408), (240, 405), (252, 403), (268, 405), (293, 411), (310, 415), (325, 415), (333, 411), (346, 409), (351, 407), (359, 399), (368, 389), (363, 384), (366, 375), (372, 365), (371, 339), (368, 324), (363, 317), (352, 309), (346, 304), (339, 299), (335, 300), (335, 305), (335, 309), (333, 321), (324, 330), (304, 332), (282, 324), (272, 318), (267, 313), (260, 308)],
    'cabelo5': [(215, 347), (229, 336), (247, 327), (263, 320), (283, 317), (306, 317), (321, 328), (321, 341), (320, 359), (312, 374), (291, 384), (266, 390), (242, 388), (228, 377), (219, 366), (322, 343), (331, 362), (346, 367), (360, 361), (370, 355), (349, 361), (343, 352), (358, 346), (358, 340), (346, 335), (342, 340), (336, 347), (328, 346)],
    'cabelo6': [(239, 343), (237, 330), (236, 315), (230, 290), (227, 281), (218, 262), (207, 252), (191, 235), (178, 227), (171, 224), (156, 215), (144, 211), (133, 208), (139, 211), (141, 216), (150, 238), (157, 248), (161, 272), (166, 288), (171, 307), (178, 321), (189, 338), (199, 361), (214, 371), (230, 379), (246, 384), (265, 385), (277, 383), (292, 378), (299, 375), (308, 365), (308, 363), (313, 356), (315, 347), (317, 344), (318, 337), (318, 335), (315, 333), (305, 332), (292, 339), (289, 345), (310, 347), (317, 338), (320, 326), (321, 319), (321, 317), (313, 314), (302, 316), (292, 319), (290, 326), (290, 335), (285, 339), (274, 342), (262, 336), (258, 334), (255, 330), (253, 327), (251, 326), (251, 333), (259, 343), (255, 345), (234, 345)],
}

def normalizar_pontos(pontos, largura, altura):
    return [(x / largura * 2 - 1, y / altura * 2 - 1) for x, y in pontos]

for chave in cabelos:
    cabelos[chave] = normalizar_pontos(cabelos[chave], 500, 500)