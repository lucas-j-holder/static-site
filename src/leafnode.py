from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag = None, value = None, props = None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value == None: raise ValueError("LeafNode requires a value.")

        start_tag = ""
        end_tag = ""
        if self.tag != None:
            start_tag = f"<{self.tag} {self.props_to_html()}>"
            end_tag = f"</{self.tag}>"
        
        return f"{start_tag}{self.value}{end_tag}"
