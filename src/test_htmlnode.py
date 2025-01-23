import unittest
from htmlnode import HTMLNode

class Test_HTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(tag = "img", props = {"href": "path/to/img.jpg"})
        node2 = HTMLNode(tag = "a", value="Test Link", props={"href": "www.test.test", "target": "_blank"})
        self.assertEqual(node.props_to_html(), "\"href\": \"path/to/img.jpg\" ")
        self.assertEqual(node2.props_to_html(), "\"href\": \"www.test.test\" \"target\": \"_blank\" ")
    def test_repr(self):
        node = HTMLNode(tag = "a", value="Test Link")
        self.assertEqual(node.__repr__(), "HTMLNode(a, Test Link, None, None)")