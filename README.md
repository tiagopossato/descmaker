# DEScMaker

This project can parse a Supremica file (.wmod) and generate a C code with the same structure of the inside supervisors.

The code generated is independent and don't any requeriment.

# How to use

## Pre-requisites

### Ambient

run `env_setup.sh` to creat an virtual environment and install the requeriments.

### Supremica
- For convenience, when synthesizing a supervisor, mark the 'Rename states' option.
- Before send supervisor 'To editor', 'Rename automaton' to remove caracteres and spaces. Keep only letters and numbers.

## Generate code

- Run the script `app/descmaker.sh -i <input> -o <output> -e -h`
    - `-i <input>` : input file (required)
    - `-o <output>` : output directory. Default: generated_code
    - `-e` : if present, execute the generated code. Default: no execution
    - `-h` : help

The script will generate a structure with the same name of the output directory. The folder will contain the generated code, organized in the same structure of the `base_code`. Inside generated code also will be a `README.md` with the instructions to run the code. Now, this can be readed in `app/base_code/README.md`.

# Adding path to the system
add the following line to your `~/.bashrc` file:

```bash
export PATH=$PATH:/path-to-project/app
```
than run `source ~/.bashrc` to reload the file.