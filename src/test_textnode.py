import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_eq_italic(self):
        node = TextNode("Hello", TextType.ITALIC, "www.hello.com")
        node2 = TextNode("Hello", TextType.ITALIC, "www.hello.com")
        self.assertEqual(node, node2)
    
    def test_repr_wit_url(self):
        node = TextNode("This is some text", TextType.ITALIC, "http://example.com")
        expected = "TextNode(This is some text, italic, http://example.com)"
        self.assertEqual(repr(node), expected)
    
    def test_repr_without_url(self):
        node = TextNode("More text", TextType.BOLD)
        expected = "TextNode(More text, bold, None)"
        self.assertEqual(repr(node), expected)

if __name__ == "__main__":
    unittest.main()