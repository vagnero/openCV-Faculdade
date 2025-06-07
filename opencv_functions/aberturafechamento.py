import cv2
from tkinter import filedialog

def aplicar_abertura_fechamento():
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

    # Abertura: erosão seguida de dilatação
    abertura = cv2.morphologyEx(imagem, cv2.MORPH_OPEN, kernel)

    # Fechamento: dilatação seguida de erosão
    fechamento = cv2.morphologyEx(imagem, cv2.MORPH_CLOSE, kernel)

    # Mostrar todas as imagens
    cv2.imshow("Original", imagem)
    cv2.imshow("Abertura", abertura)
    cv2.imshow("Fechamento", fechamento)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
