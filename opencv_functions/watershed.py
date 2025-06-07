import cv2
import numpy as np
from tkinter import filedialog

def aplicar_watershed():
    caminho = filedialog.askopenfilename(title="Escolha uma imagem",
                                         filetypes=[("Imagens", "*.jpg *.png *.bmp")])
    if not caminho:
        print("Nenhuma imagem selecionada.")
        return

    imagem = cv2.imread(caminho)
    imagem_original = cv2.imread(caminho)
    if imagem is None:
        print("Erro ao abrir a imagem.")
        return

    cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(cinza, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    kernel = np.ones((3,3), np.uint8)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
    sure_bg = cv2.dilate(opening, kernel, iterations=3)
    dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
    _, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg, sure_fg)

    _, markers = cv2.connectedComponents(sure_fg)
    markers += 1
    markers[unknown == 255] = 0

    cv2.watershed(imagem, markers)
    imagem[markers == -1] = [255, 0, 0]

    cv2.imshow("Original", imagem_original)
    cv2.imshow("Watershed", imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
