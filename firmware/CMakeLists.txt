cmake_minimum_required(VERSION 3.22)

file(STRINGS "${CMAKE_CURRENT_LIST_DIR}/../VERSION" ESPTELEPATHY_PROJECT_VERSION LIMIT_COUNT 1)
if(NOT ESPTELEPATHY_PROJECT_VERSION)
    message(FATAL_ERROR "VERSION is missing or empty")
endif()
set(PROJECT_VER "${ESPTELEPATHY_PROJECT_VERSION}")

include($ENV{IDF_PATH}/tools/cmake/project.cmake)
idf_build_set_property(MINIMAL_BUILD ON)
project(esptelepathy)
