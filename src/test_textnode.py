import unittest
from textnode import TextNode, TextType, text_node_to_html_node

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
    
class TestTextNodeToHTML(unittest.TestCase):  
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_bold(self):
        node = TextNode('This is bold', TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'b')
        self.assertEqual(html_node.value, 'This is bold')
    
    def test_link(self):
        node = TextNode("Click me!", TextType.LINK, "https://boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click me!")
        self.assertIn("href", html_node.props)
        self.assertEqual(html_node.props["href"], "https://boot.dev")

if __name__ == "__main__":
    unittest.main()