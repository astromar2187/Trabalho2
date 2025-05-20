import cv2
import numpy as np

def mediana(imagem, tamanho_kernel):
    imagem_filtrada = cv2.medianBlur(imagem, tamanho_kernel)
    return imagem_filtrada

def aplicar_mascara(imagem_cinza, mascara):
    return cv2.filter2D(src=imagem_cinza, ddepth=-1, kernel=mascara)

