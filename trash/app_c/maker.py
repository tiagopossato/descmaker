try:
    import os
    import argparse
    from utils import copy_directory, remove_directory
    from descmaker_parser import descmaker_parser
    from descmaker_builder import descmaker_builder

except ImportError as e:
    print("Import error: ", e)
    exit(-1)

base_dir = os.path.dirname(os.path.realpath(__file__))

# Specify the regex patterns to exclude files and directories
exclude_files = [
    r'sup.c',  # Exclude a specific files
    r'sup.h',
    r'platformio.ini'
]

exclude_dirs = [
    r'build'  # Exclude directories build
]

def convert_supervisor(input_file, output_dir):
    """
    Main function to translate FSM in input_file to code
    """

    if input_file==None or not os.path.exists(input_file):
        print(f"File {input_file} not found")
        # raise exception
        raise FileNotFoundError

    # join script path with 'base_code' folder
    base_code_path = os.path.join(base_dir, 'base_code')

    # Call the function to copy the directory structure
    try:
        copy_directory(base_code_path, output_dir, exclude_files, exclude_dirs)
        print("Directory copied successfully!")
    except Exception as e:
        print("Directory copy failed!")
        exit(-1)
        
    # print input_file and output files
    print(f"Input file: {input_file}")
    print(f"Output path: {output_dir}")

    # parser
    supervisors, global_event_list = descmaker_parser(input_file)

    # builder
    descmaker_builder(supervisors, global_event_list, output_dir)  

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, help='Input file', required=True)
    parser.add_argument('--output', type=str, help='Output path', default='generated_code', required=False)

    input_file = parser.parse_args().input
    output_dir = parser.parse_args().output

    try:
        convert_supervisor(input_file, output_dir)
        print("Supervisor converted successfully!")
    except Exception as e:
        # remove output directory
        remove_directory(output_dir)
        print(e)