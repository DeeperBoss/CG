olhos = {
    'olhos1': [(209, 317), (287, 317)],
    'olhos2': [(225, 292), (260, 292)],
    'olhos3': [(209, 277), (282, 278), (282, 278), (282, 278), (282, 278)],
    'olhos4': [(212, 257), (212, 257), (212, 257), (212, 257), (212, 257), (212, 257), (290, 257), (290, 257), (290, 257), (290, 257), (290, 257), (290, 257), (290, 257), (290, 257), (290, 257), (290, 257), (290, 257), (290, 257), (290, 257), (290, 257), (290, 257)],
    'olhos5': [(249, 287), (248, 287)],
    'olhos6': [(211, 260), (242, 294), (272, 258)],
}

def normalizar_pontos(pontos, largura, altura):
    return [(x / largura * 2 - 1, y / altura * 2 - 1) for x, y in pontos]

for chave in olhos:
    olhos[chave] = normalizar_pontos(olhos[chave], 500, 500)