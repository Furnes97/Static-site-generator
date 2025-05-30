


class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html

        #keys, values = zip(*self.props.items())
        #text = " "
        #for i in range(len(keys)):
        #    text += f'{keys[i]}="{values[i]}" '
        #return text[:-1]



    def __repr__(self):
        return f"{self.tag}, {self.tag}, {self.children}, {self.props}"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None ,props)
        #self.props = props

    def to_html(self):
        if self.value is None:
            raise ValueError("all leaf nodes must have value")
        if self.tag is None:
            return self.value
        else:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

        #text[:-1]
    def __repr__(self):
            return f"LeafNode({self.tag}, {self.value}, {self.props})"



class ParentNode(HTMLNode):
    def __init__(self, tag, children ,props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag is required for parentnode")
        if self.children is None:
            raise ValueError("Children are missing")

        return f'<{self.tag}>{"".join(list(map(lambda childnode: childnode.to_html(),self.children)))}</{self.tag}>'

"""
def text_node_to_html_node(text_node):
    if text_node != TextType.TEXT.value:
        return

    elif TextType.BOLD:
    elif TextType.ITALIC:
    elif TextType.CODE:
    elif TextType.LINK:
    elif TextType.IMAGE:
    else:
        raise Exception("Wrong node")


"""

"""
t should handle each type of the TextType enum. If it gets a TextNode that is none of those types, it should raise an exception. Otherwise, it should return a new LeafNode object.

TextType.TEXT: This should return a LeafNode with no tag, just a raw text value.
TextType.BOLD: This should return a LeafNode with a "b" tag and the text
TextType.ITALIC: "i" tag, text
TextType.CODE: "code" tag, text
TextType.LINK: "a" tag, anchor text, and "href" prop
TextType.IMAGE: "img" tag, empty string value, "src" and "alt" props ("src" is the image URL, "alt" is the alt text)
"""


"""
def __init__(self, tag, value, props=None):
    super().__init__(tag, value, None ,props)
"""
