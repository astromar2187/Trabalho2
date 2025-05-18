import cv2
import matplotlib.pyplot as plt
import math
import os

def carregar_imagem(caminho):
    imagem = cv2.imread(caminho, cv2.IMREAD_GRAYSCALE)
    return imagem

def mostrar_imagem(imagem, titulo="Imagem"):
    plt.imshow(imagem, cmap='gray')
    plt.title(titulo)
    plt.axis('off')
    plt.show()

def comparar_imagens(imagem1, titulo1, imagem2, titulo2):
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    
    axs[0].imshow(imagem1, cmap='gray')
    axs[0].set_title(titulo1)
    axs[0].axis('off')
    
    axs[1].imshow(imagem2, cmap='gray')
    axs[1].set_title(titulo2)
    axs[1].axis('off')
    
    plt.tight_layout()
    plt.show()

def comparar_mult_imagens(imagens, rotulos):
    if len(imagens) != len(rotulos):
        print("O número de imagens e rótulos deve ser igual.")
        return

    N = len(imagens)
    cols = math.ceil(math.sqrt(N))
    rows = math.ceil(N / cols)

    fig, axs = plt.subplots(rows, cols, figsize=(4*cols, 4*rows))
    axs = axs.flatten()  # Facilita o acesso linear aos subplots

    for i in range(N):
        axs[i].imshow(imagens[i], cmap='gray')
        axs[i].set_title(rotulos[i])
        axs[i].axis('off')

    # Esconde subplots não usados
    for j in range(N, len(axs)):
        axs[j].axis('off')

    plt.tight_layout()
    plt.show()


def salvar_plot(plot, name, dir_path='output'):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    if not name.lower().endswith('.png'):
        name += '.png'
    caminho = os.path.join(dir_path, name)
    plot.savefig(caminho, bbox_inches='tight')
    print(f"Plot salvo em: {caminho}")



