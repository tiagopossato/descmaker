cmake_minimum_required(VERSION 3.0.0)
project(Supervisor C)

# add the library
add_subdirectory(lib)
list(APPEND ADDITIONAL_LIBS Supervisor)

set(SOURCE_FILES src/main.c)

list(APPEND SOURCE_FILES src/event_handler/events.c)
list(APPEND SOURCE_FILES src/event_handler/event_handler.c)
list(APPEND SOURCE_FILES src/supervisors/supervisor_list.c)

list(APPEND SOURCE_FILES src/supervisors/sup.c)

add_executable(supervisor ${SOURCE_FILES})
target_link_libraries(supervisor ${ADDITIONAL_LIBS})
