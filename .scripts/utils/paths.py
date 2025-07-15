from pathlib import Path

from utils.images import verify_image

"""
    utilidades relacionadas à arquivos e diretórios
"""

ROOT = Path(".")
MAIN_README = Path("README.md")
SOURCES = Path("sources.json")

def get_wallpaper_dirs():
    """
        obter todos os diretórios do repositório que se parecem com diretórios de wallpapers
    """
    
    wallpaper_dirs = []
    
    for directory in ROOT.iterdir():
        # ignorar coisas que não são diretórios, ou que começam com sufixos irrelevantes (tipo .git)
        if not directory.is_dir() or directory.name.startswith((".", "__", "venv", "env")):
            continue
        
        wallpaper_dirs.append(directory)
    
    return wallpaper_dirs

def get_wallpaper_img_files():
    """
        obter todos os arquivos individuais dentro dos diretórios de wallpapers
    """

    img_files = []

    # pesquisar os itens dentro de cada diretório de wallpaper
    # e adicionar o item à tupla caso ele seja uma imagem
    for directory in get_wallpaper_dirs():
        for item in directory.iterdir():
            if not verify_image(item):
                continue

            img_files.append(item)
    
    return img_files