import cv2
from tkinter import filedialog

def aplicar_sobel():
    caminho = filedialog.askopenfilename(title="Escolha uma imagem",
                                         filetypes=[("Imagens", "*.png *.jpg *.jpeg *.bmp")])
    if not caminho:
        print("Nenhuma imagem selecionada.")
        return

    imagem = cv2.imread(caminho, cv2.IMREAD_GRAYSCALE)
    if imagem is None:
        print("Erro ao abrir a imagem.")
        return

    sobelx = cv2.Sobel(imagem, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(imagem, cv2.CV_64F, 0, 1, ksize=5)
    sobel = cv2.magnitude(sobelx, sobely)

    cv2.imshow("Original", imagem)
    cv2.imshow("Sobel", sobel.astype('uint8'))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
