
from markdown_blocks import BlockType, markdown_to_blocks, block_to_block_type, markdown_to_html_node

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


    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        block = "- list\n- items"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)


class Test_Markdown_to_HTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        print("----_____-----____----__---__--_-__-__")
        print(html)
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )




if __name__ == "__main__":
    unittest.main()
