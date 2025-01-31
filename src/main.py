from textnode import TextNode, TextType
from markdown import extract_markdown_images
from htmlnodeconstruction import markdown_to_html_node
from leafnode import LeafNode
import shutil
import os
import re

def extract_header(markdown):
    header_1_regex = re.compile(r"# (\w+)")
    header = header_1_regex.match(markdown)
    if header is None or len(header.string) < 3: raise ValueError("No H1 Header found!")
    return header.group(1)


def generate_page(from_path, template_path, dst_path):
    print(f"Generating page from {from_path} to {dst_path} using {template_path}")

    with open(from_path, "r") as from_file:
        from_contents = from_file.read()
    
    with open(template_path, "r") as template_file:
        template_content = template_file.read()
    
    node = markdown_to_html_node(from_contents)

    html_text = node.to_html()
    title = extract_header(from_contents)

    page = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_text)

    if not os.path.exists("/".join(dst_path.split("/")[0:-1])):
        os.mkdir("/".join(dst_path.split("/")[0:-1]))
    
    with open(dst_path, "w") as destination:
        destination.write(page)
    




            

def copy_static_files(path, dst):
        for object in os.listdir(path):
            object_path = os.path.join(path, object)
            destination_path = os.path.join(dst, object)
            if os.path.isfile(object_path):
                
                shutil.copy(object_path, destination_path)
                print(f"Moving {object_path} to {destination_path}")
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

def main():
    move_static_files_to_public_folder()
    generate_page("content/index.md", "template.html", "public/index.html")

main()