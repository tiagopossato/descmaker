# DEScMaker

This tool can parse a "Waters/Supremica" file (.wmod) and generate code with the same structure of the inside supervisors.

The code generated is independent and don't any requeriment.

# File tree
    .
    ├── app
    │   ├── descmaker.py
    │   ├── descmaker_parser.py
    │   ├── descmaker_c_builder.py
    │   ├── descmaker_python_builder.py
    │   ├── templates_c
    │   │   ├── base_code
    │   │   └── template
    │   ├── templates_python
    │   │   ├── base_code
    │   │   └── template
    │   └── utils.py
    ├── descmaker.py
    └── requirements.txt

## Generated Python code file tree
    .
    ├── __init__.py
    ├── log.csv
    ├── main.py
    ├── README.md
    └── Supervisor
        ├── Base
        │   ├── Event.py
        │   ├── __init__.py
        │   ├── __pycache__
        │   ├── README.md
        │   ├── State.py
        │   ├── Supervisor.py
        │   └── Transition.py
        ├── event_handler.py
        ├── events.py
        ├── __init__.py
        ├── logger.py
        ├── __pycache__
        ├── README.md
        └── supervisors
            ├── __init__.py
            ├── __pycache__
            ├── README.md
            └── [sups].py

## Generated C code file tree
    .
    ├── CMakeLists.txt
    ├── lib
    │   ├── CMakeLists.txt
    │   └── supervisor
    │       ├── CMakeLists.txt
    │       ├── README.md
    │       ├── structure.png
    │       ├── sup_debug.h
    │       ├── supervisor.c
    │       └── supervisor.h
    ├── README.md
    ├── run.sh
    └── src
        ├── event_handler
        │   ├── event_handler.c
        │   ├── event_handler.h
        │   ├── events.c
        │   └── events.h
        ├── main.c
        └── supervisors
            ├── [sups].c
            ├── [sups].h
            ├── supervisor_list.c
            └── supervisor_list.h

# How to use

## Pre-requisites

Install python3.

### Supremica
- For convenience, when synthesizing a supervisor, mark the 'Rename states' option.
- Before send supervisor 'To editor', 'Rename automaton' to remove caracteres and spaces. Keep only letters and numbers.
- Do not name a supervisor as 'supervisor'

## Generate code

run `python3 descmaker.py -i <input> -o <output> -l <language> -e` with terminal to execute the software:
- `-i <input>` : input file (required)
- `-o <output>` : output directory. Default: generated_code
- `-l <language>` : output language. Can be c or python. Default: c
- `-e` :  If present, compile with cmake/gcc and execute the generated code. Default: no execution

In the first run, the script will create the virtual environment and install the dependencies. This can take a while. After that, the script will generate the code.

The script will generate a structure with the same name of the output directory. The folder will contain the generated code, arranged in the same structure of the `app/templates_[language]/base_code`. Inside generated code also will be a `README.md` with the instructions to run the code. Now, this can be readed in `app/templates_[language]/base_code/README.md`.


# Visual description

![Visual description](https://github.com/tiagopossato/descmaker/blob/main/docs/visual_readme.svg?raw=true)

# How to cite this work

```bibtex
@software{Possato2023,
author = {Possato, Tiago and Valentini, João H. and Southier, Luiz F. P. and Teixeira, Marcelo},
license = {GPL-3.0+},
month = {4},
title = {{DEScMaker}},
url = {https://github.com/tiagopossato/descmaker},
year = {2023}
}

```

```apa
Possato, T., Valentini, J. H., Southier, L. F. P., & Teixeira, M. (2023). DEScMaker [Computer software]. https://github.com/tiagopossato/descmaker
```

```abnt
Possato, T., Valentini, J. H., Southier, L. F. P., Teixeira, M. DEScMaker. 2023. Disponível em: <https://github.com/tiagopossato/descmaker>. Acesso em: dia mes. ano.
```
