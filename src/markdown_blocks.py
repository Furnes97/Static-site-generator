
from enum import Enum


def markdown_to_blocks(markdown):
    clean_list = []
    markdown_list = markdown.split("\n\n")
    #markdown_list.extend(markdown.split("\n\n"))
    clean_list = list(filter(None, markdown_list))
    final_list = [element.strip() for element in clean_list]
    #for element in
    return final_list


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(markdown_block):
    # Check if its a heading block
    headings = ["# ", "## ", "### ", "#### ", "##### ", "###### "]
    headings_list = list(map(lambda x: markdown_block.startswith(x), headings))
    if any(headings_list):
        return BlockType.HEADING
    # Check if its a code block
    if markdown_block[:3] == "```" and markdown_block[-3:] == "```":
        return BlockType.CODE
    # Check if its a quote block
    quote_list = list(map(lambda line: line[0] == ">", markdown_block.split("\n")))
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
