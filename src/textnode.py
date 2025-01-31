from enum import Enum
import re

class TextType(Enum):
    CODE = "code"
    ITALIC = "italic"
    BOLD = "bold"
    TEXT = "text"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text: str, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, node):
        return self.text == node.text and self.text_type == node.text_type and self.url == node.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    

