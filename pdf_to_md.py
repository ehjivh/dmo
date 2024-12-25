from markitdown import MarkItDown
import os
from tqdm import tqdm

def convert_pdfs_to_md(pdf_directory, md_directory):
    markitdown = MarkItDown()
    if not os.path.exists(md_directory):
        os.makedirs(md_directory)
    
    pdf_files = [f for f in os.listdir(pdf_directory) if f.endswith(".pdf")]
    for filename in tqdm(pdf_files, desc="Converting PDFs to Markdown"):
        pdf_path = os.path.join(pdf_directory, filename)
        result = markitdown.convert(pdf_path)
        md_filename = os.path.splitext(filename)[0] + ".md"
        md_path = os.path.join(md_directory, md_filename)
        with open(md_path, "w") as file:
            file.write(result.text_content)

if __name__ == "__main__":
    pdf_directory = "/Users/tatsuki/Downloads/dmo/pdf/"
    md_directory = "/Users/tatsuki/Downloads/dmo/md/"
    convert_pdfs_to_md(pdf_directory, md_directory)