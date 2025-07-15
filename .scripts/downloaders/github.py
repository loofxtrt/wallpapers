from urllib.parse import urlparse
from pathlib import Path, PurePosixPath
import requests


def url_to_raw(url: str):
    """
        transforma uma url de repositório em uma url de raw content. ex:  
        original: https://github.com/dharmx/walls/blob/main/anime/a_road_with_power_lines_and_power_lines.png  
        raw: https://raw.githubusercontent.com/dharmx/walls/refs/heads/main/anime/a_road_with_power_lines_and_power_lines.png  
          
        original: https://github.com/michaelScopic/Wallpapers/blob/main/linux/0405.jpg  
        raw: https://raw.githubusercontent.com/michaelScopic/Wallpapers/refs/heads/main/linux/0405.jpg
    """

    parsed_url = urlparse(url) # transformar a string em uma url parseada
    path = PurePosixPath(parsed_url.path) # obter apenas o path da url, excluindo o domínio. ex: /dharmx/walls/blob/main/...

    parts = list(path.parts) # quebrar o path em partes, ex: ['', 'dharmx', 'walls', 'blob', 'main', 'anime', 'file.png']

    if "blob" in parts:
        # obtem a posição em que 'blob' aparece na lista
        blob_index = parts.index("blob")

        # obter as posições dos outros elementos da url
        user_repo = parts[1:3] # vai do índice 1 até o 3, obtendo: dharmx (índice 1) e walls (índice 2)
        branch = parts[blob_index + 1] # obtém o nome do branch, que vem depois da posição do blob
        rest = parts[blob_index + 2 :] # restante do caminho depois do nome do branch

        # montar o novo path completo
        # o * antes de new_parts faz com que a lista seja desempacotada antes de ser passada pra função como um único argumento
        # seria o equivalente de escrever: PurePosixPath('', 'dharmx', 'walls', 'refs', 'heads', 'main', 'anime', 'file.png')
        new_parts = [''] + user_repo + ['refs', 'heads', branch] + rest
        new_path = PurePosixPath(*new_parts)
    else:
        # se não tiver 'blob', usa o path original
        new_path = path

    raw_url = f"https://raw.githubusercontent.com/{new_path}"
    return raw_url

def get_name_from_url(url: str):
    # obter apenas o nome do arquivo na url, o último elemento
    parsed_url = urlparse(url)
    path = PurePosixPath(parsed_url.path)
    last = path.name

    return last

def download_from_github(url: str, destination: str = None):
    if not destination:
        print("destino inválido")
        return

    raw_url = url_to_raw(url)
    file_name = get_name_from_url(url)

    # começar uma requisição pra url
    req = requests.get(raw_url, stream=True)
    req.raise_for_status()

    # montar o caminho final do arquivo
    final_file = Path(destination) / file_name

    # abrir esse arquivo, e nele, em chunks de 8192 bytes, baixar o arquivo
    with final_file.open("wb") as f:
        for chunk in req.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)