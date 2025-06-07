import cv2
from tkinter import filedialog

def aplicar_media():
    caminho = filedialog.askopenfilename(title="Escolha uma imagem",
                                         filetypes=[("Imagens", "*.jpg *.png *.bmp")])
    if not caminho:
        return

    imagem = cv2.imread(caminho)
    filtrada = cv2.blur(imagem, (5, 5))

    cv2.imshow("Original", imagem)
    cv2.imshow("Filtro Média", filtrada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
