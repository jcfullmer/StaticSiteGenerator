from copystatic import cp_source_to_dest
from page_generator import generate_page



def main():
    cp_source_to_dest("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")






if __name__ == "__main__":
    main()