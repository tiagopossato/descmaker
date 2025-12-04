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
    │   ├── templates_esp-idf
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

## Generated code for ESP32 using ESP-IDF file tree
    .
    ├── components
    │   ├── supervisor
    │   │   ├── CMakeLists.txt
    │   │   ├── sup_debug.h
    │   │   ├── supervisor.c
    │   │   └── supervisor.h
    │   ├── event_handler
    │   │   ├── CMakeLists.txt
    │   │   ├── event_handler.c
    │   │   ├── event_handler.h
    │   │   ├── events.c
    │   │   └── events.h
    │   └── supervisors
    │       ├── CMakeLists.txt
    │       ├── supervisor_list.c
    │       ├── supervisor_list.h
    │       ├── [sups].c
    │       └── [sups].h
    ├── main
    │   ├── CMakeLists.txt
    │   └── main.c
    └── CMakeLists.txt

# How to use

## Pre-requisites

Install python3.

### Supremica
- For convenience, when synthesizing a supervisor, mark the 'Rename states' option.
- Before send supervisor 'To editor', 'Rename automaton' to remove caracteres and spaces. Keep only letters and numbers.
- Do not name a supervisor as 'supervisor'

## Generate code

**In the root folder (not in '\app')** run `python3 descmaker.py -i <input> -o <output> -l <language> -e` with terminal to execute the software:
- `-i <input>` : input file (required)
- `-o <output>` : output directory. Default: generated_code
- `-l <language>` : output language. Can be c, python or esp-idf. Default: c
- `-e` :  If present, compile with cmake/gcc and execute the generated code. Default: no execution

In the first run, the script will create the virtual environment and install the dependencies. This can take a while. After that, the script will generate the code.

The script will generate a structure with the same name of the output directory. The folder will contain the generated code, arranged in the same structure of the `app/templates_[language]/base_code`. Inside generated code also will be a `README.md` with the instructions to run the code. Now, this can be readed in `app/templates_[language]/base_code/README.md`.


# Visual description

![Visual description](https://github.com/tiagopossato/descmaker/blob/main/docs/visual_readme.svg?raw=true)

# How to cite this work

```bibtex
@article{Possato2026,
title = {DEScMaker: A tool for automated code generation for discrete event systems controllers},
journal = {Science of Computer Programming},
volume = {247},
pages = {103350},
year = {2026},
issn = {0167-6423},
doi = {https://doi.org/10.1016/j.scico.2025.103350},
url = {https://www.sciencedirect.com/science/article/pii/S0167642325000899},
author = {Tiago Possato and João H. Valentini and Luiz F.P. Southier and Marco A.C. Barbosa and Marcelo Teixeira},
keywords = {Formal modeling, Automated code generation, Implementation},
}
```

```apa
Possato, T., Valentini, J. H., Southier, L. F. P., Barbosa, M. A. C., & Teixeira, M. (2026). DEScMaker: A tool for automated code generation for discrete event systems controllers. Science of Computer Programming, 247, 103350. https://doi.org/10.1016/j.scico.2025.103350
```

```abnt
POSSATO, T. et al. DEScMaker: A tool for automated code generation for discrete event systems controllers. Science of Computer Programming, v. 247, p. 103350, jan. 2026. Disponível em: <https://www.sciencedirect.com/science/article/pii/S0167642325000899>. Acesso em: dia mes. ano.
```

Version 2.2.0: esp-idf output adjusted
