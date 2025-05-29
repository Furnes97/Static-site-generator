


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



        #dictionary_tags = {
        #"a":["<a>", "<a/>"],
        #"p":["<a","</a>"]
        #}
