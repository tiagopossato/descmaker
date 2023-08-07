import argparse
import os
import subprocess

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
        exit(-1)

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
        if(os.name == 'nt'):
            result = subprocess.Popen(['python', '-m', 'venv', 'env'])
        else:
            result = subprocess.Popen(['python3', '-m', 'venv', 'env'])
        result.wait()

        if(result.returncode != 0):
            print("Error creating virtual env!")
            exit(-1)
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

    # Path to the script that must run under the virtualenv
    maker = os.path.join(script_path, 'maker.py')

    result = subprocess.Popen([python_bin, maker, '--input', input_file, '--output', output_dir])
    result.wait()

    if os.name == 'posix' and execute and result.returncode == 0:
        print("Executing generated code...")
        # change execution path to output_dir
        os.chdir(output_dir)
        # execute main.py   
        os.system('./run.sh')