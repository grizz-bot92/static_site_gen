from textnode import TextNode, TextType
import re

#Converts raw markdown into TextNodes by splitting 

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_list = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_list.append(node)
            continue

        parts = node.text.split(delimiter)

        if len(parts) % 2 == 0:
            raise ValueError("Invalid markdown, closing delimiter missing!")
        for i, part in enumerate(parts):
            if part == "":
                continue
            if i % 2 == 0:
                new_list.append(TextNode(part, TextType.TEXT))
            else:
                new_list.append(TextNode(part, text_type))
    return new_list

#extracts images using regex
def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def split_nodes_image(old_nodes):
    final_list = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            final_list.append(node)
            continue
        images = extract_markdown_images(node.text)

        if len(images) == 0:
            final_list.append(node)
            continue
            
        current_text = node.text
        
        for image in images:
            literal = f'![{image[0]}]({image[1]})'
            before, after = current_text.split(literal, 1)
            if before:
                final_list.append(TextNode(before, TextType.TEXT))
            current_text = after
            final_list.append(TextNode(image[0], TextType.IMAGE, image[1]))
        if current_text:
            final_list.append(TextNode(current_text, TextType.TEXT))
    return final_list

def split_nodes_link(old_nodes):
    final_list = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            final_list.append(node)
            continue
        links = extract_markdown_links(node.text)

        if len(links) == 0:
            final_list.append(node)
            continue
            
        current_text = node.text
        
        for link in links:
            literal = f'[{link[0]}]({link[1]})'
            before, after = current_text.split(literal, 1)
            if before:
                final_list.append(TextNode(before, TextType.TEXT))
            current_text = after
            final_list.append(TextNode(link[0], TextType.LINK, link[1]))
        if current_text:
            final_list.append(TextNode(current_text, TextType.TEXT))
    return final_list

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, '**', TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, '*', TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, '`', TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
    

