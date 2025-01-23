import unittest

from textnode import TextType, TextNode, split_nodes_delimiter

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node.", text_type=TextType.BOLD)
        node2 = TextNode("This is a text node.", text_type=TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("This is a text node.", text_type=TextType.BOLD)
        node2 = TextNode("This is not the same text node.", text_type=TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_repr(self):
        node = TextNode("This is a text node.", text_type=TextType.BOLD)

        self.assertEqual(node.__repr__(), "TextNode(This is a text node., bold, None)")
    
    def test_default_url(self):
        node = TextNode("TestNode", TextType.BOLD)

        self.assertEqual(node.url, None)
    
    def test_texttype_values(self):
        url = TextNode("TEST", TextType.LINK)
        image = TextNode("TEST", TextType.IMAGE)
        normal = TextNode("TEST", TextType.TEXT)
        bold = TextNode("TEST", TextType.BOLD)
        italic = TextNode("TEST", TextType.ITALIC)
        code = TextNode("TEST", TextType.CODE)

        self.assertEqual(url.__repr__(), "TextNode(TEST, link, None)")
        self.assertEqual(image.__repr__(), "TextNode(TEST, image, None)")
        self.assertEqual(normal.__repr__(), "TextNode(TEST, text, None)")
        self.assertEqual(bold.__repr__(), "TextNode(TEST, bold, None)")
        self.assertEqual(italic.__repr__(), "TextNode(TEST, italic, None)")
        self.assertEqual(code.__repr__(), "TextNode(TEST, code, None)")
    
class Test_split_nodes_delimiter(unittest.TestCase):
    def test_code(self):
        start_node = TextNode("This is `code here` a test node.", TextType.TEXT)

        nodes = split_nodes_delimiter([start_node], "`", TextType.CODE)

        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text_type, TextType.CODE)
        self.assertEqual(nodes[2].text_type, TextType.TEXT)

        self.assertEqual(nodes[0].text, "This is ")
        self.assertEqual(nodes[1].text, "code here")
        self.assertEqual(nodes[2].text, " a test node.")
    
    def test_bold(self):
        start_node = TextNode("This is **bold here** a test node.", TextType.TEXT)

        nodes = split_nodes_delimiter([start_node], "**", TextType.BOLD)

        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text_type, TextType.BOLD)
        self.assertEqual(nodes[2].text_type, TextType.TEXT)

        self.assertEqual(nodes[0].text, "This is ")
        self.assertEqual(nodes[1].text, "bold here")
        self.assertEqual(nodes[2].text, " a test node.")
    
    def test_italic(self):
        start_node = TextNode("This is *italic here* a test node.", TextType.TEXT)

        nodes = split_nodes_delimiter([start_node], "*", TextType.ITALIC)

        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text_type, TextType.ITALIC)
        self.assertEqual(nodes[2].text_type, TextType.TEXT)

        self.assertEqual(nodes[0].text, "This is ")
        self.assertEqual(nodes[1].text, "italic here")
        self.assertEqual(nodes[2].text, " a test node.")

    def test_code_left(self):
        start_node = TextNode("`This is code here` a test node.", TextType.TEXT)

        nodes = split_nodes_delimiter([start_node], "`", TextType.CODE)

        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[1].text_type, TextType.CODE)
        self.assertEqual(nodes[2].text_type, TextType.TEXT)

        self.assertEqual(nodes[1].text, "This is code here")
        self.assertEqual(nodes[2].text, " a test node.")
    
    def test_bold_left(self):
        start_node = TextNode("**This is bold here** a test node.", TextType.TEXT)

        nodes = split_nodes_delimiter([start_node], "**", TextType.BOLD)

        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[1].text_type, TextType.BOLD)
        self.assertEqual(nodes[2].text_type, TextType.TEXT)

        self.assertEqual(nodes[1].text, "This is bold here")
        self.assertEqual(nodes[2].text, " a test node.")
    
    def test_italic_left(self):
        start_node = TextNode("*This is italic here* a test node.", TextType.TEXT)

        nodes = split_nodes_delimiter([start_node], "*", TextType.ITALIC)
        print(nodes)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[1].text_type, TextType.ITALIC)
        self.assertEqual(nodes[2].text_type, TextType.TEXT)

        self.assertEqual(nodes[1].text, "This is italic here")
        self.assertEqual(nodes[2].text, " a test node.")
    
    def test_italic_right(self):
        start_node = TextNode("This is italic here a *test node.*", TextType.TEXT)

        nodes = split_nodes_delimiter([start_node], "*", TextType.ITALIC)
        print(nodes)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[1].text_type, TextType.ITALIC)
        self.assertEqual(nodes[2].text_type, TextType.TEXT)

        self.assertEqual(nodes[1].text, "test node.")
        self.assertEqual(nodes[2].text, "")
    
    def test_italic_multiple(self):
        start_node = TextNode("This *is* italic *here* a *test* node.", TextType.TEXT)

        nodes = split_nodes_delimiter([start_node], "*", TextType.ITALIC)
        self.assertEqual(len(nodes), 7)
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text_type, TextType.ITALIC)
        self.assertEqual(nodes[2].text_type, TextType.TEXT)
        self.assertEqual(nodes[3].text_type, TextType.ITALIC)
        self.assertEqual(nodes[4].text_type, TextType.TEXT)
        self.assertEqual(nodes[5].text_type, TextType.ITALIC)
        self.assertEqual(nodes[6].text_type, TextType.TEXT)

        self.assertEqual(nodes[0].text, "This ")
        self.assertEqual(nodes[1].text, "is")
        self.assertEqual(nodes[2].text, " italic ")
        self.assertEqual(nodes[3].text, "here")
        self.assertEqual(nodes[4].text, " a ")
        self.assertEqual(nodes[5].text, "test")
        self.assertEqual(nodes[6].text, " node.")


if __name__ == "__main__":
    unittest.main()