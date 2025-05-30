from textnode import TextNode, TextType
'''
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    split_nodes_list = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            new_nodes.extend(node.text.split(delimiter))
        else:
            return (new_nodes.append(node))
    if len(split_nodes_list) % 2 == 0:
        raise ValueError("invalid markdown, formatted section not closed")
    for i in range(len(split_nodes_list)):
        if i == 0 or (i % 2) == 0:
            new_nodes.append(TextNode(split_nodes_list[i], TextType.TEXT))
        else:
            new_nodes.append(TextNode(split_nodes_list[i], text_type))
    return new_nodes
'''


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes
