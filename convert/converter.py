import ebooklib
import os

from bs4 import BeautifulSoup
from docx import Document
from ebooklib import epub
from htmldocx import HtmlToDocx


def epub_to_docx(epub_path, docx_path):
    """
    Convert an EPUB file to a DOCX file.

    :param epub_path: Path to the input EPUB file.
    :param docx_path: Path to save the output DOCX file.
    """
    # Read the EPUB file
    book = epub.read_epub(epub_path)
    doc = Document()

    # Loop through each HTML item in the EPUB (all chapter-like items are instances of EpubHtml)
    for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
        content = item.get_content()
        # Use BeautifulSoup to extract text from the HTML content
        soup = BeautifulSoup(content, 'html.parser')
        text = str(soup)
        print(f"text is: '{text}'.")
        new_parser = HtmlToDocx()
        new_parser.add_html_to_document(text, doc)

    # Save the DOCX file
    print(f"Conversion successful: '{docx_path}' created.")
    doc.save(docx_file)


# Define the input and results directories
input_folder = './../input_files'
results_folder = './../results'

# Create the results folder if it doesn't exist
if not os.path.exists(results_folder):
    os.makedirs(results_folder)


# Iterate over all files in the input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith('.epub'):
        epub_file = os.path.join(input_folder, filename)
        # Construct the output DOCX file path using the same base filename
        base_name = os.path.splitext(filename)[0]
        docx_file = os.path.join(results_folder, base_name + '.docx')
        # Only convert if the DOCX does not already exist
        if not os.path.exists(docx_file):
            print(f"Converting '{filename}' to DOCX...")
            epub_to_docx(epub_file, docx_file)
        else:
            print(f"Skipping '{filename}' (DOCX already exists).")