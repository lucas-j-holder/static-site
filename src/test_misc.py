from htmlnodeconstruction import text_nodes_to_html_nodes
from textnode import TextNode, TextType
from leafnode import LeafNode
import unittest

class Test_text_nodes_to_html_nodes(unittest.TestCase):

    def test_text(self):
        textnode = [TextNode("This is a test node.", TextType.TEXT, None)]
        node = text_nodes_to_html_nodes(textnode)

        expected_string = "This is a test node."

        self.assertEqual(node[0].to_html(), expected_string)
    
    def test_bold(self):
        textnode = [TextNode("This is a test node.", TextType.BOLD, None)]
        node = text_nodes_to_html_nodes(textnode)

        expected_string = "<b>This is a test node.</b>"

        self.assertEqual(node[0].to_html(), expected_string)
    
    def test_italic(self):
        textnode = [TextNode("This is a test node.", TextType.ITALIC, None)]
        node = text_nodes_to_html_nodes(textnode)

        expected_string = "<i>This is a test node.</i>"

        self.assertEqual(node[0].to_html(), expected_string)

    def test_code(self):
        textnode = [TextNode("This is a test node.", TextType.CODE, None)]
        node = text_nodes_to_html_nodes(textnode)

        expected_string = "<code>This is a test node.</code>"

        self.assertEqual(node[0].to_html(), expected_string)
    
    def test_link(self):
        textnode = [TextNode("This is a test node.", TextType.LINK, "www.test.test")]
        node = text_nodes_to_html_nodes(textnode)

        expected_string = "<a href=\"www.test.test\" >This is a test node.</a>"

        self.assertEqual(node[0].to_html(), expected_string)

    def test_image(self):
        textnode = [TextNode("This is a test node.", TextType.IMAGE, "path/to/image.jpg")]
        node = text_nodes_to_html_nodes(textnode)

        expected_string = "<img href=\"path/to/image.jpg\" alt=\"This is a test node.\" ></img>"

        self.assertEqual(node[0].to_html(), expected_string)
    
if __name__ == "__main__":
    unittest.main()