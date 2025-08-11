import os
from copystatic import ROOT_PATH
from block_to_html import markdown_to_html_node


def extract_title(markdown):
    temp = ""
    for line in markdown.splitlines():
        if line.startswith("# "):
            temp = line[2:]
    if temp == "":
        raise Exception("Error in extract_title: There is no h1 header.")
    return temp


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(os.path.join(ROOT_PATH, from_path), "r") as f:
        mdfile = f.read()
    with open(os.path.join(ROOT_PATH, template_path), "r") as f:
        template_file = f.read()
    html = markdown_to_html_node(mdfile)
    html = html.to_html()
    page_title = extract_title(mdfile)
    final_file = template_file.replace("{{ Title }}", page_title)
    final_file = final_file.replace("{{ Content }}", html)
    absdest_dir = os.path.dirname(os.path.join(ROOT_PATH, dest_path))
    filename = os.path.splitext(os.path.basename(from_path))[0]
    if not os.path.exists(absdest_dir):
        print("Creating destination directories")
        os.mkdir(os.path.dirname(absdest_dir))
    with open(f"{absdest_dir}/{filename}.html", "w") as f:
        f.write(final_file)
    print("File saved successfully")
    

    
    
    #print(template_file)
    #print(mdfile)
    #print(template_file)