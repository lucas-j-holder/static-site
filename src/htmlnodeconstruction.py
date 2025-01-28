from markdown import block_to_block_type, markdown_to_blocks
from leafnode import LeafNode
from parentnode import ParentNode

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
            children.append(LeafNode("li", line))
    elif tag in ["pre"]:
        for line in lines:
            children.append(LeafNode("code", line))
    if children == []:
        return None
    return children
            

def construct_html_node(tag, block):
    children = block_text_to_children(tag, block)
    value = None
    if children is None:
        value = block
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