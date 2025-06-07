import tkinter as tk
from tkinter import ttk
from opencv_functions import *

class AppMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Menu de Processamento de Imagem")
        self.root.geometry("400x600")

        # Container principal com canvas + scrollbar
        container = tk.Frame(self.root)
        container.pack(fill="both", expand=True)

        self.canvas = tk.Canvas(container)
        scrollbar = tk.Scrollbar(container, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)

        # Atualiza o scrollregion e largura do frame rolável
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Faz o frame interno ocupar 100% da largura do canvas
        self.canvas.bind("<Configure>", self.resize_frame)

        # Criar o menu dentro do frame rolável
        self.create_menu()

    def resize_frame(self, event):
        canvas_width = event.width
        self.canvas.itemconfig("all", width=canvas_width)

    def create_menu(self):
        titulo = tk.Label(self.scrollable_frame, text="Menu Principal", font=("Arial", 16, "bold"))
        titulo.pack(pady=10, fill="x", expand=True)

        self.add_section("📋 Autores", [
            ("Exibir Autores", self.exibir_autores),
        ])

        self.add_section("🔬 Morfologia", [
            ("Erosão", self.erosao),
            ("Dilatação", self.dilatacao),
            ("Abertura/Fechamento", self.abertura_fechamento),
            ("Gradiente Morfológico", self.gradiente_morfologico),
            ("Top Hat", self.top_hat),
        ])

        self.add_section("⚡ Operadores de Borda", [
            ("Sobel", self.sobel),
            ("Canny", self.canny),
            ("Watershed", self.watershed_gui),
        ])

        self.add_section("🔧 Operações", [
            ("Subtração", self.subtracao),
            ("Filtro Mediana", self.mediana),
            ("Filtro Média", self.media),
        ])

        self.add_section("📈 Equalização", [
            ("Equalização", self.equalizar),
        ])

        self.add_section("⚙️ Realce e Binarização", [
            ("Stretch Linear", self.linear_stretch_gui),
            ("Splitting", self.splitting_histogram),
            ("Binarização", self.binarizacao_gui),
        ])

        autores = tk.Label(self.scrollable_frame, text="Autores: Aldo, Aline, Audrey, Jose, Vagner Wesley", font=("Arial", 8))
        autores.pack(pady=10, fill="x", expand=True)

    def add_section(self, title, buttons):
        frame = ttk.LabelFrame(self.scrollable_frame, text=title)
        frame.pack(fill="x", padx=10, pady=5, expand=True)

        for label, command in buttons:
            btn = ttk.Button(frame, text=label, command=command)
            btn.pack(fill="x", padx=5, pady=2, expand=True)

    # Funções chamadas pelos botões
    def erosao(self): aplicar_erosao()
    def dilatacao(self): aplicar_dilatacao()
    def abertura_fechamento(self): aplicar_abertura_fechamento()
    def gradiente_morfologico(self): aplicar_gradiente_morfologico()
    def top_hat(self): aplicar_top_hat()
    def sobel(self): aplicar_sobel()
    def canny(self): aplicar_canny()
    def watershed_gui(self): aplicar_watershed()
    def subtracao(self): aplicar_subtracao()
    def mediana(self): aplicar_mediana()
    def media(self): aplicar_media()
    def equalizar(self): aplicar_equalizacao()
    def linear_stretch_gui(self): aplicar_linear_stretch()
    def splitting_histogram(self): aplicar_splitting()
    def binarizacao_gui(self): aplicar_binarizacao()

    def exibir_autores(self):
        janela = tk.Toplevel(self.root)
        janela.title("Sobre o Projeto")
        janela.geometry("300x150")

        label = tk.Label(janela, text="Projeto de Processamento de Imagens\n\nAutores:", font=("Arial", 12, "bold"))
        label.pack(pady=10)

        nomes = "Aldo Rosa\nAline Almeida\nAudrey Bergamine\nJose Leandro\nVagner Matias\nWesley Paulo"
        label_nomes = tk.Label(janela, text=nomes, font=("Arial", 10))
        label_nomes.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = AppMenu(root)
    root.mainloop()
