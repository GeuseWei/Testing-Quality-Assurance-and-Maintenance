ASAN_OPTIONS=detect_leaks=0 LLVM_PROFILE_FILE='pf-%p' ./src/doom_fuzz -runs=10 -use-value-profile=1 -jobs=100 -workers=8  -detect_leaks=0 >/dev/null
