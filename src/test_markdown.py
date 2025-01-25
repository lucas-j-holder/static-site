import unittest

from markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_links, text_to_textnodes, markdown_to_blocks
from textnode import TextType, TextNode
    
class Test_spliting_functions(unittest.TestCase):
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

        self.assertEqual(len(nodes), 2)
        self.assertEqual(nodes[0].text_type, TextType.CODE)
        self.assertEqual(nodes[1].text_type, TextType.TEXT)

        self.assertEqual(nodes[0].text, "This is code here")
        self.assertEqual(nodes[1].text, " a test node.")
    
    def test_bold_left(self):
        start_node = TextNode("**This is bold here** a test node.", TextType.TEXT)

        nodes = split_nodes_delimiter([start_node], "**", TextType.BOLD)

        self.assertEqual(len(nodes), 2)
        self.assertEqual(nodes[0].text_type, TextType.BOLD)
        self.assertEqual(nodes[1].text_type, TextType.TEXT)

        self.assertEqual(nodes[0].text, "This is bold here")
        self.assertEqual(nodes[1].text, " a test node.")
    
    def test_italic_left(self):
        start_node = TextNode("*This is italic here* a test node.", TextType.TEXT)

        nodes = split_nodes_delimiter([start_node], "*", TextType.ITALIC)
        self.assertEqual(len(nodes), 2)
        self.assertEqual(nodes[0].text_type, TextType.ITALIC)
        self.assertEqual(nodes[1].text_type, TextType.TEXT)

        self.assertEqual(nodes[0].text, "This is italic here")
        self.assertEqual(nodes[1].text, " a test node.")
    
    def test_italic_right(self):
        start_node = TextNode("This is italic here a *test node.*", TextType.TEXT)

        nodes = split_nodes_delimiter([start_node], "*", TextType.ITALIC)
        self.assertEqual(len(nodes), 2)
        self.assertEqual(nodes[1].text_type, TextType.ITALIC)

        self.assertEqual(nodes[1].text, "test node.")
    
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
    
    def test_split_nodes_image(self):
        expected = [TextNode("TestText", TextType.IMAGE, "test.text.com"), TextNode(" blah blah blah blah ", TextType.TEXT), TextNode("Rick Roll", TextType.IMAGE, "rickastley.com"), TextNode(" ", TextType.TEXT), TextNode("Rick Roll", TextType.IMAGE, "rickastley.com")]
        test_node = [TextNode("![TestText](test.text.com) blah blah blah blah ![Rick Roll](rickastley.com) ![Rick Roll](rickastley.com)", TextType.TEXT)]

        self.assertEqual(expected, split_nodes_image(test_node))

    def test_split_nodes_links(self):
        expected = [TextNode("TestText", TextType.LINK, "test.text.com"), TextNode(" blah blah blah blah ", TextType.TEXT), TextNode("Rick Roll", TextType.LINK, "rickastley.com"), TextNode(" ", TextType.TEXT), TextNode("Rick Roll", TextType.LINK, "rickastley.com")]
        test_node = [TextNode("[TestText](test.text.com) blah blah blah blah [Rick Roll](rickastley.com) [Rick Roll](rickastley.com)", TextType.TEXT)]

        self.assertEqual(expected, split_nodes_links(test_node))

    def test_split_nodes_image_and_links(self):
        expected = [TextNode("TestText", TextType.LINK, "test.text.com"), TextNode(" blah blah blah blah ", TextType.TEXT), TextNode("Rick Roll Image", TextType.IMAGE, "rickastley.com"), TextNode(" ", TextType.TEXT), TextNode("Rick Roll", TextType.LINK, "rickastley.com")]
        test_node = [TextNode("[TestText](test.text.com) blah blah blah blah ![Rick Roll Image](rickastley.com) [Rick Roll](rickastley.com)", TextType.TEXT)]

        self.assertEqual(expected, split_nodes_links(split_nodes_image(test_node)))
        self.assertEqual(expected, split_nodes_image(split_nodes_links(test_node)))
    
    def test_all_as_one(self):
        starting_text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        expected = [
                    TextNode("This is ", TextType.TEXT),
                    TextNode("text", TextType.BOLD),
                    TextNode(" with an ", TextType.TEXT),
                    TextNode("italic", TextType.ITALIC),
                    TextNode(" word and a ", TextType.TEXT),
                    TextNode("code block", TextType.CODE),
                    TextNode(" and an ", TextType.TEXT),
                    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                    TextNode(" and a ", TextType.TEXT),
                    TextNode("link", TextType.LINK, "https://boot.dev"),
                ]

        result = text_to_textnodes(starting_text)

        self.assertEqual(expected, result)


class Test_extract_markdown_images(unittest.TestCase):
    def test_extract_markdown_images(self):
        expected = [("TestText", "test.text.com"), ("Rick Roll", "rickastley.com")]
        test_string = "![TestText](test.text.com) blah blah blah blah ![Rick Roll](rickastley.com)"

        self.assertEqual(expected, extract_markdown_images(test_string))

class Test_extract_markdown_links(unittest.TestCase):
    def test_extract_markdown_links(self):
        expected = [("TestText", "test.text.com"), ("Rick Roll", "rickastley.com")]
        test_string = "[TestText](test.text.com) blah blah blah blah [Rick Roll](rickastley.com) ![Rick Roll](rickastley.com)"

        self.assertEqual(expected, extract_markdown_links(test_string))

class Test_markdown_to_blocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        expected = ['# This is a heading', 'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', '* This is the first list item in a list block\n* This is a list item\n* This is another list item']
        text = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""

        self.assertEqual(expected, markdown_to_blocks(text))

if __name__ == "__main__":
    unittest.main()