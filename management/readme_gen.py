from pathlib import Path

def generate_readme(wallpaper_dir: Path):
    contents = ""

    for item in wallpaper_dir.iterdir():
        if item.is_file() and not item.suffix == ".md":
            contents += f'<a href="a_statue_of_a_woman_with_wings_and_a_plant.png"><img alt="a_statue_of_a_woman_with_wings_and_a_plant" src="a_statue_of_a_woman_with_wings_and_a_plant.png"></a>'