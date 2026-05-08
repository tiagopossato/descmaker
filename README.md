# DEScMaker

A tool for automated code generation from Discrete Event Systems (DES) controllers modeled in Supremica/Waters.

[![Python](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-Apache%202.0-green.svg)](LICENSE)
[![DOI](https://img.shields.io/badge/DOI-10.1016%2Fj.scico.2025.103350-blue)](https://doi.org/10.1016/j.scico.2025.103350)

---

## Table of Contents

- [About](#about)
- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Input Format](#input-format)
- [Output Structure](#output-structure)
- [Examples](#examples)
- [Citing This Work](#citing-this-work)
- [License](#license)
- [Authors](#authors)

---

## About

DEScMaker parses **.wmod** files — the XML-based format used by Waters/Supremica for modeling Discrete Event Systems under the Supervisory Control Theory (SCT) — and generates standalone, dependency-free controller code in three target languages:

- **C** — for embedded systems and microcontrollers (PlatformIO / CMake)
- **ESP-IDF** — for Espressif ESP32 devices using the ESP-IDF framework
- **Python** — for rapid prototyping, simulation, and integration with [Factory I/O](https://factoryio.com/)

The generated code includes a complete supervisor runtime (event handler, state machine engine, and supervisor list) and is ready to compile and run out of the box.

This tool is described in detail in the paper:

> Possato, T., Valentini, J. H., Southier, L. F. P., Barbosa, M. A. C., & Teixeira, M. (2026). *DEScMaker: A tool for automated code generation for discrete event systems controllers*. Science of Computer Programming, 247, 103350. https://doi.org/10.1016/j.scico.2025.103350

---

## Features

- **Multi-language output** — generate C, Python, or ESP-IDF code from a single `.wmod` model
- **Automatic environment setup** — creates a Python virtual environment and installs dependencies on first run
- **Template-based generation** — clean separation between base runtime code and generated supervisor logic
- **Standalone output** — generated code depends on nothing outside its own directory
- **Supervisor runtime included** — each output bundles a complete event handler and state machine engine
- **PlatformIO & CMake ready** — C output works with PlatformIO (AVR, ARM, ESP) and standard CMake builds
- **10-character supervisor naming** — enforces C-compatible variable names (validated and auto-cleaned)

---

## Project Structure

```
.
├── descmaker.py                    # CLI entry point (venv management + argument parsing)
├── CITATION.cff                    # Citation metadata (CFF format)
├── LICENSE                         # Apache License 2.0
├── README.md
│
├── app/                            # Core application
│   ├── descmaker.py                # Orchestrator: copy base → parse → build
│   ├── descmaker_parser.py         # XML parser for .wmod files (BeautifulSoup)
│   ├── descmaker_c_builder.py      # C code generator
│   ├── descmaker_python_builder.py # Python code generator
│   ├── descmaker_espidf_builder.py # ESP-IDF code generator
│   ├── utils.py                    # Utilities: template engine, file ops, name validation
│   ├── requirements.txt            # Python dependencies (beautifulsoup4, lxml)
│   │
│   ├── templates_c/                # C language templates
│   │   ├── base_code/              #   Supervisor runtime library (supervisor.c/.h, event_handler, etc.)
│   │   └── template/               #   Code generation templates (main, events, supervisors, CMakeLists)
│   │
│   ├── templates_esp-idf/          # ESP-IDF templates
│   │   ├── base_code/              #   Runtime components (supervisor, event_handler, supervisors)
│   │   └── template/               #   Code generation templates
│   │
│   └── templates_python/           # Python templates
│       ├── base_code/              #   Runtime classes (Event, State, Supervisor, Transition, event_handler)
│       └── template/               #   Code generation templates
│
└── examples/                       # Example models and generated code
    ├── Manufacturing_System/       #   Full case study with Factory I/O scene
    │   ├── Manufacturing_System_models.wmod
    │   ├── Turn_Table.factoryio    #     Factory I/O scene file
    │   ├── code_python/            #     Generated Python controllers
    │   └── factoryIOInterface/     #     Factory I/O bridge (connection, input, output)
    │
    ├── transmission_system/        #   C code example (Transmitters)
    │
    ├── supremica_examples/         #   Various Supremica model examples
    │   ├── MesaGiratoriaModular.wmod
    │   ├── MesaGiratoriaMonolitico.wmod
    │   ├── article.wmod
    │   └── ...
    │
    └── other_examples/             #   Additional .wmod models
        ├── 1_PequenaFabrica.wmod
        ├── 2_Labirinto.wmod
        ├── 3_syncTransferLine.wmod
        ├── 4_MesaMontagem.wmod
        ├── 5_poultryprocess.wmod
        └── 6_automotiveline.wmod
```

---

## Prerequisites

- **Python 3.x** (tested on Python 3.8+)
- No other dependencies need to be pre-installed — the tool creates its own virtual environment and installs everything on first run

For running generated code:
- **C output**: GCC, CMake (>= 3.10), and optionally [PlatformIO](https://platformio.org/)
- **ESP-IDF output**: [ESP-IDF](https://docs.espressif.com/projects/esp-idf/) toolchain
- **Python output**: Python 3.x (no additional packages)

### Supremica modeling guidelines

When creating models in Supremica for use with DEScMaker:

- Enable the **"Rename states"** option when synthesizing a supervisor
- Before sending a supervisor to the editor, use **"Rename automaton"** to remove special characters and spaces — keep only letters and numbers
- Do not name any supervisor `supervisor` (reserved name)

---

## Installation

```bash
git clone https://github.com/tiagopossato/descmaker.git
cd descmaker
```

No manual dependency installation is required. The first time you run the tool, it will automatically:

1. Create a Python virtual environment in `env/`
2. Install the required packages (`beautifulsoup4`, `lxml`) from `app/requirements.txt`

The virtual environment is created only once; subsequent runs use the existing environment.

---

## Usage

Run from the **project root** (not from `app/`):

```bash
python3 descmaker.py -i <input> -o <output> -l <language> [-e]
```

### Arguments

| Argument | Required | Default | Description |
|----------|----------|---------|-------------|
| `-i` | Yes | — | Path to the input `.wmod` file |
| `-o` | No | `generated_code` | Output directory for the generated code |
| `-l` | No | `c` | Target language: `c`, `python`, or `esp-idf` |
| `-e` | No | (disabled) | Compile and execute the generated code after generation |

### Examples

**Generate C code from a Supremica model:**
```bash
python3 descmaker.py -i examples/supremica_examples/example.wmod -o my_c_project -l c
```

**Generate Python code and run it immediately:**
```bash
python3 descmaker.py -i examples/supremica_examples/example.wmod -o my_python_project -l python -e
```

**Generate ESP-IDF code for ESP32:**
```bash
python3 descmaker.py -i examples/supremica_examples/example.wmod -o my_esp_project -l esp-idf
```

**Generate C code, compile with CMake, and execute:**
```bash
python3 descmaker.py -i examples/TransmittersKallil.wmod -o output -l c -e
```

### What happens when you run

1. The tool checks for a virtual environment (`env/`) — if absent, it creates one and installs dependencies
2. It parses the `.wmod` file, extracting all supervisors, states, events, and transitions
3. It copies the appropriate base runtime code for the target language
4. It fills the templates with the parsed model data, generating per-supervisor source files
5. If `-e` is specified, it compiles and runs the generated code:
   - **C**: executes `./run.sh` (requires POSIX environment)
   - **Python**: executes `main.py`

---

## How It Works

DEScMaker follows a three-stage pipeline:

### 1. Parse (`descmaker_parser.py`)

Reads the `.wmod` XML file using BeautifulSoup and extracts:
- **Global event list** — all events declared in the model, with their kind (`CONTROLLABLE` or `UNCONTROLLABLE`)
- **Supervisors** — each supervisor's states (with initial state flag), events (filtered to those it responds to), and transitions (edges between states labeled with events)

Supervisor names are validated and cleaned to be valid C identifiers (max 10 characters, letters/numbers/underscores only).

### 2. Copy base code (`utils.py`)

The base runtime code for the selected language is copied from `app/templates_<lang>/base_code/` to the output directory. Files matching `*template*` patterns, placeholder files (`sup.c`, `sup.h`, `sup.py`), and `platformio.ini` are excluded — these are either templates or example stubs.

### 3. Build (`descmaker_<lang>_builder.py`)

Each builder fills the language-specific templates with the parsed model data using a custom template engine (`utils.CustomTemplate` with `%$%` delimiters). Generated files include:

| Language | Generated Files |
|----------|----------------|
| **C** | `events.h`, `events.c`, `main.c`, `supervisor_list.h`, `supervisor_list.c`, per-supervisor `.c`/`.h`, `CMakeLists.txt` |
| **Python** | `events.py`, `main.py`, per-supervisor `.py`, `__init__.py` files |
| **ESP-IDF** | Same as C, but organized as ESP-IDF components with individual `CMakeLists.txt` |

### Architecture diagram

```
.wmod file
    │
    ▼
┌─────────────────────┐
│  descmaker_parser   │  Parses XML → supervisors, events, states, transitions
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  app/descmaker.py   │  Orchestrator: copies base_code, selects builder
└────────┬────────────┘
         │
    ┌────┴────┬─────────────┐
    ▼         ▼             ▼
┌───────┐ ┌───────┐ ┌──────────────┐
│ C     │ │Python │ │ ESP-IDF      │
│Builder│ │Builder│ │ Builder      │
└───┬───┘ └───┬───┘ └──────┬───────┘
    ▼         ▼             ▼
  C code   Python code   ESP-IDF code
  (.c/.h)  (.py)         (.c/.h + CMake)
```

---

## Input Format

DEScMaker accepts `.wmod` files — the native XML format of Supremica/Waters. A `.wmod` file contains:

- **Event declarations** (`EventDeclList`) — globally defined events, each with a `Kind` (`CONTROLLABLE` or `UNCONTROLLABLE`) and a `Name`
- **Supervisors** (`SimpleComponent` of kind `SUPERVISOR`) — each containing:
  - **States** (`NodeList` → `SimpleNode`) — automaton states, optionally marked as `Initial`
  - **Transitions** (`EdgeList` → `Edge`) — labeled edges with `Source`, `Target`, and associated event

Events of kind `PROPOSITION` are ignored during parsing. Guard conditions (names starting with `{`) are also skipped.

---

## Output Structure

### C output

```
output/
├── CMakeLists.txt                  # Build configuration
├── README.md                       # Instructions for compiling and running
├── run.sh                          # Build & run script
├── lib/
│   └── supervisor/
│       ├── supervisor.c/h          # Supervisor runtime engine
│       └── sup_debug.h             # Debug macros
└── src/
    ├── main.c                      # Entry point (set actions, trigger events)
    ├── event_handler/
    │   ├── event_handler.c/h       # Event handler runtime
    │   └── events.c/h              # Event declarations
    └── supervisors/
        ├── supervisor_list.c/h     # Linked list of all supervisors
        ├── <sup_name>.c            # Per-supervisor state machine
        └── <sup_name>.h            # Per-supervisor header
```

### Python output

```
output/
├── main.py                         # Entry point (set actions, trigger events)
├── README.md                       # Instructions for customizing and running
└── Supervisor/
    ├── __init__.py                 # Supervisor list and entry points
    ├── events.py                   # Event declarations
    ├── event_handler.py            # Event handler runtime
    ├── logger.py                   # Logging utility (writes log.csv)
    ├── Base/                       # Runtime classes
    │   ├── Event.py                #   Event class
    │   ├── State.py                #   State class
    │   ├── Supervisor.py           #   Supervisor class
    │   └── Transition.py           #   Transition class
    └── supervisors/
        ├── __init__.py             # Supervisor imports
        └── <sup_name>.py           # Per-supervisor state machine
```

### ESP-IDF output

```
output/
├── CMakeLists.txt                  # Top-level CMake
├── sdkconfig                       # ESP-IDF configuration
├── main/
│   ├── CMakeLists.txt
│   └── main.c                      # Entry point
└── components/
    ├── supervisor/                 # Supervisor runtime engine
    │   ├── CMakeLists.txt
    │   ├── supervisor.c/h
    │   └── sup_debug.h
    ├── event_handler/              # Event handler runtime
    │   ├── CMakeLists.txt
    │   ├── event_handler.c/h
    │   └── events.c/h
    └── supervisors/                # Generated supervisors
        ├── CMakeLists.txt
        ├── supervisor_list.c/h
        ├── <sup_name>.c
        └── <sup_name>.h
```

---

## Examples

### Manufacturing System

A complete case study of an automated manufacturing cell, located at `examples/Manufacturing_System/`. It includes:

- **`Manufacturing_System_models.wmod`** — the SCT model with multiple supervisors
- **`Turn_Table.factoryio`** — a Factory I/O 3D simulation scene
- **`code_python/`** — pre-generated Python controllers for each subsystem
- **`factoryIOInterface/`** — Python bridge for connecting to Factory I/O via its SDK
- **`convert_python.py`** — helper script to regenerate the Python code

To regenerate the controllers:
```bash
# From the examples/Manufacturing_System/ directory:
python3 ../../descmaker.py -i Manufacturing_System_models.wmod -o code_python -l python -e
```

### Transmission System

A C-language example at `examples/transmission_system/` demonstrating a communication protocol controller. Includes the generated C source, CMake build, and the supervisor runtime library.

### Other Examples

The `examples/other_examples/` directory contains six additional `.wmod` models covering different SCT scenarios: small factory, labyrinth navigation, synchronous transfer line, assembly table, poultry process, and automotive line.

The `examples/supremica_examples/` directory contains Supremica models used in the published paper, including modular and monolithic versions of a rotary table example, sensor models, and the article's running example.

---

## Citing This Work

If you use DEScMaker in your research, please cite the paper:

**BibTeX:**
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

**APA:**
```
Possato, T., Valentini, J. H., Southier, L. F. P., Barbosa, M. A. C., & Teixeira, M. (2026). DEScMaker: A tool for automated code generation for discrete event systems controllers. Science of Computer Programming, 247, 103350. https://doi.org/10.1016/j.scico.2025.103350
```

**ABNT:**
```
POSSATO, T. et al. DEScMaker: A tool for automated code generation for discrete event systems controllers. Science of Computer Programming, v. 247, p. 103350, jan. 2026. Available at: <https://www.sciencedirect.com/science/article/pii/S0167642325000899>.
```

---

## License

This project is licensed under the **Apache License, Version 2.0** — see the [LICENSE](LICENSE) file for the full text.

---

## Authors

- **Tiago Possato** — UTFPR, IFC — [ORCID](https://orcid.org/0000-0002-9285-4331)
- **João H. Valentini** — UTFPR
- **Luiz F. P. Southier** — UTFPR
- **Marco A. C. Barbosa** — UTFPR
- **Marcelo Teixeira** — UTFPR

Repository: [https://github.com/tiagopossato/descmaker](https://github.com/tiagopossato/descmaker)
