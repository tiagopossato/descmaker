import subprocess
import os

input_file = '2_MesaMontagem_Flexível.wmod'

output_dir = 'code_c'

descmaker = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..','..','descmaker.py')

if __name__ == '__main__':
    print(descmaker)
    result = subprocess.Popen(['python3', descmaker, '-i', input_file, '-o', output_dir, '-l', 'c'])
    result.wait()
    if(result.returncode != 0):
        print("\n--->Error running descmaker!\n")
        print("\nAre you running on the same path as the script?\n\n")
        exit(-1)
    else:
        print("\n--->descmaker executed successfully!\n")
