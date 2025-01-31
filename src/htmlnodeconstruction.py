from markdown import block_to_block_type, markdown_to_blocks, text_to_textnodes
from leafnode import LeafNode
from parentnode import ParentNode
from textnode import TextNode, TextType
import re

def text_nodes_to_html_nodes(text_nodes:list[TextNode]):
    nodes = []
    for text_node in text_nodes:
        match text_node.text_type:
            case TextType.TEXT:
                nodes.append(LeafNode(None, text_node.text))
            case TextType.BOLD:
                nodes.append(LeafNode("b", text_node.text))
            case TextType.ITALIC:
                nodes.append(LeafNode("i", text_node.text))
            case TextType.CODE:
                nodes.append(LeafNode("code", text_node.text))
            case TextType.LINK:
                nodes.append(LeafNode("a", text_node.text, {"href": text_node.url}))
            case TextType.IMAGE:
                nodes.append(LeafNode("img", "", {"href": text_node.url, "alt": text_node.text}))
            case _:
                raise ValueError("TextNode has invalid TextType.")
    return nodes

def get_html_tag(block):
    block_type = block_to_block_type(block)
        
    tag = ""
    if "heading" in block_type: tag = f"h{block_type[-1]}"
    match block_type:
        case "code":
            tag = "pre"
        case "unordered list":
            tag = "ul"
        case "ordered list":
            tag = "ol"
        case "quote":
            tag = "blockquote"
        case "paragraph":
            tag = "p"
    return tag

def block_text_to_children(tag, block):
    lines = block.split("\n")
    children = []
    if tag in ["ul", "ol"]:
        for line in lines:
            text_nodes = text_to_textnodes(" ".join(line.split(" ")[1:]))
            value = text_nodes_to_html_nodes(text_nodes)
            new_line = ""
            for node in value:
                new_line += node.to_html()
            children.append(LeafNode("li", new_line))
    elif tag in ["pre"]:
        code_regex = re.compile(r"^`{3}(.+)`{3}$", re.S)
        matches = code_regex.match(block)
        lines = matches.group(1).split("\n")
        for line in lines:
            children.append(LeafNode("code", line + "<br>"))
    elif tag in ["p"]:
        text_nodes = text_to_textnodes(lines[0])
        children = text_nodes_to_html_nodes(text_nodes)
    if children == []:
        return None
    return children
            

def construct_html_node(tag, block):
    children = block_text_to_children(tag, block)
    value = None
    if children is None:
        value = block
        if tag in ["h1","h2","h3","h4","h5","h6","blockquote"]:
            value = " ".join(value.split(" ")[1:])
        node = LeafNode(tag, value, children)
    else:
        node = ParentNode(tag, children)
    return node
    

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        tag = get_html_tag(block)

        nodes.append(construct_html_node(tag, block))
    node = ParentNode("div", nodes)
    return node

if __name__ == "__main__":
    markdown = """
# This is a heading

```This is a code block.```

> Blockquote time!
> Bois!

* Unordered list
- list unordered
* guess what? ul time.

1. Ordered list
2. List item 2
3. Wtf, list time again?

###### Header 6 time.
"""

    print(markdown_to_html_node(markdown))