set(EXTRA_LIBS textscreen pcsound opl SDL2::SDL2main SDL2::SDL2 SDL2::mixer SDL2::net )

set(DOOM_BINARY_DIR ${Chocolate\ Doom_BINARY_DIR})

set(FREEDOOM_WAD "${PROJECT_SOURCE_DIR}/freedoom-0.12.1/freedoom2.wad")

add_executable(doom_fuzz fuzz_target.c)
target_include_directories(doom_fuzz PRIVATE ${DOOM_BINARY_DIR} ${DOOM_ROOT}/src ${DOOM_ROOT}/src/doom)
target_link_libraries(doom_fuzz PRIVATE game doom ${EXTRA_LIBS} )

# require LLD on Linux. Apple has it's own linker
if(UNIX AND NOT APPLE)
	target_link_libraries(doom_fuzz PRIVATE -fuse-ld=lld)
endif()

target_compile_options(doom_fuzz PRIVATE -fsanitize=fuzzer,address )
target_link_libraries(doom_fuzz PRIVATE -fsanitize=fuzzer,address)
target_compile_definitions(doom_fuzz PRIVATE FREEDOM_WAD="${FREEDOOM_WAD}")

