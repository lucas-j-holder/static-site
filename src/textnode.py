from enum import Enum

class TextType(Enum):
    CODE = "code"
    ITALIC = "italic"
    BOLD = "bold"
    TEXT = "text"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, node):
        return self.text == node.text and self.text_type == node.text_type and self.url == node.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        text = node.text
        split_text = text.split(delimiter)
        if len(split_text) == 1:
            new_nodes.append(node)
        else:
            for i in range(len(split_text)):
                if i % 2 == 0:
                    new_nodes.append(TextNode(split_text[i], node.text_type, None))
                else:
                    new_nodes.append(TextNode(split_text[i], text_type, None))
    return new_nodes