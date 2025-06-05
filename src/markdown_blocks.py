
from enum import Enum

from htmlnode import LeafNode, ParentNode
from markdown_node import split_nodes_link, split_nodes_image, split_nodes_delimiter, text_to_textnodes

from textnode import TextNode, TextType, text_node_to_html_node


"""

def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

"""

"""
def markdown_to_blocks(markdown):
    #markdown_list.extend(markdown.split("\n\n"))
    blocks = markdown.split("\n\n")
    final_blocks = []
    for block in blocks:
        # Check if the block is empty or contains only whitespace
        if block.strip() == "":
            continue # Skip empty blocks

        # If the block is not empty, add it to the final list
        final_blocks.append(block)

    return final_blocks


    #clean_list = list(filter(None, markdown_list))
    #final_list = [element.strip() for element in clean_list]
    #for element in
"""

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(markdown_block):
    # Check if its a heading block
    markdown_block = markdown_block.strip()
    headings = ["# ", "## ", "### ", "#### ", "##### ", "###### "]
    headings_list = list(map(lambda x: markdown_block.startswith(x), headings))
    if any(headings_list):
        return BlockType.HEADING
    # Check if its a code block
    if markdown_block[:3] == "```" and markdown_block[-3:] == "```":
        return BlockType.CODE
    # Check if its a quote block
    quote_list = list(map(lambda line: line and line[0] == ">", markdown_block.split("\n")))
    if all(quote_list) and len(quote_list) >= 1:
        return BlockType.QUOTE

    # check if its an unordered list block
    unordered_list = list(map(lambda line: line[0:2] == "- " , markdown_block.split("\n")))
    if all(unordered_list) and len(unordered_list) >= 1:
        return BlockType.UNORDERED_LIST

    #Check if its an ordered list block
    counter_ordered = 1
    ordered_check_list = []
    for line in markdown_block.split("\n"):
        ordered_check_list.append(line.startswith(f"{counter_ordered}. "))
        counter_ordered += 1
    if all(ordered_check_list) and len(ordered_check_list) >= 1:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH


def markdown_to_parent_node_tag(text, block_type):
    if block_type == BlockType.PARAGRAPH:
        return "p"

    if block_type == BlockType.HEADING:
        heading_level = text[0:6].count("#")
        return f"h{heading_level}"
    if block_type == BlockType.CODE:
        return "pre"
    if block_type == BlockType.QUOTE:
        return "blockquote"
    if block_type == BlockType.ORDERED_LIST:
        return "ol"
    if block_type == BlockType.UNORDERED_LIST:
        return "ul"






def markdown_to_html_node(markdown):
    blocks = list(map(lambda block: (block, block_to_block_type(block)), markdown_to_blocks(markdown)))
    parent_nodes = []
    for text, block_type in blocks:

        p_tag = markdown_to_parent_node_tag(text, block_type)
        lines = text.splitlines()
        cleaned_lines = []
        for line in lines:
            if line.strip() != "":
                cleaned_lines.append(line)
        text = "\n".join(cleaned_lines)

        if text.strip() == "":
            continue

        if block_type ==  BlockType.CODE:



            # Remove leading newlines (already have this)
            while text.startswith('\n'):
                text = text[1:]

            # Remove the opening ``` and the newline that might follow it
            if text.startswith("```"):
                text = text[3:] # Remove ```
                if text.startswith('\n'):
                    text = text[1:] # Remove newline after ```

            # Remove the trailing ``` and the newline that might precede it
            if text.endswith("```"):
                text = text[:-3]

            """
            while text.startswith("\n"):
                text = text[1:]
            text = text.strip("```")

            #lines = text.splitlines()
            """
            lines = text.splitlines()
            format_text = "\n".join([line.lstrip() for line in lines])
            leaf_nodes = [LeafNode("code", format_text)]
            parent_nodes.append(ParentNode(p_tag, leaf_nodes))


        if block_type ==  BlockType.ORDERED_LIST or block_type ==  BlockType.UNORDERED_LIST:
            list_parents = []
            lines = text.split("\n")
            for line in lines:
                html_nodes = []
                text_nodes = text_to_textnodes(line)
                for text_node in text_nodes:
                    html_nodes.append(text_node_to_html_node(text_node))
                list_parents.append(ParentNode("li", html_nodes))
            parent_nodes.append(ParentNode(p_tag, list_parents))


        if block_type == BlockType.HEADING or block_type == BlockType.QUOTE or block_type == BlockType.PARAGRAPH:
            text = text.lstrip()
            text = text.replace("\n", " ")
            text_nodes = text_to_textnodes(text)
            leaf_nodes = []
            for text_node in text_nodes:
                leaf_nodes.append(text_node_to_html_node(text_node))

            parent_nodes.append(ParentNode(p_tag, leaf_nodes))


    return ParentNode("div", parent_nodes)

        #text_nodes = text_to_textnodes(block[0])
    #    print(text_nodes)
