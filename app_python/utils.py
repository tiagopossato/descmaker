import os
import shutil
import re

def copy_directory(source, destination, exclude_files=None, exclude_dirs=None):
    if os.path.exists(destination):
        overwrite = input("Output directory exists. Do you want to overwrite it? [y/n]: ")
        if overwrite == 'y':
            # remove directory
            shutil.rmtree(destination)
        else:
            exit(-1)
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