from main import text_node_to_html_node
from textnode import TextNode, TextType
from leafnode import LeafNode
import unittest

class Test_text_node_to_html_node(unittest.TestCase):

    def test_text(self):
        textnode = TextNode("This is a test node.", TextType.TEXT, None)
        node = text_node_to_html_node(textnode)

        expected_string = "This is a test node."

        self.assertEqual(node.to_html(), expected_string)
    
    def test_bold(self):
        textnode = TextNode("This is a test node.", TextType.BOLD, None)
        node = text_node_to_html_node(textnode)

        expected_string = "<b>This is a test node.</b>"

        self.assertEqual(node.to_html(), expected_string)
    
    def test_italic(self):
        textnode = TextNode("This is a test node.", TextType.ITALIC, None)
        node = text_node_to_html_node(textnode)

        expected_string = "<i>This is a test node.</i>"

        self.assertEqual(node.to_html(), expected_string)

    def test_code(self):
        textnode = TextNode("This is a test node.", TextType.CODE, None)
        node = text_node_to_html_node(textnode)

        expected_string = "<code>This is a test node.</code>"

        self.assertEqual(node.to_html(), expected_string)
    
    def test_link(self):
        textnode = TextNode("This is a test node.", TextType.LINK, "www.test.test")
        node = text_node_to_html_node(textnode)

        expected_string = "<a \"href\": \"www.test.test\" >This is a test node.</a>"

        self.assertEqual(node.to_html(), expected_string)

    def test_image(self):
        textnode = TextNode("This is a test node.", TextType.IMAGE, "path/to/image.jpg")
        node = text_node_to_html_node(textnode)

        expected_string = "<img \"href\": \"path/to/image.jpg\" \"alt\": \"This is a test node.\" ></img>"

        self.assertEqual(node.to_html(), expected_string)
    
if __name__ == "__main__":
    unittest.main()