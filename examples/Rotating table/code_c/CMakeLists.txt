cmake_minimum_required(VERSION 3.15)
project(Supervisor C)

# Set C standard
set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)

# Include directories
include_directories(
    ${CMAKE_CURRENT_SOURCE_DIR}/lib
)

# Source files
set(SOURCE_FILES 
    src/main.c
    src/event_handler/events.c
    src/event_handler/event_handler.c
    src/supervisors/supervisor_list.c
    src/supervisors/supR0EsteiraSensor.c
    src/supervisors/supEsteiraMesa_GiratoriaR1.c
    src/supervisors/supR2Mesa_GiratoriaFuradeira.c
    src/supervisors/supR3Mesa_GiratoriaTeste.c
    src/supervisors/supR4Mesa_GiratoriaRobo.c
    src/supervisors/supR5EsteiraMesa_GiratoriaFuradeira.c
    src/supervisors/supR6Mesa_GiratoriaFuradeiraTeste.c
    src/supervisors/supR7Mesa_GiratoriaTesteRobo.c
    src/supervisors/supR8EsteiraMesa_GiratoriaFuradeiraTeste.c
)

# Add the library
add_subdirectory(lib)
list(APPEND ADDITIONAL_LIBS Supervisor)

# Create the executable
add_executable(supervisor ${SOURCE_FILES})

# Link libraries
target_link_libraries(supervisor ${ADDITIONAL_LIBS})

# Compiler options for warnings
if(CMAKE_C_COMPILER_ID MATCHES "GNU|Clang")
    target_compile_options(supervisor PRIVATE -Wall -Wextra -Wpedantic -Wpadded)
elseif(MSVC)
    target_compile_options(supervisor PRIVATE /W4)
endif()


# Debug and Release build configurations
set(CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG} -g -O0")
set(CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE} -O3")
