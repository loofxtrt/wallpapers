from pathlib import Path

from gen_main_readme import generate_main_readme
from gen_sub_readme import generate_sub_readme

def main():
    # percorrer todos os diretórios no root (projeto atual) e gerar um readme pra cada um
    for wallpaper_dir in Path(".").iterdir():
        if wallpaper_dir.is_dir():
            generate_sub_readme(wallpaper_dir)
    
    # gerar e escrever os contents no readme principal
    contents = generate_main_readme()
    
    with open(Path("./README.md"), "w") as f:
        f.write(contents)

main()