import unittest
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes,

)

from textnode import TextNode, TextType

class TestInlineMarkdown(unittest.TestCase):
    def test_bold(self):
        node = TextNode("This is text with **bold** text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" text", TextType.TEXT),
            ],
            new_nodes,
        )
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_two_images(self):
        matches = extract_markdown_images(
            "[(this is text with an image ![rick roll](https://i.imgur.com/aKaOqIh.gif) and another ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)]"
        )
        self.assertListEqual(
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"), 
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
                ], 
                matches
            )
    
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is a test with a [link](www.hello.com)"
        )
        self.assertListEqual([
            ("link", "www.hello.com")
        ], matches)
    
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    
    def test_no_images(self):
        node = TextNode("This has no images", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This has no images", TextType.TEXT)
            ], new_nodes
        )
    
    def test_split_links(self):
        node = TextNode("text with a [link](www.hello.com) and another [link](www.goodbye.com)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "www.hello.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("link", TextType.LINK, "www.goodbye.com"),

            ], new_nodes
        )
    
    def test_only_link(self):
        node = TextNode("[link](www.hello.com)", TextType.TEXT)
        new_node = split_nodes_link([node])
        self.assertListEqual(
            [
            TextNode("link", TextType.LINK, "www.hello.com"),
            ],
            new_node
        )
    
    def test_text_to_markdown_bold(self):
        nodes = "This is text with **bold** text"
        new_node = text_to_textnodes(nodes)
        self.assertListEqual(
            [
                TextNode("This is text with ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" text", TextType.TEXT),
            ],
            new_node
        )

    def test_text_to_markdown_italic(self):
        nodes = "This is text with *italic* text"
        new_node = text_to_textnodes(nodes)
        self.assertListEqual(
            [
                TextNode("This is text with ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" text", TextType.TEXT),
            ],
            new_node
        )
    
    def test_text_to_markdown_italic_bold(self):
        nodes = "This is text with *italic* and **bold** text"
        new_node = text_to_textnodes(nodes)
        self.assertListEqual(
            [
                TextNode("This is text with ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" and ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" text", TextType.TEXT),
            ],
            new_node
        )
    

if __name__ == "__main__":
    unittest.main()