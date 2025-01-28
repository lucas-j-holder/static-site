import unittest
from htmlnodeconstruction import markdown_to_html_node
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode

class Test_HTMLNodeConstruction(unittest.TestCase):
    def test_props_to_html(self):
        markdown = """
# This is a heading

```This is a code block.```

> Blockquote time!
> Bois!

* Unordered list
- list unordered
* ul time.

1. Ordered list
2. List item 2
3. list time again?

###### Header 6 time.
"""

        nodes = markdown_to_html_node(markdown)

        expected = ParentNode("div", [
            LeafNode("h1", "# This is a heading"),
            ParentNode("pre", [
                LeafNode("code", "```This is a code block.```")
            ]),
            LeafNode("blockquote", """> Blockquote time!
> Bois!"""),
            ParentNode("ul",[
                LeafNode("li", "* Unordered list"),
                LeafNode("li", "- list unordered"),
                LeafNode("li", "* ul time.")
            ]),
            ParentNode("ol", [
                LeafNode("li", "1. Ordered list"),
                LeafNode("li", "2. List item 2"),
                LeafNode("li", "3. list time again?"),
        ]),
            LeafNode("h6", "###### Header 6 time.")
        ])
        self.assertEqual(len(nodes.children), len(expected.children))
        for i in range(len(nodes.children)):
            self.assertEqual(nodes.children[i], expected.children[i])
        self.assertEqual(nodes, expected)

if __name__ == "__main__":
    unittest.main()