from enum import Enum
from htmlnode import HTMLNode, ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType

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



def markdown_to_html(markdown):
    pass


def text_to_children(text):
    html_nodes = []
    nodes = text_to_textnodes(text)

    for node in nodes:
        result = text_node_to_html_node(node)
        html_nodes.append(result)
    return html_nodes


para = "### Line one, still same paragraph"

def markdown_to_paragraph(markdown):
    lines = markdown.split("\n")
    joined = " ".join(lines)
    child = text_to_children(joined)
    return ParentNode("p", child)

def markdown_to_heading(markdown):
    level = 0

    for ch in markdown:
        if ch == "#":
            level+=1
        else:
            break
    if level == 0 or level > 6:
        return("Invalid range")
    if len(markdown) <= level or markdown[level] != " ":
        return("Invalid markdown")
    text = markdown[level + 1: ]

    children = text_to_children(text)
    return ParentNode(f'h{level}', children)

print(markdown_to_heading(para))


def markdown_to_code(markdown):
    pass

def markdown_to_quote(markdown):
    pass

def markdown_to_ul(markdown):
    pass

def markdown_to_ol(markdown):
    pass