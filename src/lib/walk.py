from pathlib import Path
import re

def walk_python (levels_dir):


    py_dirs = list(sorted(set(p.parent for p in levels_dir.rglob('*.py') if not p.name == '__init__.py')))
    
    return [ (p, len(list(p.glob('*.py')))) for p in py_dirs]

def walk_images(levels_dir):

    resource_extensions = ('.png', '.gif', '.jpeg', '.jpg')

    image_dirs = [p for p in levels_dir.rglob('*') if p.suffix in resource_extensions]

    return image_dirs


def get_lmla(dir_=None):

    """Get level, module, lesson, assignment from a directory"""
    if dir_ is None:
        p = Path('.')
    else:
        p = Path(dir_)

    _, level, module, *parts = str(p).split('/')

    if len(parts) == 1:
        ls, a = parts[0], parts[0]
    elif len(parts) == 2:
        ls, a = parts
    else:
        assert(False)

    return level, module, ls, a

