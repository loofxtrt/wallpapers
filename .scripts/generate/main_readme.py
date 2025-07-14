from pathlib import Path

from utils.paths import get_wallpaper_dirs

"""
    gera o readme principal do repo/índice de todas as outras pastas
"""

def generate_summary():
    contents = ""

    # obter todas as pastas de wallpapers nesse repo
    for wall_dir in get_wallpaper_dirs():
        # montar o caminho do arquivo do readme dentro desse diretório de wallpapers
        # se o arquivo existir, adicionar o hyperlink dele no contents
        md_path = wall_dir / "README.md"
        if md_path.is_file():
            contents += f"![{wall_dir.name}](./{wall_dir.name}/README.md)  \n"
        
    return contents

def generate_grid():
    pass

def generate_main_readme():
    summary = generate_summary()
    contents = summary

    return contents