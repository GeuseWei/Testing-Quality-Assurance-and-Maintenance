# While Language

A runtime and symbolic execution engine for a small imperative language called WHILE. 

The language is very simple and includes only integer variables, basic
statements, control flow, and loops. There are no functions, references, or
dynamic memory.

## Installation Instructions

A virtual environment is highly recommended

```
$ python3 -m venv $(pwd)/venv
$ . ./venv/activate
```

Install required packages
```
$ pip3 install -r requirements.txt
```

Run tests
```
$ python3 -m wlang.test
```

## Code structure

Key components of the code are described below:
```
wlang/
├── ast.py                    Abstract Syntax Tree (AST)
├── int.py                    Interpreter (execution engine)
├── parser.py                 Parser (generated from while.ebnf using tatsu)
├── semantics.py              Converts parser actions to AST
├── stats_visitor.py          Visitor to compute statistics over a program AST
├── stmt_counter.py           Visitor to count number of statements in a program AST
├── sym.py                    Symbolic execution engine
├── test.py                   Test driver. Run with python -m wlang.test
├── test_int.py               Tests for the interpreter
├── test_parser.py            Tests for the parser
├── test_stats_visitor.py     Tests from stats_visitor
├── test_sym.py               Tests for symbolic execution engine
├── test_undef_visitor.py     Tests for undef_visitor
├── test_util.py              Tests for util package
├── undef_visitor.py          Visitor to compute all variables that are used unassigned
├── util.py                   Utlility functions
├── while.ebnf                Grammar for tatsu to generaet parser.py
├── while.lean.ebnf           Readable version of the grammar
└── while.svg                 Pictorial representation of the grammar
```

## Generate parser

This step is only necessary if you change something in the grammar file (`whiel.ebnf`). To generate new `parser.py` follow the following:
```
$ tatsu -o parser.py while.ebnf
```

To generate pretty-printed version of the grammar:
```
$ tatsu --pretty-lean while.ebnf > while.lean.ebnf
```

To generate SVG version of the grammar:
```
$ tatsu --draw -o while.svg while.ebnf
```
