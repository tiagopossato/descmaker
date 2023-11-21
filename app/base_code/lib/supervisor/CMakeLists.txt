cmake_minimum_required(VERSION 3.15)
project(Supervisor VERSION 0.1.0 LANGUAGES C)

# Set C standard
set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)

# Create the library
add_library(Supervisor supervisor.c)

# Versioning
set_target_properties(Supervisor PROPERTIES VERSION ${PROJECT_VERSION})
