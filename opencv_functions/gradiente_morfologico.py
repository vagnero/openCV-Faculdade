import cv2
from tkinter import filedialog

def aplicar_gradiente_morfologico():
    caminho = filedialog.askopenfilename(title="Escolha uma imagem",
                                         filetypes=[("Imagens", "*.png *.jpg *.jpeg *.bmp")])
    if not caminho:
        print("Nenhuma imagem selecionada.")
        return

    imagem = cv2.imread(caminho, cv2.IMREAD_GRAYSCALE)
    if imagem is None:
        print("Erro ao abrir a imagem.")
        return

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    gradiente = cv2.morphologyEx(imagem, cv2.MORPH_GRADIENT, kernel)

    cv2.imshow("Original", imagem)
    cv2.imshow("Gradiente Morfológico", gradiente)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
