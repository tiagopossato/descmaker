# Test Case

To compile and run use: `./run.sh`

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

# Visual explanation

![Visual explanation](https://github.com/tiagopossato/descmaker/blob/main/docs/visual_readme.drawio.svg?raw=true