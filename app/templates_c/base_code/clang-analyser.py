import os
import subprocess

for directory in ['lib', 'src']:
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.c') or file.endswith('.h'):
                filepath = os.path.join(root, file)
                print(f'Verying {filepath}')
                subprocess.run(['clang-tidy', filepath,
                '-warnings-as-errors=*', 
                '-p=/home/tiago/descmaker/app/templates_c/base_code/build/compile_commands.json',
                '--',
                '-std=c99'],
                check=True)
