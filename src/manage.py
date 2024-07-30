import logging
import os
import shutil
from pathlib import Path
from textwrap import dedent

import click
import yaml

from lib.walk import *

logger = logging.getLogger(__name__)


@click.group()
@click.option('-v', '--verbose', is_flag=True, show_default=True, default=False, help="INFO logging")
@click.option('-vv', '--debug', is_flag=True, show_default=True, default=False, help="DEBUG logging")
@click.option('-E', '--exceptions', is_flag=True, show_default=True, default=False,
              help="Display exception stack traces")
def main(verbose: bool, debug: bool,  exceptions: bool):

    if debug:
        logging.basicConfig()
        logger.setLevel(logging.DEBUG)
    elif verbose:
        logging.basicConfig()
        logger.setLevel(logging.INFO)

    global show_exceptions
    show_exceptions = exceptions


def main_entry():
    try:
        main()
    except Exception as e:
        if show_exceptions:
            raise
        else:
            click.echo(f"Error: {e}")

@main.command(name='meta', help='Regenerate meta.yaml')
@click.option('-l', '--level_dir', default='levels', help="Root directory to levels")
def meta(level_dir='levels'):

    for p, n in walk_python(Path(level_dir)):
        #print(n, p)

    
        l,m,ls, a = get_lmla(Path(p))

        print(f"{n} {p} Level: {l}, Module: {m}, Lesson: {ls}, Assignment: {a}")

@main.command(name='rename', help='Regenerate meta.yaml')
@click.option('-l', '--level_dir', default='levels', help="Root directory to levels")
def rename(level_dir='levels'):

    from PIL import Image

    for p in walk_images(Path(level_dir)):
        p = Path(p).absolute()

        if p.suffix.lower() in {'.gif', '.jpeg', '.jpg'}:
            img = Image.open(p)
            png_path = p.with_suffix('.png')
            img.save(png_path, 'PNG')
            print(f"Converted {p.name} to {png_path.name}")
            # unlink the original
            p.unlink()
            p = Path(png_path).absolute

        if '/data/' in str(p):
            n = str(p).replace('/data/', '/images/')
            Path(n).parent.mkdir(parents=True, exist_ok=True)
            p.rename(n)
            print(f"Renamed {p} to {n}")
            

if __name__ == '__main__':
    main_entry()