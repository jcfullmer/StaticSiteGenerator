from textnode import TextNode, TextType


def main():
    test = TextNode("This is some anchor text", TextType.LINK, "https://boot.dev")
    print(test)

if __name__ == "__main__":
    main()