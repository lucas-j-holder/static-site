from textnode import TextNode, TextType
from markdown import extract_markdown_images
from leafnode import LeafNode
import shutil
import os

def text_node_to_html_node(text_node:TextNode):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"href": text_node.url, "alt": text_node.text})
        case _:
            raise ValueError("TextNode has invalid TextType.")

def copy_static_files(path, dst):
        for object in os.listdir(path):
            object_path = os.path.join(path, object)
            destination_path = os.path.join(dst, object)
            if os.path.isfile(object_path):
                
                shutil.copy(object_path, destination_path)
                print(destination_path)
            elif os.path.isdir(object_path):
                os.mkdir(destination_path)
                copy_static_files(object_path, destination_path)


def move_static_files_to_public_folder():
    dirname = "/".join(os.path.curdir.split("/")[0:-1])
    static_folder = os.path.join(dirname, "static")
    public_folder = os.path.join(dirname, "public")
    if not os.path.exists(static_folder): raise FileNotFoundError("Static Folder not present!")
    if os.path.exists(public_folder):
        shutil.rmtree(public_folder)
        os.mkdir(public_folder)
    else:
        os.mkdir(public_folder)
    copy_static_files(static_folder, public_folder)
    print(os.listdir(public_folder))

def main():
    test_node = TextNode("This is a test node", TextType.BOLD, None)
    move_static_files_to_public_folder()

main()