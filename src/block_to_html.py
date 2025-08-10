from htmlnode import ParentNode
from textnode import TextNode, text_node_to_html_node, TextType
from inline_markdown import text_to_textnodes
from block_markdown import BlockType, markdown_to_blocks, block_to_block_type

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for node in text_nodes:
        children.append(text_node_to_html_node(node))
    return children


def list_items_to_children(block):
    items = block.split("\n")  
    children = []
    for item in items:
        if item == "":
            continue
        if item.startswith("-"):
            text = item[2:]  
            children.append(ParentNode("li", text_to_children(text)))
        elif item[0].isdigit():
            text = item.split(". ", 1)[1] 
            children.append(ParentNode("li", text_to_children(text)))
    return children

def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code block")
    text = block[4:-3]
    raw_text_node = TextNode(text, TextType.TEXT)
    child = text_node_to_html_node(raw_text_node)
    code = ParentNode("code", [child])
    return ParentNode("pre", [code])

def block_node_to_html_node(block, block_type):
    if block_type == BlockType.PARAGRAPH:
        children = text_to_children(block.replace("\n", " "))
        return ParentNode("p", children)
    if block_type == BlockType.HEADING:
        level = 0
        for char in block:
            if char == "#":
                level += 1
            else:
                break
        text = block[level + 1:]
        children = text_to_children(text)
        return ParentNode(f"h{level}", children)
    if block_type == BlockType.CODE:
        return code_to_html_node(block)
    if block_type == BlockType.QUOTE:
        lines = block.split("\n")
        quote_text = []
        for line in lines:
            quote_text.append(line.lstrip("> "))
        processed_text = " ".join(quote_text)
        children = text_to_children(processed_text)
        return ParentNode("blockquote", children)
    if block_type == BlockType.UNORDERED_LIST:
        children = list_items_to_children(block)
        return ParentNode("ul", children)
    if block_type == BlockType.ORDERED_LIST:
        children = list_items_to_children(block)
        return ParentNode("ol", children)
    raise Exception("Block Node is not a valid HTML type.")


def markdown_to_html_node(text):
    md_blocks = markdown_to_blocks(text)
    md_html = []
    for block in md_blocks:
        type = block_to_block_type(block)
        md_html.append(block_node_to_html_node(block, type,))
    return ParentNode("div", md_html)        

