from enum import Enum
from htmlnode import LeafNode


class TextType(Enum):
    TEXT = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type: TextType, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        else:
            return False
        
    def __repr__(self):
        if not self.url:    
            return f"TextNode({self.text}, {self.text_type.value})"
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, value=text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", value=text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", value=text_node.text)
    if text_node.text_type == TextType.LINK:
        return LeafNode("a", value=text_node.text, props={"href": text_node.url})
    if text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", props={"src": text_node.url, "alt": text_node.text})
    raise Exception("Text Node is not a valid text type.")
