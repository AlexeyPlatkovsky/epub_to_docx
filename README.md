# EPUB to DOCX Converter

This project is a Python script that converts EPUB files into DOCX files. It processes all EPUB files in a specified input folder, converts each file to DOCX while preserving HTML formatting (such as bold and italic) using the **htmldocx** library, and saves the results in a designated output folder.

## Features

- **Batch Conversion:** Scans a folder (`input_files`) for all EPUB files and converts those without a corresponding DOCX in the results folder.
- **HTML Formatting Preservation:** Uses BeautifulSoup and htmldocx to convert HTML content (from the EPUB) into formatted DOCX content.
- **Automatic Folder Creation:** Creates the results folder if it does not already exist.
- **Simple and Extensible:** The code is easy to modify for additional processing or integration into larger projects.

## Requirements

- Python 3.x
- [ebooklib](https://pypi.org/project/EbookLib/)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
- [python-docx](https://pypi.org/project/python-docx/)
- [htmldocx](https://pypi.org/project/htmldocx/)

You can install the dependencies using pip:

```bash
pip install ebooklib beautifulsoup4 python-docx htmldocx
```
or
```bash
pip install -r requirements.txt
```

## How to Run
To run the converter, follow these steps:

### 1.Prepare Your Files:

Create a folder named `input_files` in the root of your project directory and place all your EPUB files there.
Ensure there is a folder named `results` (or let the script create it automatically). This folder will be used to store the converted DOCX files.
Run the Script:

### 2. Run script in terminal
Open a terminal (or command prompt) and navigate to the project root directory.
Execute the script by running:
```
python converter.py
```

The script will iterate through each EPUB file in the `input_files` folder. 
<br>For every file that does not already have a corresponding DOCX file in the results folder, it will:
<br> 1. Read and parse the EPUB file.
<br> 2.Extract the HTML content from each document item.
<br> 3.Convert the HTML (with formatting preserved) into DOCX format.
<br> 4.Save the output DOCX file in the results folder using the same base filename as the original EPUB.

### Monitor the Output:

The script prints messages to the console indicating whether it is converting a file or skipping it because a DOCX version already exists.
Once the script finishes, check the results folder for your converted DOCX files.