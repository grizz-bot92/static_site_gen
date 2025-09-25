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

string = 'this is **bold** text with *italic* text and a [link](www.hello.com)'

def text_to_children(text):
    html_nodes = []
    nodes = text_to_textnodes(text)

    for node in nodes:
        result = text_node_to_html_node(node)
        html_nodes.append(result)
    return html_nodes


para = "Line one, still same paragraph"

def markdown_to_paragraph(markdown):
    lines = markdown.split("\n")
    joined = " ".join(lines)
    child = text_to_children(joined)
    return ParentNode("p", child)

def markdown_to_heading(markdown):
    valid = markdown.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### "))


def markdown_to_code(markdown):
    pass

def markdown_to_quote(markdown):
    pass

def markdown_to_ul(markdown):
    pass

def markdown_to_ol(markdown):
    pass