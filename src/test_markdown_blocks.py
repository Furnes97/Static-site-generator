
from markdown_blocks import BlockType, markdown_to_blocks, block_to_block_type

import unittest


class TestMarkdownToBlocks(unittest.TestCase):

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )



    def test_markdown_to_blocks2(self):
        md = """
This is **bolded** paragraph

This is **bolded** paragraph also

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
- And another item
- Guess what, one more
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is **bolded** paragraph also",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items\n- And another item\n- Guess what, one more",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

class TestBlockToBlockType(unittest.TestCase):
    def test_heading1(self):
        case = block_to_block_type("### Hello there ```")
        answer = BlockType.HEADING
        self.assertEqual(answer, case)

    def test_heading2(self):
        case = block_to_block_type("##### Hello ## 1. there ```")
        answer = BlockType.HEADING
        self.assertEqual(answer, case)

    def test_code1(self):
        case = block_to_block_type("``` this is code ```")
        answer = BlockType.CODE
        self.assertEqual(answer, case)

    def test_code2(self):
        case = block_to_block_type("This is paragraph ``` dont react to this 'codeblock' ```")
        answer = BlockType.PARAGRAPH
        self.assertEqual(answer, case)

    def test_ordered_list1(self):
        case = block_to_block_type("1. list item 1 out of 1")
        answer = BlockType.ORDERED_LIST
        self.assertEqual(answer, case)

    def test_ordered_list2(self):
        case = block_to_block_type("1. list item\n2. second item\n3. third")
        answer = BlockType.ORDERED_LIST
        self.assertEqual(answer, case)

    def test_ordered_list3(self):
        case = block_to_block_type("1. list item 1 out of 1\n4. it aint ordered return paragraph")
        answer = BlockType.PARAGRAPH
        self.assertEqual(answer, case)

    def test_unordered_list1(self):
        case = block_to_block_type("- hell\n- world\n- just work please")
        answer = BlockType.UNORDERED_LIST
        self.assertEqual(answer, case)

if __name__ == "__main__":
    unittest.main()
