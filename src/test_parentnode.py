import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class Test_ParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
    
    def test_no_children(self):
        node = ParentNode("ol", None, None)
        with self.assertRaises(ValueError) as e:
            node.to_html()
        self.assertTrue("ParentNode requires children." in e.exception.args)

    def test_parentnode_as_child(self):
        node = ParentNode(
            "ol",
            [
                LeafNode("li", "List Item 1"),
                ParentNode("ul", [
                    LeafNode("li", "List Item 2"),
                    LeafNode("li", "List Item 3")
                ])
            ],
        )

        expected_string = "<ol><li>List Item 1</li><ul><li>List Item 2</li><li>List Item 3</li></ul></ol>"

        self.assertEqual(node.to_html(), expected_string)
    
    def test_props(self):
        node = ParentNode(
            "ol",
            [
                LeafNode("li", "List Item 1"),
                ParentNode("ul", [
                    LeafNode("li", "List Item 2"),
                    LeafNode("li", "List Item 3")
                ])
            ],
            props={"style": "color:red"}
        )

        expected_string = "<ol \"style\": \"color:red\" ><li>List Item 1</li><ul><li>List Item 2</li><li>List Item 3</li></ul></ol>"

        self.assertEqual(node.to_html(), expected_string)
    
    def test_children_props(self):
        node = ParentNode(
            "ol",
            [
                LeafNode("li", "List Item 1", {"style": "color:green"}),
                ParentNode("ul", [
                    LeafNode("li", "List Item 2"),
                    LeafNode("li", "List Item 3")
                ],
                props={"style": "color:blue"})
            ],
            props={"style": "color:red"}
        )

        expected_string = "<ol \"style\": \"color:red\" ><li \"style\": \"color:green\" >List Item 1</li><ul \"style\": \"color:blue\" ><li>List Item 2</li><li>List Item 3</li></ul></ol>"

        self.assertEqual(node.to_html(), expected_string)

if __name__ == "__main__":
    unittest.main()