import unittest

from . import token_with_escape


class CoverageTests(unittest.TestCase):

    def test_1(self):
        """Node Coverage but not Edge Coverage"""
        # YOUR CODE HERE
        # Cover node1, node2, node3, node4, node5
        self.assertEqual(token_with_escape("^a"), ["a"])
        # Cover node1, node2, node3, node4, node6, node7
        self.assertEqual(token_with_escape("a|"), ["a", ""])
        # Cover node1, node2, node3, node4, node6, node8
        self.assertEqual(token_with_escape("a"), ["a"])
        # Cover node1, node2, node3,node9, node10
        self.assertEqual(token_with_escape("^^"), ["^"])
        # Cover node1, node2, node11
        self.assertEqual(token_with_escape(""), [""])

    def test_2(self):
        """Edge Coverage but not Edge Pair Coverage"""
        # YOUR CODE HERE
        # In this test case, we traverse all the edges, but not all edge pairs,
        self.assertEqual(token_with_escape('a|b^c'), ['a', 'bc'])
        # For example, the edge pair (node10, node2, node3) is not included in this test case.

    def test_3(self):
        """Edge Pair Coverage but not Prime Path Coverage"""
        # YOUR CODE HERE
        # Cover 1-2-3-4-5-2-3-9-10-2-11
        self.assertEqual(token_with_escape('^a'), ['a'])
        # Cover 1-2-3-4-5-2-3-9-10-2-3-4-6-8-2-11
        self.assertEqual(token_with_escape('^ab'), ['ab'])
        # Cover 1-2-3-4-6-8-2-3-4-6-7-2-11
        self.assertEqual(token_with_escape('|^'), ['', ''])
        # Cover 1-2-3-4-5-2-3-9-10-2-11
        self.assertEqual(token_with_escape('a|'), ['a', ''])
        # Now we have traversed all the edge pairs, but not all prime paths.
        # For example, the prime path (node8, node2, node3, node4, node6, node8) is not included in this test case.
