from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered = list(map(lambda x: x.strip(), blocks))
    result = list(filter(lambda x: x != "", filtered))
    return result

def block_to_block_type(markdown):
    lines = markdown.split('\n')

    if markdown.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING

    if len(lines) >= 2 and lines[0] == '```' and lines[-1] == "```":
        return BlockType.CODE
    
    count = 1

    if markdown.startswith('>'):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if markdown.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if markdown.startswith(f'{count}. '):
        for line in lines:
            if not line.startswith(f"{count}. "):
                return BlockType.PARAGRAPH
            count+=1
        return BlockType.ORDERED_LIST
        
    return BlockType.PARAGRAPH



md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""

print(block_to_block_type(md))


