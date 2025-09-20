from textnode import *


def main():
    node = TextNode("This is some anchor text", TextType.Normal_Text, "https://www.boot.dev")
    print(node)
if __name__ == "__main__":
    main()