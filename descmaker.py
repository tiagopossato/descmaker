"""
Checks the parameters provided;
Checks and creates the virtual environment;
Runs DEScMaker in the app folder;
"""

import argparse
import os
import subprocess
import sys

if __name__ == '__main__':
    # verify if user set params
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', type=str, help='Input file', required=True, nargs=1)
    parser.add_argument('-o', type=str, help='Output path', default='generated_code',
                        required=False)
    parser.add_argument('-l', type=str, help='Output language',
                        choices=['c', 'python', 'esp-idf'], default='c', required=False, nargs=1)
    parser.add_argument('-e', action=argparse.BooleanOptionalAction,
                        help='Execute generated code', required=False)

    input_file = parser.parse_args().i[0]
    output_dir = parser.parse_args().o
    output_language = parser.parse_args().l[0]
    execute = parser.parse_args().e

    if not os.path.exists(input_file):
        print(f"Input file '{input_file}' not found.")
        # print parser help
        parser.print_help()
        sys.exit(-1)

    # print input and output files
    print(f"Input file: {input_file}")
    print(f"Output path: {output_dir}")
    print(f"Output language: {output_language}")
    print(f"Execute: {execute}")


    # get execution path
    execution_path = os.getcwd()

    # join execution path with output_dir
    output_dir = os.path.join(execution_path, output_dir)

    # get script path
    script_path = os.path.dirname(os.path.realpath(__file__))

    # get parent directory of script path
    # parent_dir = os.path.dirname(script_path)

    env_dir = os.path.join(script_path, 'env')
    
    # Path to a Python interpreter that runs any Python script
    # under the virtualenv /path/to/virtualenv/
    if os.name == 'nt':
        python_bin = os.path.join(env_dir, 'Scripts', 'python.exe')
    else:
        python_bin = os.path.join(env_dir, 'bin', 'python')

    # verify if virtual env named 'env' exists
    if not os.path.exists(env_dir):
        # get current execution path
        current_dir = os.getcwd()
        # change execution path to output_dir
        os.chdir(script_path)
        print(f"Virtual env 'env' not found in '{script_path}'.")
        # create virtual env
        print("Creating virtual env...")

        PYTHON_NAME = 'python3'
        if os.name == 'nt':
            PYTHON_NAME = 'python'

        with subprocess.Popen([PYTHON_NAME, '-m', 'venv', 'env']) as process:
            RESULT = process.wait()

        if RESULT != 0:
            print("Error creating virtual env!")
            sys.exit(-1)

        print("Virtual env created successfully!")
        # install requirements
        print("Installing requirements...")

        with subprocess.Popen([python_bin, '-m', 'pip', 'install', '-r',
                               'app/requirements.txt']) as process:
            RESULT = process.wait()

        if RESULT != 0:
            print("Error installing requirements!")
            sys.exit(-1)
        else:
            print("Requirements installed successfully!")
        # change execution path to output_dir
        os.chdir(current_dir)

    # Path to the script that must run under the virtualenv
    maker = os.path.join(script_path, 'app', 'descmaker.py')

    # Runs DEScMaker with Python from the virtual environment.
    with subprocess.Popen([python_bin, maker, '--input', input_file, '--output',
                           output_dir, '-l', output_language]) as process:
        RESULT = process.wait()

    if execute and RESULT == 0:
        if os.name == 'posix' and output_language == 'c':
            print("Executing generated code...")
            # change execution path to output_dir
            os.chdir(output_dir)
            # execute run.sh
            os.system('./run.sh')
        if output_language == 'python':
            print("Executing generated code...")
            # change execution path to output_dir
            os.chdir(output_dir)
            # execute main.py
            if os.name == 'nt':
                os.system('python3.exe main.py')
            else:
                os.system('python3 main.py')
