cmake_minimum_required(VERSION 3.10)
project("Fuzz Doom" VERSION 1.0.0 LANGUAGES C)

add_definitions(-DBUILD_FOR_FUZZING)
add_subdirectory(chocolate-doom)

set(DOOM_ROOT ${Chocolate\ Doom_SOURCE_DIR})
set(CMAKE_MODULE_PATH "${DOOM_ROOT}/cmake")
find_package(SDL2 2.0.7)
find_package(SDL2_mixer 2.0.2)
find_package(SDL2_net 2.0.0)



add_subdirectory(src)
