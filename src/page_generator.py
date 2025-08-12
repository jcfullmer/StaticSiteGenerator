import os
from block_to_html import markdown_to_html_node


def extract_title(markdown):
    temp = ""
    for line in markdown.splitlines():
        if line.startswith("# "):
            temp = line[2:]
    if temp == "":
        raise ValueError("Error in extract_title: There is no h1 header.")
    return temp


def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        mdfile = f.read()
    with open(template_path, "r") as f:
        template_file = f.read()
    html = markdown_to_html_node(mdfile)
    html = html.to_html()
    page_title = extract_title(mdfile)
    final_file = template_file.replace("{{ Title }}", page_title)
    final_file = final_file.replace("{{ Content }}", html)
    final_file = final_file.replace('href="/', f'href="{basepath}')
    final_file = final_file.replace('src="/', f'src="{basepath}')
    dest_dir_path = os.path.dirname(dest_path)
    
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    with open(dest_path.replace(".md", ".html"), "w") as f:
        f.write(final_file)
    print("File saved successfully")



def generate_pages_recursively(dir_path_content, template_path, dest_dir_path, basepath):
        for item in os.listdir(dir_path_content):
            print(item)
            from_path = os.path.join(dir_path_content, item)
            dest_path = os.path.join(dest_dir_path, item)
            print(from_path, dest_path)
            if os.path.isfile(from_path):
                print(f"Copying {item} to {dest_dir_path}")
                generate_page(from_path, template_path, dest_path, basepath)
            if os.path.isdir(from_path):
                generate_pages_recursively(from_path, template_path, dest_path, basepath)