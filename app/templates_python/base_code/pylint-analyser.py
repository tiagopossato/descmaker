"""
Analyser
"""
import os
import subprocess

for root, dirs, files in os.walk('Supervisor'):
    for file in files:
        if file.endswith('.py'):
            filepath = os.path.join(root, file)
            print(f'Verying {filepath}')
            subprocess.run(['pylint',
            '--py-version=3.12',
            filepath],
            check=False)
