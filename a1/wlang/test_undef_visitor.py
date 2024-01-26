import unittest

from . import ast, undef_visitor


class TestUndefVisitor(unittest.TestCase):
    def test1(self):
        prg1 = "x := 10; y := x + z"
        ast1 = ast.parse_string(prg1)

        uv = undef_visitor.UndefVisitor()
        uv.check(ast1)
        # UNCOMMENT to run the test
        self.assertEquals({ast.IntVar('z')}, uv.get_undefs())

    def test_if1(self):
        prg1 = "x := 1; if x < 0 then y := 1 else y := 2; z := y + 1 "
        ast1 = ast.parse_string(prg1)
        uv = undef_visitor.UndefVisitor()
        uv.check(ast1)
        self.assertEquals(set(), uv.get_undefs())

    def test_if2(self):
        prg1 = "if x > 0 then y := z"
        ast1 = ast.parse_string(prg1)
        uv = undef_visitor.UndefVisitor()
        uv.check(ast1)
        self.assertEquals({ast.IntVar('z'), ast.IntVar('x')}, uv.get_undefs())

    def test_while(self):
        prg1 = "while x > 0 do x := x + y"
        ast1 = ast.parse_string(prg1)
        uv = undef_visitor.UndefVisitor()
        uv.check(ast1)
        self.assertEquals({ast.IntVar('x'), ast.IntVar('y')}, uv.get_undefs())

    def test_assert(self):
        prg1 = "assert x = 1"
        ast1 = ast.parse_string(prg1)
        uv = undef_visitor.UndefVisitor()
        uv.check(ast1)
        self.assertEquals({ast.IntVar('x')}, uv.get_undefs())

    def test_assume(self):
        prg1 = "assume x > 10"
        ast1 = ast.parse_string(prg1)
        uv = undef_visitor.UndefVisitor()
        uv.check(ast1)
        self.assertEquals({ast.IntVar('x')}, uv.get_undefs())

    def test_havoc(self):
        prg1 = "havoc x, y"
        ast1 = ast.parse_string(prg1)
        uv = undef_visitor.UndefVisitor()
        uv.check(ast1)
        self.assertEquals(set(), uv.get_undefs())

    def test_Visit_Stmt(self):
        ast1 = ast.Stmt()
        uv = undef_visitor.UndefVisitor()
        uv.check(ast1)
