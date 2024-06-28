import os


def explodePath(path: str) -> list[str]:

    sliced_path: list[str] = []

    path = path.replace('.', '')

    if '/' in path:
        sliced_path = path.split('/')
    elif '\\' in path:
        sliced_path = path.split('\\')

    return sliced_path


def joinPath(exploded_path: list[str]) -> str:
    
    path: str = os.getcwd()

    for folder in exploded_path:
        path = os.path.join(path, folder)
    
    return path

