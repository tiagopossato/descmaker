cmake_minimum_required(VERSION 3.15)
project(supervisorTester C)

# Set C standard
set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)

# Source files
set(SOURCE_FILES 
    src/main.c
    src/event_handler/events.c
    src/event_handler/event_handler.c
    src/supervisors/supervisor_list.c
    src/supervisors/sup.c
)

# Include directories
include_directories(
    ${CMAKE_CURRENT_SOURCE_DIR}/lib
)

# Add the library
add_subdirectory(lib)
list(APPEND ADDITIONAL_LIBS supervisorTester)

# Link directories
link_directories(${CMAKE_CURRENT_SOURCE_DIR}/lib)

# Create the executable
add_executable(supervisorTester ${SOURCE_FILES})

# Link libraries
target_link_libraries(supervisorTester ${ADDITIONAL_LIBS})

# Compiler options for warnings
if(CMAKE_C_COMPILER_ID MATCHES "GNU|Clang")
    target_compile_options(supervisorTester PRIVATE -Wall -Wextra -Wpedantic -Wpadded)
elseif(MSVC)
    target_compile_options(supervisorTester PRIVATE /W4)
endif()

# Debug and Release build configurations
set(CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG} -g -O0")
set(CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE} -O3")

