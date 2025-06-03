from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block(markdown):
    if markdown[:3] == "```" and markdown[-3:] == "```":
        return BlockType.CODE

print(block_to_block("```hello```"))
