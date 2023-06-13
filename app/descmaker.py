import argparse
import os
import subprocess
import shutil
import re

def copy_directory(source, destination, exclude_files=None, exclude_dirs=None):
    if os.path.exists(destination):
        overwrite = input("Output directory exists. Do you want to overwrite it? [y/n]: ")
        if overwrite == 'y':
            # remove directory
            shutil.rmtree(output_dir)
        else:
            exit(0)
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


# Specify the regex patterns to exclude files and directories
exclude_files = [
    r'\b\w*supervisors/sup.\w*\b',  # Exclude a specific files with end with .pyc
]

exclude_dirs = [
    r'build'  # Exclude directories like 'internal1', 'internal2', etc.
]

if __name__ == '__main__':
    # verify if user set params
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', type=str, help='Input file', required=True)
    parser.add_argument('-o', type=str, help='Output path', default='generated_code', required=False)
    if(os.name == 'posix'):
        parser.add_argument('-e', action=argparse.BooleanOptionalAction, help='Execute generated code', required=False)

    input_file = parser.parse_args().i
    output_dir = parser.parse_args().o
    if(os.name == 'posix'):
        execute = parser.parse_args().e

    # verify if input file exists
    if not os.path.exists(input_file):
        print(f"Input file '{input_file}' not found.")
        # print parser help
        parser.print_help()
        exit(0)

    # print input and output files
    print(f"Input file: {input_file}")
    print(f"Output path: {output_dir}")
    if(os.name == 'posix'):
        print(f"Execute: {execute}")

    # get execution path
    execution_path = os.getcwd()
    # join execution path with output_dir
    output_dir = os.path.join(execution_path, output_dir)
    
    # get script path
    script_path = os.path.dirname(os.path.realpath(__file__))
    # join script path with 'base_code' folder
    base_code_path = os.path.join(script_path, 'base_code')

    # get parent directory of script path
    parent_dir = os.path.dirname(script_path)

    env_dir = os.path.join(parent_dir, 'env')

    # Path to a Python interpreter that runs any Python script
    # under the virtualenv /path/to/virtualenv/
    if(os.name == 'nt'):
        python_bin = os.path.join(env_dir, 'Scripts', 'python.exe')
    else:
        python_bin = os.path.join(env_dir, 'bin', 'python')

    # verify if virtual env named 'env' exists
    if not os.path.exists(env_dir):
        # change execution path to output_dir
        os.chdir(parent_dir)
        print(f"Virtual env 'env' not found in '{parent_dir}'.")
        # create virtual env
        print("Creating virtual env...")
        os.system('python3 -m venv env')
        print("Virtual env created successfully!")
        # install requirements
        print("Installing requirements...")
        result = subprocess.Popen([python_bin, '-m', 'pip', 'install', '-r', 'app/requirements.txt'])
        result.wait()
        if(result.returncode != 0):
            print("Error installing requirements!")
            exit(0)
        else:
            print("Requirements installed successfully!")
    
    # Call the function to copy the directory structure
    copy_directory(base_code_path, output_dir, exclude_files, exclude_dirs)
    print("Directory copied successfully!")

    # Path to the script that must run under the virtualenv
    maker = os.path.join(script_path, 'maker.py')

    # print(f'Python bin: {python_bin}')
    # print(f'Maker: {maker}')

    result = subprocess.Popen([python_bin, maker, '--input', input_file, '--output', output_dir])
    result.wait()

    if os.name == 'posix' and execute and result.returncode == 0:
        print("Executing generated code...")
        # change execution path to output_dir
        os.chdir(output_dir)
        # execute main.py   
        os.system('./run.sh')