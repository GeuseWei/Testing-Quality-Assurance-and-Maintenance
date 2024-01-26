# REPORT

## Personal Information
- Student Name: Zhijun Wei
- Student ID: 21027550
- WatID: z29wei

## What have been done to compile and run the code
1. Install the docker on Macbook, and connect the docker with VS code.
2. Clone the Chocolate-Doom and the provided fuzzing target, and build them.
3. Create the CORPUS and SEED folder under build to ensure the fuzz target could run properly.
4. Follow the instructions on how to run the fuzz target and generate the coverage report.

## What have been done to increase the coverage
1. First add the wad file to the SEED folder. I tried the provided file freedoom2.wad and some other wad files from the internet, each of them can increase the coverage if they are added to the SEED folder. However the difference in the amount of increase between different wad files is not significant, so I finally chose the provided file freedoomq2.wad as the seed. By this method, the coverage of w_wad.c increased to 70% and the coverage of p_setup.c increased to 82.3%. 
2. To achieve higher coverage, I modified fuzz_traget.c, line 209, to char *filename = "~fuzz.wadas". In this way, more lines in the w_wad.c can be covered, more specifically, lines 118-132 and lines 144-161 are covered now. In this way, the coverage of w_wad.c increased to 84.4%. Now both w_wad.c and p_setup.c have coverage of more than 79%.

## What bugs have been found? Can you replay the bug with chocolate-doom, not with the fuzz target?
```
Direct leak of 72 byte(s) in 10 object(s) allocated from:
    #0 0x434954 in strdup (/home/doom/stqam/fb/build/src/doom_fuzz+0x434954)
    #1 0x4dc080 in M_StringDuplicate /home/doom/stqam/fb/build/../chocolate-doom/src/m_misc.c:423:14
    #2 0x4a10c4 in SetVariable /home/doom/stqam/fb/build/../chocolate-doom/src/m_config.c:1942:32
    #3 0x4a0512 in LoadDefaultCollection /home/doom/stqam/fb/build/../chocolate-doom/src/m_config.c:2031:9
    #4 0x477ec6 in LLVMFuzzerTestOneInput /home/doom/stqam/fb/build/../src/fuzz_target.c:167:3
    #5 0x382a51 in fuzzer::Fuzzer::ExecuteCallback(unsigned char const*, unsigned long) (/home/doom/stqam/fb/build/src/doom_fuzz+0x382a51)
    #6 0x38478a in fuzzer::Fuzzer::ReadAndExecuteSeedCorpora(std::__Fuzzer::vector<fuzzer::SizedFile, fuzzer::fuzzer_allocator<fuzzer::SizedFile> >&) (/home/doom/stqam/fb/build/src/doom_fuzz+0x38478a)
    #7 0x384e19 in fuzzer::Fuzzer::Loop(std::__Fuzzer::vector<fuzzer::SizedFile, fuzzer::fuzzer_allocator<fuzzer::SizedFile> >&) (/home/doom/stqam/fb/build/src/doom_fuzz+0x384e19)
    #8 0x372e9e in fuzzer::FuzzerDriver(int*, char***, int (*)(unsigned char const*, unsigned long)) (/home/doom/stqam/fb/build/src/doom_fuzz+0x372e9e)
    #9 0x39c932 in main (/home/doom/stqam/fb/build/src/doom_fuzz+0x39c932)
    #10 0x7f8a28958bf6 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21bf6)
```
If we did not instruct AddressSanitizer to disregard the leak, we will get the message above. However, these messages are benign because the fuzz target leaks memory on exit.

## Did you manage to compile the game and play it on your local machine (Not inside Docker)?
Yes. I installed chocolate doom on my Macbook and ran the freedoom2.wad file. The screenshot is attached to the report folder.