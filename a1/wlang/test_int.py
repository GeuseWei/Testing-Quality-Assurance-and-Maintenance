# The MIT License (MIT)
# Copyright (c) 2016 Arie Gurfinkel

# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import unittest

from . import ast, int, parser


class New_AstVisitor(ast.AstVisitor):
    def __init__(self):
        super(New_AstVisitor, self).__init__()
        self.vars = 0

    # Stm, Exp, Const are the bases
    def visit_Stmt(self, node, *args, **kwargs):
        pass

    def visit_Exp(self, node, *args, **kwargs):
        pass

    def visit_Const(self, node, *args, **kwargs):
        pass

    def visit_AsgnStmt(self, node, *args, **kwargs):
        super(New_AstVisitor, self).visit_AsgnStmt(node, *args, **kwargs)
        self.visit(node.lhs)
        self.visit(node.rhs)
        self.vars += 1


class TestInt(unittest.TestCase):
    # cover ast.py
    def test_Ast(self):
        prg1 = "x := 1"
        ast1 = ast.parse_string(prg1)
        ast1.__repr__()

    def test_Skip(self):
        prg1 = "skip"
        ast1 = ast.parse_string(prg1)
        self.assertEqual(ast1, ast1)
        print(ast1)
        visitor = New_AstVisitor()
        visitor.visit(ast1)

    def test_Asgn(self):
        prg1 = "x := 10"
        ast1 = ast.parse_string(prg1)
        visitor = New_AstVisitor()
        visitor.visit(ast1)

    def test_If(self):
        prg1 = "if 1 < 2 then x := 1 else x := 2"
        ast1 = ast.parse_string(prg1)
        self.assertEqual(ast1, ast1)
        visitor = New_AstVisitor()
        visitor.visit(ast1)

    def test_If2(self):
        prg1 = "x := 1; y := 2; {if x < 0 or y < 0 then x := x - 1 else x := x + 1}; if x < 0 then x := x - 1"
        ast1 = ast.parse_string(prg1)
        print(ast1)
        interp = int.Interpreter()
        st = int.State()
        interp.run(ast1, st)

    def test_While(self):
        prg1 = "while 1 < 2 do x := 1"
        ast1 = ast.parse_string(prg1)
        self.assertEqual(ast1, ast1)
        print(ast1)
        visitor = New_AstVisitor()
        visitor.visit(ast1)

    def test_Assert(self):
        prg1 = "assert 1 > 2"
        ast1 = ast.parse_string(prg1)
        visitor = New_AstVisitor()
        visitor.visit(ast1)
        self.assertEqual(ast1, ast1)
        interp = int.Interpreter()
        print(interp)
        st = int.State()
        interp.run(ast1, st)

    def test_Assume(self):
        prg1 = "assume x < 1"
        ast1 = ast.parse_string(prg1)
        visitor = New_AstVisitor()
        visitor.visit(ast1)
        self.assertEqual(ast1, ast1)
        print(ast1)
        interp = int.Interpreter()
        st = int.State()
        interp.run(ast1, st)

    def test_Havoc(self):
        prg1 = "havoc x, y"
        ast1 = ast.parse_string(prg1)
        visitor = New_AstVisitor()
        visitor.visit(ast1)
        self.assertEqual(ast1, ast1)
        print(ast1)
        interp = int.Interpreter()
        st = int.State()
        interp.run(ast1, st)

    def test_PrintState(self):
        prg1 = "x := 1; print_state"
        ast1 = ast.parse_string(prg1)
        interp = int.Interpreter()
        st = int.State()
        interp.run(ast1, st)

    def test_PrintState2(self):
        prg1 = "print_state"
        ast1 = ast.parse_string(prg1)
        self.assertEqual(ast1, ast1)
        visitor = New_AstVisitor()
        visitor.visit(ast1)

    def test_Exp(self):
        ast1 = ast.Exp(["x := 1", "y := 2"], ["x := 1"])
        ast1.arg(0)
        ast1.is_binary()
        ast1.is_unary()
        print(ast1)

    def test_BExp(self):
        prg1 = "if (not true) and (true) then x:=1"
        ast1 = ast.parse_string(prg1)
        interp = int.Interpreter()
        st = int.State()
        interp.run(ast1, st)

    def test_AExp(self):
        prg1 = "x := 1 * 2 / 3"
        ast1 = ast.parse_string(prg1)
        interp = int.Interpreter()
        st = int.State()
        interp.run(ast1, st)

    def test_Const(self):
        ast1 = ast.Const(1)
        print(ast1)
        ast1.__repr__()
        ast1.__hash__()

    def test_BoolConst(self):
        prg1 = "x := 1 ; if true then x := x - 1 else x := x + 1; if false then x := x + 1"
        ast1 = ast.parse_string(prg1)
        print(ast1)
        interp = int.Interpreter()
        st = int.State()
        interp.run(ast1, st)
        st.__repr__()

    def test_IntVar(self):
        ast1 = ast.IntVar("x")
        print(ast1)
        ast1.__repr__()
        ast1.__hash__()

    def test_parse_file(self):
        file = "wlang/test1.prg"
        ast.parse_file(file)

    def test_PrintVisitor(self):
        visitor = ast.PrintVisitor()
        visitor.visit_PrintStateStmt(ast.SkipStmt())
        print(visitor)

    def test_StmtList(self):
        stmt_list = ast.StmtList(None)
        print(stmt_list)

    # cover remaining int.py
    def test_State(self):
        prg1 = "x := 1; y := 2; skip"
        ast1 = ast.parse_string(prg1)
        interp = int.Interpreter()
        st = int.State()
        interp.run(ast1, st)

    def test_Interpreter(self):
        prg1 = "x := 1; y := 2; z := 1; assert x <= y; assert x = z; assert y >= x"
        ast1 = ast.parse_string(prg1)
        interp = int.Interpreter()
        st = int.State()
        interp.run(ast1, st)

    # cover remaining parser.py
    def test_WhileLangBuffer(self):
        prg1 = "x := 1; while x > 0 inv x > 0 do x := x-1"
        parser.WhileLangBuffer(prg1)

    def test_inv(self):
        prg1 = "x := 1; while x > 0 inv x > 0 do x := x-1"
        ast1 = ast.parse_string(prg1)
        interp = int.Interpreter()
        st = int.State()
        interp.run(ast1, st)

    def test_assert_false(self):
        exp1 = ast.AExp(["+"], [ast.IntConst(1), ast.IntConst(1)])
        rel_exp = ast.RelExp(exp1, "++", exp1)
        interp = int.Interpreter()
        st = int.State()
        interp.visit_RelExp(rel_exp, st)

    def test_WhileLangSemantics(self):
        Sem = parser.WhileLangSemantics()
        prg1 = "x := 1; y := 2"
        ast1 = ast.parse_string(prg1)
        self.assertEquals(Sem.start(ast1), ast1)
        self.assertEquals(Sem.stmt_list(ast1), ast1)
        self.assertEquals(Sem.stmt(ast1), ast1)
        self.assertEquals(Sem.asgn_stmt(ast1), ast1)
        self.assertEquals(Sem.block_stmt(ast1), ast1)
        self.assertEquals(Sem.skip_stmt(ast1), ast1)
        self.assertEquals(Sem.print_state_stmt(ast1), ast1)
        self.assertEquals(Sem.if_stmt(ast1), ast1)
        self.assertEquals(Sem.while_stmt(ast1), ast1)
        self.assertEquals(Sem.assert_stmt(ast1), ast1)
        self.assertEquals(Sem.assume_stmt(ast1), ast1)
        self.assertEquals(Sem.havoc_stmt(ast1), ast1)
        self.assertEquals(Sem.var_list(ast1), ast1)
        self.assertEquals(Sem.bexp(ast1), ast1)
        self.assertEquals(Sem.bterm(ast1), ast1)
        self.assertEquals(Sem.bfactor(ast1), ast1)
        self.assertEquals(Sem.batom(ast1), ast1)
        self.assertEquals(Sem.bool_const(ast1), ast1)
        self.assertEquals(Sem.rexp(ast1), ast1)
        self.assertEquals(Sem.rop(ast1), ast1)
        self.assertEquals(Sem.aexp(ast1), ast1)
        self.assertEquals(Sem.addition(ast1), ast1)
        self.assertEquals(Sem.subtraction(ast1), ast1)
        self.assertEquals(Sem.term(ast1), ast1)
        self.assertEquals(Sem.mult(ast1), ast1)
        self.assertEquals(Sem.division(ast1), ast1)
        self.assertEquals(Sem.factor(ast1), ast1)
        self.assertEquals(Sem.neg_number(ast1), ast1)
        self.assertEquals(Sem.atom(ast1), ast1)
        self.assertEquals(Sem.name(ast1), ast1)
        self.assertEquals(Sem.number(ast1), ast1)
        self.assertEquals(Sem.INT(ast1), ast1)
        self.assertEquals(Sem.NAME(ast1), ast1)
        self.assertEquals(Sem.NEWLINE(ast1), ast1)