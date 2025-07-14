from pathlib import Path

"""
    gera o readme principal do repo/índice de todas as outras pastas
"""

def generate_main_readme():
    contents = ""

    # obter todas as pastas de wallpapers nesse repo
    for wall_dir in Path(".").iterdir():
        # ignorar coisas que não são diretórios, ou que começam com sufixos irrelevantes (tipo .git)
        if not wall_dir.is_dir() or wall_dir.name.startswith(".") or wall_dir.name.startswith("__"):
            continue
        
        # montar o caminho do arquivo do readme dentro desse diretório de wallpapers
        # se o arquivo existir, adicionar o hyperlink dele no contents
        md_path = wall_dir / "README.md"
        if md_path.is_file():
            contents += f"![{wall_dir.name}](./{wall_dir.name}/README.md)  \n"
        
    return contents