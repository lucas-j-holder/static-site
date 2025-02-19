import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        text = node.text
        split_text = text.split(delimiter)
        if len(split_text) == 1:
            new_nodes.append(node)
        else:
            for i in range(len(split_text)):
                if split_text[i] == "": continue
                if i % 2 == 0:
                    new_nodes.append(TextNode(split_text[i], node.text_type, None))
                else:
                    new_nodes.append(TextNode(split_text[i], text_type, None))
    return new_nodes

def extract_markdown_images(text):
    regex_string = r"!\[(.*?)\]\((.*?)\)"
    tuples = []
    regex = re.compile(regex_string)
    matches = regex.findall(text)
    if len(matches) == 0: return tuples

    for match in matches:
        tuples.append((match[0], match[1]))
    
    return tuples
    
def extract_markdown_links(text):
    regex_string = r"(?<!!)\[(.*?)\]\((.*?)\)"
    tuples = []
    regex = re.compile(regex_string)
    matches = regex.findall(text)
    if len(matches) == 0: return tuples

    for match in matches:
        tuples.append((match[0], match[1]))
    
    return tuples

def split_nodes_text_object(old_nodes: list[TextNode], extract_function, new_texttype:TextType, split_string_function):
    new_nodes = []
    for node in old_nodes:
        text = node.text
        tuples = extract_function(text)
        if len(tuples) == 0: new_nodes.append(node); continue
        for tuple in tuples:
            split_string = split_string_function(tuple[0], tuple[1])
            text_split = text.split(split_string, 1)
            if text_split[0] != "": new_nodes.append(TextNode(text_split[0], node.text_type))
            text = text_split[1]
            new_nodes.append(TextNode(tuple[0], new_texttype, tuple[1]))
        if text != "" and node.text_type not in [TextType.IMAGE, TextType.LINK]: new_nodes.append(TextNode(text, node.text_type))
    return new_nodes

def split_nodes_image(old_nodes: list[TextNode]):
    return split_nodes_text_object(old_nodes, extract_markdown_images, TextType.IMAGE, lambda a, b: f"![{a}]({b})")

def split_nodes_links(old_nodes: list[TextNode]):
    return split_nodes_text_object(old_nodes, extract_markdown_links, TextType.LINK, lambda a, b: f"[{a}]({b})")

def text_to_textnodes(text):
    start_node = [TextNode(text, TextType.TEXT)]
    return split_nodes_links(split_nodes_image(split_nodes_delimiter(split_nodes_delimiter(split_nodes_delimiter(start_node, "**", TextType.BOLD), "*", TextType.ITALIC), "`", TextType.CODE)))

def markdown_to_blocks(markdown):
    markdown_lines = markdown.split("\n")
    blocks = []
    block = ""

    for line in markdown_lines:
        if line == "":
            if block != "":
                blocks.append(block.strip())
                block = ""
            else:
                continue
        else:
            block += line + "\n"
    if block != "":
        blocks.append(block.strip())
    return blocks



def block_to_block_type(block):
    lines = block.split("\n")
    heading_regex = re.compile(r"^#{1,6} ")
    code_regex = re.compile(r"^`{3}.+`{3}$", re.S)
    unordered_regex = re.compile(r"^[\*-] ")
    if heading_regex.match(block): return f"heading {heading_regex.match(block).end() - 1}"
    if code_regex.match(block): return "code"
    quote = True
    for line in lines:
        if len(line) == 0: quote = False; break
        if line[0] != ">": quote = False; break
    if quote: return "quote"
    if unordered_regex.match(block):
        if len(lines) == 1: return "unordered list"
        else:
            unordered = True
            for line in lines[1:]:
                if not unordered_regex.match(line): unordered = False; break
            if unordered: return "unordered list"
    ordered = True
    for i in range(len(lines)):
        if len(lines[i]) < len(str(i + 1)) + 2: ordered = False; break

        if lines[i][:len(str(i + 1)) + 2] != f"{i+1}. ": ordered = False; break
    if ordered: return "ordered list"
    return "paragraph"
    


if __name__ == "__main__":
    text = "###### Heading 6"
    print(block_to_block_type(text))