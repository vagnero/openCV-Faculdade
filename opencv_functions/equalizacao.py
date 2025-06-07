import cv2
from tkinter import filedialog

def aplicar_equalizacao():
    caminho = filedialog.askopenfilename(title="Escolha uma imagem",
                                         filetypes=[("Imagens", "*.jpg *.png *.bmp")])
    if not caminho:
        return

    imagem = cv2.imread(caminho, cv2.IMREAD_GRAYSCALE)
    equalizada = cv2.equalizeHist(imagem)

    cv2.imshow("Original", imagem)
    cv2.imshow("Equalizada", equalizada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
