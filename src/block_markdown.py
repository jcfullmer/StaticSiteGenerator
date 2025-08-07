



def markdown_to_blocks(markdown):
    split_markdown = []
    for i in markdown.split("\n\n"):
        i = i.strip()
        if i == "":
            continue
        split_markdown.append(i)
    return split_markdown