import unittest
from htmlnode import HTMLNode, LeafNode

class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, World")
        self.assertEqual(node.to_html(), "<p>Hello, World</p>")

    def test_leaf_to_html_div(self):
        node = LeafNode("div", "Welcome")
        self.assertEqual(node.to_html(), "<div>Welcome</div>")

    def test_no_tag(self):
        node = LeafNode(None, "Hello")
        self.assertEqual(node.to_html(), "Hello")
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )

if __name__ == "__main__":
    unittest.main()