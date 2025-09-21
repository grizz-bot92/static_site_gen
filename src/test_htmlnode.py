import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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
        
        expected = "HTMLNode(p, This is not a paragraph, None, {'class': 'primary'})"
        self.assertEqual(repr(node), expected)
    
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

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
    
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>"
        )
    def test_to_html_two_children(self):
        child1 = LeafNode("b", "Hello")
        child2 = LeafNode(None, " World!")
        parent_node = ParentNode("div", [child1, child2])
        self.assertEqual(
            parent_node.to_html(),
            "<div><b>Hello</b> World!</div>"
        )
    
    def test_headings(self):
        node = ParentNode(
            "h1",
            [
                LeafNode("b", "bold text"),
                LeafNode(None, "normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
             "<h1><b>bold text</b>normal text<i>italic text</i>normal text</h1>"
        )


if  __name__ == "__main__()":
    unittest.main()