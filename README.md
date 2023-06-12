# DEScMaker

This tool can parse a "Waters/Supremica" file (.wmod) and generate a C code with the same structure of the inside supervisors and distinguishers.

The code generated is independent and don't any requeriment.

# How to use

## Pre-requisites

Install python3.

### Supremica
- For convenience, when synthesizing a supervisor, mark the 'Rename states' option.
- Before send supervisor 'To editor', 'Rename automaton' to remove caracteres and spaces. Keep only letters and numbers.
- Do not name a supervisor as 'supervisor'
- The name of all distinguishers MUST start with GD. For example, GD1, GD2, GDwhatever, etc.
- As one would anticipate, it is imperative that no other components bear nomenclature commencing with 'GD'.

## Generate code

run `python3 app\descmaker.py -i <input> -o <output> -e` with terminal to execute the software:
- `-i <input>` : input file (required)
- `-o <output>` : output directory. Default: generated_code
- `-e` : in Linux, if present, compile with cmake/gcc and execute the generated code. Default: no execution

In the first execution, the script will create the virtual environment and install the dependencies. This can take a while. After that, the script will generate the code.

The script will generate a structure with the same name of the output directory. The folder will contain the generated code, organized in the same structure of the `base_code`. Inside generated code also will be a `README.md` with the instructions to run the code. Now, this can be readed in `app/base_code/README.md`.


# Visual explanation

![Visual explanation](https://github.com/tiagopossato/descmaker/blob/main/docs/visual_readme.svg?raw=true)

# How to cite this work

```bibtex
@software{Possato2023,
author = {Possato, Tiago},
license = {GPL-3.0+},
month = {4},
title = {{DEScMaker}},
url = {https://github.com/tiagopossato/descmaker},
year = {2023}
}
```

```apa
Possato, T. (2023). DEScMaker [Computer software]. https://github.com/tiagopossato/descmaker
```

```abnt
POSSATO, Tiago. DEScMaker. 2023. Disponível em: <https://github.com/tiagopossato/descmaker>. Acesso em: dia mes. ano.
```
