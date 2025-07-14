import json
from pathlib import Path

from utils.images import get_img_size, verify_image
from utils.paths import SOURCES

"""
    gera os readmes dentro de cada pasta, listando todas as imagens dentro delas
"""

def generate_html_figure(img_name, source_url, img_dimensions):
    width = img_dimensions[0]
    height = img_dimensions[1]

    return f'''
<figure>
    <a href="{img_name}"><img alt="{img_name}" src="{img_name}"></a>
    <figcaption>
        <a href="{source_url}">source</a>
        {width}x{height}
    </figcaption>
</figure>
<hr>
            '''

def generate_sub_readme(wall_dir: Path):
    def load_sources(sources_path: Path):
        # carrega o json de sources. deve ser usado fora do loop pra carregar apenas uma vez
        with sources_path.open("r") as f:
            return json.load(f)

    contents = ""
    sources = load_sources(SOURCES)

    for item in wall_dir.iterdir():
        # ignorar arquivos que não são imagens
        if not item.is_file() or not verify_image(item):
            continue
        
        # obter dimensões e source da imagem
        img_size = get_img_size(item)

        # obter a source da imagem, primeiro pesquisando uma chave com o mesmo nome do diretório de wallpapers atual
        # se existir, depois disso procura por uma sub chave dentro desse dicionário que tenha o mesmo nome do item atual
        # obtendo o valor de sua chave, que é a url da source
        url = sources.get(wall_dir.name, {}).get(item.name, "")

        # gerar a seção html da imagem
        contents += generate_html_figure(item.name, url, img_size)

    return contents