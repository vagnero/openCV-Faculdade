import cv2
from tkinter import filedialog
import numpy as np

def aplicar_linear_stretch():
    caminho = filedialog.askopenfilename(title="Escolha uma imagem",
                                         filetypes=[("Imagens", "*.jpg *.png *.bmp")])
    if not caminho:
        return

    imagem = cv2.imread(caminho, cv2.IMREAD_GRAYSCALE)
    min_val = np.min(imagem)
    max_val = np.max(imagem)

    stretch = ((imagem - min_val) / (max_val - min_val) * 255).astype(np.uint8)

    cv2.imshow("Original", imagem)
    cv2.imshow("Stretch Linear", stretch)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
