from markdown import markdown_to_blocks, block_to_block_type
class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def __eq__(self, node):
        return self.tag == node.tag and self.value == node.value and self.children == node.children and self.props == node.props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        props_string = " "
        if self.props == None: return ""
        
        for prop_key in self.props.keys():
            props_string += f"{prop_key}=\"{self.props[prop_key]}\" "
        return props_string
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    

