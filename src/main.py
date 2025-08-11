from copystatic import cp_source_to_dest
from page_generator import generate_page, generate_pages_recursively
import os
import shutil

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    print("Copying files to public directory")
    cp_source_to_dest(dir_path_static, dir_path_public)
    print("Generating page-")
    generate_pages_recursively(dir_path_content, template_path, dir_path_public)






if __name__ == "__main__":
    main()