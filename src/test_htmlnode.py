import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):

    #def setUp(self):
    #self.my_instance =


    def test_props_to_html(self):
        result = HTMLNode(None, None, None, {"href": "https://www.google.com","target": "_blank",}).props_to_html()
        self.assertEqual(result,  ' href="https://www.google.com" target="_blank"')

    def test_props_to_html2(self):
        result = HTMLNode(None, None, None, {"href": "https://www.google.com","target": "_blank",}).props_to_html()
        self.assertNotEqual(result, "Some random string")

    def test_props_to_html3(self):

        result = HTMLNode(None, None, None, {"abba": "hva skjer her.com","my_target": "noe skurrer",}).props_to_html()
        self.assertNotEqual(result,  'abba"="hva skjer her.com" "my_target": "noe skurrer')

    def test_props_to_html4(self):
        result = HTMLNode(None, "Hello", None, {"abba": "hva skjer her.com","my_target": "noe skurrer",}).props_to_html()
        self.assertNotEqual(result,  '"abba"="hva skjer her.com" "my_target": "noe skurrer"')


class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_to_html_p2(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_b(self):
        node = LeafNode("b", "Hello, world!")
        self.assertEqual(node.to_html(), "<b>Hello, world!</b>")

    def test_leaf_to_html_b2(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_a(self):
            node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
            self.assertEqual(
                node.to_html(),
                '<a href="https://www.google.com">Click me!</a>',
            )

if __name__ == "__main__":
    unittest.main()



"""
LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
"<a href="https://www.google.com">Click me!</a>"
"""

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
            "<div><span><b>grandchild</b></span></div>",)
