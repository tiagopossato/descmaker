import subprocess
import os

input_file = 'Manufacturing_System_models.wmod'

output_dir = 'code_python'

descmaker = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..','..','descmaker.py')

if __name__ == '__main__':
    print(descmaker)
    result = subprocess.Popen(['python3', descmaker, '-i', input_file, '-o', output_dir, '-l', 'python', '-e'])
    result.wait()
    if(result.returncode != 0):
        print("\n--->Error running descmaker!\n")
        print("\nAre you running on the same path as the script?\n\n")
        exit(-1)
    else:
        print("\n--->descmaker executed successfully!\n")
