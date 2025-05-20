from utils import *
from masks import *

PATH_ORIGINAL = 'img\\lena_gray.bmp'
PATH_RUIDO = 'img\\lena_ruido.bmp'

img_orig = carregar_imagem(PATH_ORIGINAL)
img_ruido = carregar_imagem(PATH_RUIDO)
img_mediana3 = mediana(img_ruido, 3)


def compara_mediana_mascara(imagem, mediana, mascara, nome_mascara):
    imagem_filtrada = aplicar_mascara(imagem, mascara)
    comparar_imagens(mediana, 'Filtro da mediana 3x3', imagem_filtrada, f'Imagem com mascara {nome_mascara}')

M1 = np.array([[0, 1/5, 0],
                [1/5, 1, 1/5],
                [0, 1/5, 0]])

M2 = np.array([[1/9, 1/9, 1/9],
                [1/9, 1/9, 1/9],
                [1/9, 1/9, 1/9]])

M3 = np.array([[1/32, 3/32, 1/32],
                [3/32, 16/32, 3/32],
                [1/32, 3/32, 1/32]])

M4 = np.array([[0, 1/8, 0],
                [1/8, 4/8, 1/8],
                [0, 1/8, 0]])


mascaraM1 = aplicar_mascara(img_ruido, M1)
mascaraM2 = aplicar_mascara(img_ruido, M2)
mascaraM3 = aplicar_mascara(img_ruido, M3)
mascaraM4 = aplicar_mascara(img_ruido, M4)

imagens = [img_ruido, img_mediana3, mascaraM1, mascaraM2, mascaraM3, mascaraM4]
nomes = ['Imagem com ruído', 'Filtro da mediana 3x3', 'Mascara M1', 'Mascara M2', 'Mascara M3', 'Mascara M4']
comparar_mult_imagens(imagens, nomes)
