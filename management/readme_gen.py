import json
from PIL import Image
from pathlib import Path

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
</figure><br>
            '''

def generate_readme(wallpaper_dir: Path):
    def get_img_size(img_file: Path):
        # obter as dimensões da imagem em uma tupla (largura, altura)
        with Image.open(img_file) as img:
            return img.size

    def load_sources(sources_path: Path):
        # carrega o json de sources. deve ser usado fora do loop pra carregar apenas uma vez
        sources_path
        with sources_path.open("r") as f:
            return json.load(f)

    contents = ""
    sources = load_sources(Path("management/sources.json"))

    for item in wallpaper_dir.iterdir():
        # ignorar arquivos que não são imagens
        if not item.is_file() or item.suffix == ".md":
            continue
        
        # obter dimensões e source da imagem
        img_size = get_img_size(item)

        # obter a source da imagem, primeiro pesquisando uma chave com o mesmo nome do diretório de wallpapers atual
        # se existir, depois disso procura por uma sub chave dentro desse dicionário que tenha o mesmo nome do item atual
        # obtendo o valor de sua chave, que é a url da source
        url = sources.get(wallpaper_dir.name, {}).get(item.name, "")

        # gerar a seção html da imagem
        contents += generate_html_figure(item.name, url, img_size)

    readme = wallpaper_dir / "README.md"
    with open(readme, "w", encoding="utf-8") as f:
        f.write(contents)

generate_readme(Path("/mnt/seagate/workspace/coding/projects/repos/wallpapers/anime"))