from enum import Enum



def markdown_to_blocks(markdown):
    split_markdown = []
    for i in markdown.split("\n\n"):
        i = i.strip()
        if i == "":
            continue
        split_markdown.append(i)
    return split_markdown


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(text):
    if text.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    elif text.startswith("```") and text.endswith("```"):
        return BlockType.CODE
    starts = True
    for line in text.splitlines():
        if not line.startswith(">"):
            starts = False
    if starts == True:
        return BlockType.QUOTE
    starts = True
    for line in text.splitlines():
        if line.startswith("- "):
            continue
        else:
            starts = False
    if starts == True:
        return BlockType.UNORDERED_LIST
    starts = True
    num = 0
    for line in text.splitlines():
        num += 1
        if line.startswith(f"{num}. "):
            continue
        else:
            starts = False
        num += 1
    if starts == True:
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
    


