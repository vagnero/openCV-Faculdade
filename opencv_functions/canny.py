import cv2
from tkinter import filedialog

def aplicar_canny():
    caminho = filedialog.askopenfilename(title="Escolha uma imagem",
                                         filetypes=[("Imagens", "*.png *.jpg *.jpeg *.bmp")])
    if not caminho:
        print("Nenhuma imagem selecionada.")
        return

    imagem = cv2.imread(caminho, cv2.IMREAD_GRAYSCALE)
    bordas = cv2.Canny(imagem, 100, 200)

    cv2.imshow("Original", imagem)
    cv2.imshow("Canny", bordas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
