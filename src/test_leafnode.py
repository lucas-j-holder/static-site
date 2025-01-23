import unittest
from leafnode import LeafNode

class Test_LeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("a", "This is a test node.")

        text = node.to_html()
        self.assertEqual(text, "<a >This is a test node.</a>")

        node2 = LeafNode(None, "This is a tagless node.")
        text2 = node2.to_html()
        self.assertEqual(text2, "This is a tagless node.")
