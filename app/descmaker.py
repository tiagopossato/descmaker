"""
Script to convert the code
"""
import os
import argparse
from utils import copy_directory, remove_directory
from descmaker_parser import descmaker_parser
from descmaker_python_builder import descmaker_python_builder
from descmaker_c_builder import descmaker_c_builder
from descmaker_espidf_builder import descmaker_espidf_builder

# Specify the regex patterns to exclude files and directories
exclude_files = [
    r'\b\w*template\w*\b',  # Exclude a specific files with *template*
    r'\b\w*.pyc',  # Exclude a specific files with end with .pyc
    r'sup.py',  # Exclude a specific files
    r'sup.c',
    r'sup.h',
    r'platformio.ini'
]

exclude_dirs = [
    r'__pycache__',
    r'build'
]

base_dir = os.path.dirname(os.path.realpath(__file__))


def convert_supervisor(input_file, output_dir, output_language):
    """
    Does convert the code
    """
    if input_file is None or not os.path.exists(input_file):
        print(f"File {input_file} not found")
        # raise exception
        raise FileNotFoundError

    if output_language not in ('c', 'python', 'esp-idf'):
        print(f'{output_language} not implemented')
        raise NotImplementedError

    # join script path with 'base_code' folder
    base_code_path = os.path.join(base_dir, 'templates_'+output_language, 'base_code')

    # Call the function to copy the directory structure
    copy_directory(base_code_path, output_dir, exclude_files, exclude_dirs)
    print("Directory copied successfully!")

    # print input and output files
    print(f"Input file: {input_file}")
    print(f"Output path: {output_dir}")

    # parser
    supervisors, global_event_list, supervisor_list = descmaker_parser(input_file)

    # builder
    if output_language=='python':
        descmaker_python_builder(supervisors, global_event_list, supervisor_list,
                                 base_dir, output_dir)
    if output_language=='c':
        descmaker_c_builder(supervisors, global_event_list, base_dir, output_dir)
    if output_language=='esp-idf':
        descmaker_espidf_builder(supervisors, global_event_list, base_dir, output_dir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, help='Input file', required=True)
    parser.add_argument('--output', type=str, help='Output path',
                        default='generated_code', required=False)
    parser.add_argument('-l', type=str, help='Output language',
                        choices=['c', 'python', 'esp-idf'], default='c', required=False, nargs=1)

    input_file_ = parser.parse_args().input
    output_dir_ = parser.parse_args().output
    output_language_ = parser.parse_args().l[0]

    try:
        convert_supervisor(input_file_, output_dir_, output_language_)
        print("Supervisor converted successfully!")
    except Exception as e:
        # remove output directory
        remove_directory(output_dir_)
        print(e)
