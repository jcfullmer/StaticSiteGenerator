from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import TextNode
from inline_markdown import text_to_textnodes
from block_markdown import BlockType, markdown_to_blocks, block_to_block_type

def block_node_to_html_node(block_type):
    if block_type == BlockType.PARAGRAPH:
        return HTMLNode("p",  value=block_type.text)
    if block_type == BlockType.HEADING:
        return HTMLNode("head", value=block_type.text)
    if block_type == BlockType.CODE:
        return HTMLNode("code", value=block_type.text)
    if block_type == BlockType.QUOTE:
        return HTMLNode(">", value=block_type.text, props={"href": block_type.url})
    if block_type == BlockType.UNORDERED_LIST:
        return HTMLNode("ul", value=block_type.text)
    if block_type == BlockType.ORDERED_LIST:
        return HTMLNode("ol start=1", value=block_type.text)
    raise Exception("HTML Node is not a valid HTML type.")


def markdown_to_html_node(text):
    mdBlocks = markdown_to_blocks(text)
    for block in mdBlocks:
        type = block_to_block_type(block)

