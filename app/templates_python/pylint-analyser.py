"""
Analyser
"""
import os
import subprocess

for directory in ['base_code', 'template']:
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py') and not file.endswith('-template.py'):
                filepath = os.path.join(root, file)
                print(f'Verying {filepath}')
                subprocess.run(['pylint',
                '--py-version=3.12',
                filepath],
                check=False)
