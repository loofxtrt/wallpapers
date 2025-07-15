from pathlib import Path

from utils.paths import get_wallpaper_dirs
from utils.images import verify_image

"""
    gera o readme principal do repo/índice de todas as outras pastas
"""

def generate_summary():
    contents = ""

    # pra cada diretório de wallpapers, gerar um hyperlink
    # que leva direto pro readme daquele diretório em específico
    for wall_dir in get_wallpaper_dirs():
        # montar o caminho do arquivo do readme dentro desse diretório de wallpapers
        # se o arquivo existir, adicionar o hyperlink dele no contents
        md_path = wall_dir / "README.md"
        if md_path.is_file():
            contents += f"""
<p align="center">
    <a href="./{wall_dir.name}/README.md">
        <img src="./{wall_dir.name}" alt="{wall_dir.name}">
    </a>
</p>
            """
        
    return contents

def generate_html_row(image_row: tuple[Path]):
    start = '<p align="center">\n'
    row_contents = ""
    end = '</p>\n'

    # gerar um row de imagens pra cada imagem dentro da tupla, envolvendo esse row num paragráfo
    for img_path in image_row:
        row_contents += f'  <img src="{img_path}" width="30%"/>\n'
    
    return start + row_contents + end

def generate_grid(IMAGES_PER_ROW: int):
    rows: list[tuple] = []

    for wall_dir in get_wallpaper_dirs():
        # row temporário pra ser transformado na tuplas com o número de itens
        # correspondente ao limite estabelecido pelo images per row
        temp_row = []

        for img in wall_dir.iterdir():
            if not verify_image(img):
                continue
            
            # adicionar a imagem no row temporário
            temp_row.append(img)

            # depois, verificar se o limite do row já foi atingido
            # se foi, adicionar esse temp row finalizado aos rows finais
            # e resetar ele, pra que o próximo temp row seja criado do zero
            if len(temp_row) == IMAGES_PER_ROW:
                rows.append(tuple(temp_row))
                temp_row = []
        
        # adicionar as imagens restantes caso o ultimo row nao tenha completado 3
        if temp_row:
            rows.append(temp_row)
    
    grid = ""

    # criar um row pra cada tupla, adicionando eles à grid final
    for img_tuple in rows:
        grid += generate_html_row(img_tuple)
    
    return grid

def generate_main_readme(instructions):
    # criar os conteúdos do readme principal, unindo o summary, grid, definindo a quantidade de imagens por row
    # e juntando os dois no final
    summary = generate_summary()
    grid = generate_grid(IMAGES_PER_ROW=3)

    contents = f"""
<div>
    {instructions}
</div>

<div>
    {summary}
</div>

<div>
    {grid}
</div>
    """

    return contents