import unittest

from textnode import TextType, TextNode

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
    
if __name__ == "__main__":
    unittest.main()