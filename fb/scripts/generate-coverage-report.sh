#!/bin/bash 

# merge all prof files into a single file 
llvm-profdata-10 merge -sparse pf-* -o default.profdata

# export the above file into a format that can be easily parsed
llvm-cov-10 export build/src/fuzz_target2 -instr-profile=default.profdata -format=lcov >> src.info

# generate text report
lcov -a src.info -o src_report.info

# generate a html visualization of the same report
genhtml -o html_output src_report.info

