from pathlib import Path

from caseconverter import kebabcase

from utils.paths import get_wallpaper_img_files

def rename_files_to_kebabcase():
    for img_file in get_wallpaper_img_files():
        # converter o nome de cada arquivo de imagem arquivo pra kebab-case
        file_extension = img_file.suffix
        file_name = img_file.stem # obter o nome sem a extensão
        kebab_name = kebabcase(str(file_name))

        # montar o novo nome e renomear o arquivo
        converted_name = kebab_name + file_extension
        new_path = img_file.with_name(converted_name)
        img_file.rename(new_path)

rename_files_to_kebabcase()