import glob
import logging
import os
import shutil
from pathlib import Path
import textwrap
import re
import yaml

import click

logger = logging.getLogger(__name__)

# List of directories and files to ignore
ignore_list = ['__init__.py', '_init.py', 'init.py', '.pyproject', '.project',
               '.gitignore', '.git', '.vscode', 'LICENSE', 'update_repo_structure.py',
               '.mypy_cache', '.pydevproject', '_out']


def create_new_structure(original_path, new_path):
    stack = [(original_path, new_path)]

    # Add all of the files in the original path that don't start with 'Level'
    ignore_list_extra = set(ignore_list + [e for e in os.listdir(original_path) if not e.startswith('Level')])

    while stack:

        current_original, current_new = stack.pop()

        # Use glob for a simpler way to get files and directories
        entries = glob.glob(os.path.join(current_original, '*')) + glob.glob(os.path.join(current_original, '.*'))

        for item_path in entries:
            entry_name = os.path.basename(item_path)

            if entry_name.startswith('.'):
                # we don't need to process dot files
                continue
                # entry_name = entry_name[1:]

            if os.path.isdir(item_path) and entry_name not in ignore_list_extra:
                # Handle directories
                if "Level" in entry_name or "Module" in entry_name or "module" in entry_name:
                    if "-" in entry_name:
                        dir_to_add, sub_dir_to_add = entry_name.split('-', 1)
                    elif "_" in entry_name:
                        dir_to_add, sub_dir_to_add = entry_name.split('_', 1)
                    else:
                        continue

                    new_directory_path = os.path.join(current_new, dir_to_add, sub_dir_to_add)
                    try:
                        os.makedirs(new_directory_path)
                        stack.append((item_path, new_directory_path))
                    except FileExistsError:
                        continue
                else:
                    new_directory_path = os.path.join(current_new, entry_name)
                    try:
                        os.makedirs(new_directory_path)
                        stack.append((item_path, new_directory_path))
                    except FileExistsError:
                        continue

            else:
                # Handle files                
                if entry_name not in ignore_list_extra:
                    if entry_name.startswith('_'):
                        entry_name = entry_name[1:]

                    if entry_name.endswith(('.py', '.pyde')):
                        # Create the new directory with the Python file's name and the '_' removed
                        if entry_name.startswith('_'):
                            new_directory_path = os.path.join(current_new, entry_name[1:-3] if entry_name.endswith(
                                '.py') else entry_name[1:-5])
                        else:
                            new_directory_path = os.path.join(current_new, entry_name[:-3] if entry_name.endswith(
                                '.py') else entry_name[:-5])
                        new_directory_path = os.path.join(current_new, os.path.splitext(entry_name)[0])
                        try:
                            os.makedirs(new_directory_path)
                            stack.append((item_path, new_directory_path))
                        except FileExistsError:
                            pass
                        # Move the file to the new directory
                        shutil.copy2(item_path, new_directory_path)
                    else:
                        # CREATE THE NEW DIRECTORY NAMED RESOURCES AND ADD IT TO THE STACK
                        try:
                            new_directory_path = os.path.join(current_new, 'resources')
                            os.makedirs(new_directory_path)
                            stack.append((item_path, new_directory_path))
                        except FileExistsError:
                            pass
                        if stack:
                            _, latest_directory = stack[-1]
                            shutil.copy2(item_path, latest_directory)


def remove_underscore_from_files(directory_path):
    import re

    file_p = re.compile(r'^(_\d+_|_[a-z]_|_|[a-z]_)')
    dir_p = re.compile(r'^(_|[a-z]_)')

    path = Path(directory_path)

    # Traverse through all files and directories
    for item in path.rglob('*'):  # rglob('*') will match all files and directories
        if item.is_file() and file_p.match(item.name):
            logger.debug(f"Matched file: {item.name}")
            item.rename(item.with_name(file_p.sub('', item.name)))
        elif item.is_dir() and dir_p.match(item.name):
            new_name = item.with_name(dir_p.sub('', item.name))
            logger.debug(f"Matched dir: {item.name}, rename to {new_name}")
            item.rename(new_name)


import ast


def remove_main_guard(file_path):
    with open(file_path, 'r') as file:
        source = file.read()

    # Parse the source code into an AST
    tree = ast.parse(source)

    # Find the __main__ guard
    main_guard_index = None
    for i, node in enumerate(tree.body):
        if isinstance(node, ast.If) and \
           isinstance(node.test, ast.Compare) and \
           len(node.test.ops) == 1 and \
           isinstance(node.test.ops[0], ast.Eq) and \
           len(node.test.comparators) == 1 and \
           isinstance(node.test.comparators[0], ast.Str) and \
           node.test.comparators[0].s == '__main__':
            main_guard_index = i
            break

    if main_guard_index is not None:
        # Extract the code within the main guard
        main_guard_code = ast.get_source_segment(source, tree.body[main_guard_index])

        # Remove the guard but keep the code within the guard
        start = main_guard_code.find(':') + 1
        inner_code = main_guard_code[start:]

        # Remove leading indentation from the inner code
        inner_code = textwrap.dedent(inner_code)

        # Replace the original guard with the inner code
        modified_source = source.replace(main_guard_code, inner_code)

        # Write out the modified file
        with open(file_path, 'w') as file:
            file.write(modified_source)
        logger.info(f"Removed main guard from {file_path}")


def process_python_files(directory):
    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        # Find all .py files
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)

                try:
                    remove_main_guard(file_path)
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")




def create_yaml_file(path, level, module, lesson, title):
    data = {
        'level': level,
        'module': module,
        'lesson': lesson,
        'title': title,
        'description': ''
    }

    yaml_file_path = path / '.assignment.yaml'
    with open(yaml_file_path, 'w') as file:
        yaml.dump(data, file, sort_keys=False)

def create_assignment_data(root_path):
    root = Path(root_path)
    level_pattern = re.compile(r'Level(\d+)')
    module_pattern = re.compile(r'Module(\d+)')

    for level_dir in root.iterdir():
        if level_dir.is_dir() and level_pattern.match(level_dir.name):
            level = int(level_pattern.search(level_dir.name).group(1))
            for module_dir in level_dir.iterdir():
                if module_dir.is_dir() and module_pattern.match(module_dir.name):
                    module = int(module_pattern.search(module_dir.name).group(1))
                    for lesson_dir in module_dir.iterdir():
                        if lesson_dir.is_dir():  # Assuming all subdirectories in module are lessons
                            lesson = lesson_dir.name
                            for assignment_dir in lesson_dir.iterdir():
                                if assignment_dir.is_dir():  # Assuming all subdirectories in lesson are assignments
                                    title = assignment_dir.name
                                    create_yaml_file(assignment_dir, level, module, lesson, title)


def_path = Path('./_out')


@click.command()
@click.option('--original_path', '-o', default=os.getcwd(), help='Path to the original directory')
@click.option('--new_path', '-n', default=def_path, help='Path to the new directory')
@click.option('--verbose', '-v', is_flag=True, help='Enable verbose logging')
def main(original_path: str, new_path: str, verbose: bool):
    if verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    if def_path.exists() and str(new_path) == str(def_path):
        logger.info(f"Removing existing directory: {new_path}")
        shutil.rmtree(new_path)

    logger.info(f'Source path: {original_path}')
    logger.info(f'Destination path: {new_path}')
    #create_new_structure(original_path, new_path)

    remove_underscore_from_files(new_path)

    process_python_files(new_path)

    #create_assignment_data(new_path)

if __name__ == '__main__':
    main()
