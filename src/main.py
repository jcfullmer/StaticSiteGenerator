from copystatic import cp_source_to_dest
from page_generator import generate_page, generate_pages_recursively
import os
import shutil
import sys

dir_path_static = "./static"
dir_path_docs = "./docs"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv [1]
    else:
        basepath = "/"
    print("Deleting docs  directory...")
    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)
    print("Copying files to public directory")
    cp_source_to_dest(dir_path_static, dir_path_docs)
    print("Generating page-")
    generate_pages_recursively(dir_path_content, template_path, dir_path_docs, basepath)






if __name__ == "__main__":
    main()