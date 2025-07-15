from pathlib import Path

from generate.main_readme import generate_main_readme
from generate.sub_readme import generate_sub_readme
from utils.paths import MAIN_README, get_wallpaper_dirs

"""
    função principal que de fato escreve os conteúdo gerados pelas outras funções nos readmes
"""

def main():
    # percorrer todos os diretórios de wallpaper e gerar um readme pra cada um
    for wall_dir in get_wallpaper_dirs():
        # gerar os conteúdos e montar o path do readme dele
        contents = generate_sub_readme(wall_dir)
        readme = wall_dir / "README.md"

        # criar o arquivo e escrever os conteúdos nele
        with open(readme, "w", encoding="utf-8") as f:
            f.write(contents)
    
    # gerar e escrever os contents no readme principal
    contents = generate_main_readme(
        instructions=f"""pro gowall, deve se criar um symlink ou cópia do `config.yml` em `~/.local/`  
    ex: `ln -s /mnt/seagate/workspace/coding/projects/repos/wallpapers/config.yml ~/.config/gowall/config.yml`"""
    )
    with open(MAIN_README, "w", encoding="utf-8") as f:
        f.write(contents)

main()