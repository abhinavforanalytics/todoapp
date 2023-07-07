import zipfile
from pathlib import Path


def make_archive(filepaths, destination_dir):
    dest_path = Path(destination_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = Path(filepath)   # Override the variable
            archive.write(filepath, arcname=filepath.name)  # filepath.name mentioned to
            # avoid including full path decompression and it only includes the filename not the full path


if __name__ == "__main__":
    make_archive(filepaths=["bonus.py", "bonus 4.py"], destination_dir="Dest")
