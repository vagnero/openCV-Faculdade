import cv2
from tkinter import filedialog
import numpy as np

def aplicar_splitting():
    caminho = filedialog.askopenfilename(title="Escolha uma imagem",
                                         filetypes=[("Imagens", "*.jpg *.png *.bmp")])
    if not caminho:
        return

    imagem = cv2.imread(caminho, cv2.IMREAD_GRAYSCALE)
    _, thresh = cv2.threshold(imagem, 128, 255, cv2.THRESH_BINARY)

    cv2.imshow("Original", imagem)
    cv2.imshow("Splitting (Limiar 128)", thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
