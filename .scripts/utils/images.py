from pathlib import Path
from PIL import Image

"""
    utilidades relacionadas à imagens (validação de arquivo, tamanho etc.)
"""

def verify_image(img_file):
    # verificar se o arquivo é uma imagem válida
    try:
        with Image.open(img_file) as img:
            img.verify()
        return True
    except Exception:
        return False

def get_img_size(img_file: Path):
    # obter as dimensões da imagem em uma tupla (largura, altura)
    with Image.open(img_file) as img:
        return img.size