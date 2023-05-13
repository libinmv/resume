"""
HTML to PDF Converter with PDFCROWD
"""

import os
import pdfcrowd
from dotenv import load_dotenv

load_dotenv()

PDFCROWD_API_KEY = os.getenv('PDFCROWD_API_KEY')
PDFCROWD_USERNAME = os.getenv('PDFCROWD_USERNAME')

html_file_path = input("Enter path to html File")
pdf_file_path = f"{html_file_path}.pdf"
client = pdfcrowd.HtmlToPdfClient(PDFCROWD_USERNAME, PDFCROWD_API_KEY)
client.convertFileToFile(html_file_path, pdf_file_path)
print(f'File converted and saved to {pdf_file_path}')
