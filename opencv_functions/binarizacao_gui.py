import cv2
from tkinter import filedialog

def aplicar_binarizacao():
    caminho = filedialog.askopenfilename(title="Escolha uma imagem",
                                         filetypes=[("Imagens", "*.jpg *.png *.bmp")])
    if not caminho:
        return

    imagem = cv2.imread(caminho, cv2.IMREAD_GRAYSCALE)
    _, binaria = cv2.threshold(imagem, 127, 255, cv2.THRESH_BINARY)

    cv2.imshow("Original", imagem)
    cv2.imshow("Binarização", binaria)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
