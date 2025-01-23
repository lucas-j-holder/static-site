from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag == None: raise ValueError("ParentNode requires a tag.")
        if self.children == None: raise ValueError("ParentNode requires children.")

        open_tag = f"<{self.tag}{self.props_to_html()}>"
        end_tag = f"</{self.tag}>"

        html_string = open_tag
        for child in self.children:
            html_string += child.to_html()
        html_string += end_tag
        return html_string