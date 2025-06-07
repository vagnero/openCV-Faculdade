from .erosao import aplicar_erosao
from .dilatacao import aplicar_dilatacao
from .aberturafechamento import aplicar_abertura_fechamento
from .gradiente_morfologico import aplicar_gradiente_morfologico
from .top_hat import aplicar_top_hat
from .sobel import aplicar_sobel
from .canny import aplicar_canny
from .watershed import aplicar_watershed
from .media import aplicar_media
from .mediana import aplicar_mediana
from .subtracao import aplicar_subtracao
from .linear_stretch_gui import aplicar_linear_stretch
from .equalizacao import aplicar_equalizacao
from .splitting_histogram import aplicar_splitting
from .binarizacao_gui import aplicar_binarizacao

# continue com os outros...

# Assim, tudo que for "importado de opencv_functions" já inclui essas funções
__all__ = [
    "aplicar_erosao",
    "aplicar_dilatacao",
    "aplicar_abertura_fechamento",
    "aplicar_gradiente_morfologico",
    "aplicar_top_hat",
    "aplicar_sobel",
    "aplicar_canny",
    "aplicar_watershed",
    "aplicar_subtracao",
    "aplicar_mediana",
    "aplicar_media",
    "aplicar_equalizacao",
    "aplicar_linear_stretch",
    "aplicar_splitting",
    "aplicar_binarizacao",
    # ...
]
