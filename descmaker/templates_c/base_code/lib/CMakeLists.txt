cmake_minimum_required(VERSION 3.15)
project(Supervisor VERSION 0.1.0 LANGUAGES C)

# Set C standard
set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)

add_subdirectory(supervisor)

# Versioning
set_target_properties(Supervisor PROPERTIES VERSION ${PROJECT_VERSION})

# If Supervisor library has a CMakeLists.txt, set properties there
if(TARGET Supervisor)
    set_target_properties(Supervisor PROPERTIES
        C_STANDARD 11
        C_STANDARD_REQUIRED ON
    )
endif()