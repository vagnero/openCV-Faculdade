import cv2
from tkinter import filedialog

def aplicar_subtracao():
    caminho1 = filedialog.askopenfilename(title="Escolha a primeira imagem",
                                          filetypes=[("Imagens", "*.png *.jpg *.jpeg *.bmp")])
    caminho2 = filedialog.askopenfilename(title="Escolha a segunda imagem",
                                          filetypes=[("Imagens", "*.png *.jpg *.jpeg *.bmp")])
    if not caminho1 or not caminho2:
        return

    img1 = cv2.imread(caminho1, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(caminho2, cv2.IMREAD_GRAYSCALE)

    if img1.shape != img2.shape:
        print("As imagens precisam ter o mesmo tamanho!")
        return

    resultado = cv2.absdiff(img1, img2)

    cv2.imshow("Imagem 1", img1)
    cv2.imshow("Imagem 2", img2)
    cv2.imshow("Subtração", resultado)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
