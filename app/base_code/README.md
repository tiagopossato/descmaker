# Test Case

To compile and run use: `./run.sh`

## ESP32 with ESP-IDF
# 

- Move library ```supervisor``` to folder ```components```.
- Change ```components/supervisor/CMakeLists.txt``` content to:

```cmake
idf_component_register(SRCS "supervisor.c"
                    INCLUDE_DIRS ".")
```

- Move ```src/supervisors``` to ```components/supervisors```.

- Change ```components/supervisors/CMakeLists.txt``` content to:

```cmake
idf_component_register(SRCS "events.c" "handle_event.c" "sup.c"
                    INCLUDE_DIRS "."
                    REQUIRES supervisor)
```
- Remember to add every supervisor C file to ```SRCS``` variable.

- Change all includes that point to ```../../lib/supervisor/supervisor.h``` to ```supervisor```.

- Remove all occurrences of ```supervisors/``` in main file includes. 

- The final folder structure should be like this:

```bash
.
├── components
│   ├── supervisor
│   │   ├── CMakeLists.txt
│   │   ├── sup_debug.h
│   │   ├── supervisor.c
│   │   └── supervisor.h
│   └── supervisors
│       ├── CMakeLists.txt
│       ├── events.c
│       ├── events.h
│       ├── handle_event.c
│       ├── handle_event.h
│       ├── sup.c
│       └── sup.h
├── main
│   ├── CMakeLists.txt
│   └── main.c
└── CMakeLists.txt
```

## ESP32 with PlatformIO

To use with PlatformIO, comment the main function in `main.c` and rename `main.c` to `main.cpp`. 


# Files structure
```
|-- generated_code
|  |-- lib
|  |  |-- supervisor
|  |  |  |-- supervisor.c
|  |  |  |-- supervisor.h
|  |  |  |-- sup_debug.h
|  |  |  |-- CMakeLists.txt
|  |  |  |-- README.md
|  |  |-- CMakeLists.txt
|  |-- src
|  |  |-- supervisors
|  |  |  |-- events.c
|  |  |  |-- events.h
|  |  |  |-- handle_event.c
|  |  |  |-- handle_event.h
|  |  |  |-- [sup's].c
|  |  |  |-- [sup's].h
|  |  |-- main.c
|  |-- CMakeLists.txt
|  |-- platformio.ini
|  |-- README.md
|  |-- run.sh
```