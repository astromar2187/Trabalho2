from utils import *

PATH_ORIGINAL = 'img\\lena_gray.bmp'
PATH_RUIDO = 'img\\lena_ruido.bmp'

img_orig = carregar_imagem(PATH_ORIGINAL)
img_ruido = carregar_imagem(PATH_RUIDO)

comparar_imagens(img_orig, 'Imagem Original', img_ruido, 'Imagem com ruído')