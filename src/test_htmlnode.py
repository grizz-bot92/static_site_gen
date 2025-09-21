import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node  = HTMLNode(
            "p",
            "Hello",
            None,
            {"class": "greeting", "href": "https://boot.dev"}

        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"'
            )
    
    def test_values(self):
        node = HTMLNode(
            "div", 
            "Hello World"
            )
        
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello World")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)
    
    def test_repr(self):
        node = HTMLNode(
            "p", 
            "This is not a paragraph", 
            None, 
            {"class": "primary"}
            )
        
        expected = "HTMLNode(p, This is not a paragraph, Children: None, {'class': 'primary'})"
        self.assertEqual(repr(node), expected)

if  __name__ == "__main__()":
    unittest.main()