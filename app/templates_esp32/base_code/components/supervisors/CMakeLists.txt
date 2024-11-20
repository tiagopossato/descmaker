idf_component_register(SRCS "sup.c" "supervisor_list.c"
                    INCLUDE_DIRS "."
                    REQUIRES supervisor event_handler)
