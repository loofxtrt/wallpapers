from pathlib import Path

ROOT = Path(".")
MAIN_README = Path("README.md")
SOURCES = Path("sources.json")

def get_wallpaper_dirs():
    wallpaper_dirs = []
    
    for directory in ROOT.iterdir():
        # ignorar coisas que não são diretórios, ou que começam com sufixos irrelevantes (tipo .git)
        if not directory.is_dir() or directory.name.startswith(".") or directory.name.startswith("__"):
            continue
        
        wallpaper_dirs.append(directory)
    
    return wallpaper_dirs