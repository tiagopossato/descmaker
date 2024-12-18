import os
import shutil
import re
import sys
from string import Template

verified_sup_names = set()

class CustomTemplate(Template):
    delimiter = '%$%'

def fill_template(template, dest, template_dict):
    # verify if script is being executed on Windows and convert paths to Windows format
    if os.name == 'nt':
        template = template.replace('/', '\\')
        dest = dest.replace('/', '\\')

    # make the names of the files
    with open(template, 'r', encoding='utf-8') as f:
        src = CustomTemplate(f.read())
        result = src.safe_substitute(template_dict)

    with open(dest,'w', encoding='utf-8') as arquivo:
        arquivo.write(result)


def copy_directory(source, destination, exclude_files=None, exclude_dirs=None):
    if os.path.exists(destination):
        overwrite = input("Output directory exists. Do you want to overwrite it? [y/n]: ")
        if overwrite == 'y':
            # remove directory
            shutil.rmtree(destination)
        else:
            sys.exit(-1)
    # Create the destination directory
    os.makedirs(destination)

    for item in os.listdir(source):
        source_path = os.path.join(source, item)
        destination_path = os.path.join(destination, item)

        if os.path.isfile(source_path):
            # Skip the excluded files based on regex pattern
            # print(f"Copying file: {source_path}, item: {item}")
            if exclude_files and any(re.match(pattern, item) for pattern in exclude_files):
                # print(f"Skipping file: {source_path}")
                continue

            # Copy files
            shutil.copy2(source_path, destination_path)
        elif os.path.isdir(source_path):
            # Skip the excluded directories based on regex pattern
            # print(f"Copying dir: {source_path}")
            if exclude_dirs and any(re.match(pattern, item) for pattern in exclude_dirs):
                # print(f"Skipping dir: {source_path}")
                continue

            # Recursively copy directories
            copy_directory(source_path, destination_path, exclude_files, exclude_dirs)

def remove_directory(path):
    shutil.rmtree(path)

def is_valid_sup_name(_sup_name):
    """
    Regular expression pattern to check if the sup_name is valid for C and Python
    (max 10 characters)
    """
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]{0,9}$'
    return re.match(pattern, _sup_name)

def clean_sup_name(_sup_name):
    # Remove invalid characters
    _sup_name = re.sub(r'[^a-zA-Z0-9_]', '', _sup_name)
    # Limit the length to 10 characters
    return _sup_name[:10]

def validate_and_update_variable_name(_sup_name):
    """
    validate the supervisor's name to match the variable naming rules in C
    """
    if is_valid_sup_name(_sup_name):
        return _sup_name

    cleaned_sup_name = clean_sup_name(_sup_name)
    if cleaned_sup_name in verified_sup_names:
        counter = 1
        while f"{cleaned_sup_name}_{counter}" in verified_sup_names:
            counter += 1
        cleaned_sup_name = f"{cleaned_sup_name}_{counter}"
    verified_sup_names.add(cleaned_sup_name)
    return cleaned_sup_name

if __name__ == "__main__":
    # Example usage:
    sup_name = input("Enter the sup_name: ")
    verified_sup_name = validate_and_update_variable_name(sup_name)
    print("Supervisory name after verification:", verified_sup_name)
