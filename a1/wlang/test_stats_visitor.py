import unittest

from . import ast, stats_visitor


class TestStatsVisitor(unittest.TestCase):
    # test Stmt, StmtList, AsgnStmt
    def test_Stmt(self):
        prg1 = "x := 1; y := -1"
        ast1 = ast.parse_string(prg1)
        sv = stats_visitor.StatsVisitor()
        sv.visit(ast1)
        self.assertEquals(sv.get_num_stmts(), 2)
        self.assertEquals(sv.get_num_vars(), 2)

    def test_if1(self):
        prg1 = "x := 1; if x > 0 then y := 1 else y := 2"
        ast1 = ast.parse_string(prg1)
        sv = stats_visitor.StatsVisitor()
        sv.visit(ast1)
        self.assertEquals(sv.get_num_stmts(), 4)
        self.assertEquals(sv.get_num_vars(), 2)

    def test_if2(self):
        prg1 = "x := 1; if x > 0 then y := z + 1"
        ast1 = ast.parse_string(prg1)
        sv = stats_visitor.StatsVisitor()
        sv.visit(ast1)
        self.assertEquals(sv.get_num_stmts(), 3)
        self.assertEquals(sv.get_num_vars(), 3)

    def test_while(self):
        prg1 = "x := 1; while x > 0 do y := 2"
        ast1 = ast.parse_string(prg1)
        sv = stats_visitor.StatsVisitor()
        sv.visit(ast1)
        self.assertEquals(sv.get_num_stmts(), 3)
        self.assertEquals(sv.get_num_vars(), 2)

    def test_assert(self):
        prg1 = "assert x > y"
        ast1 = ast.parse_string(prg1)
        sv = stats_visitor.StatsVisitor()
        sv.visit(ast1)
        self.assertEquals(sv.get_num_stmts(), 1)
        self.assertEquals(sv.get_num_vars(), 2)

    def test_assume(self):
        prg1 = "assume x = 10"
        ast1 = ast.parse_string(prg1)
        sv = stats_visitor.StatsVisitor()
        sv.visit(ast1)
        self.assertEquals(sv.get_num_stmts(), 1)
        self.assertEquals(sv.get_num_vars(), 1)

    def test_havoc(self):
        prg1 = "havoc x, y"
        ast1 = ast.parse_string(prg1)
        sv = stats_visitor.StatsVisitor()
        sv.visit(ast1)
        self.assertEquals(sv.get_num_stmts(), 1)
        self.assertEquals(sv.get_num_vars(), 2)
