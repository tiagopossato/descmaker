cmake_minimum_required(VERSION 3.15)
project(Supervisor C)

# Set C standard
set(CMAKE_C_STANDARD 99)
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
    src/supervisors/supervisor.c
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
