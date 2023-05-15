"""
HTML to PDF Converter with PDFCROWD
"""

import os
import pdfcrowd
from dotenv import load_dotenv

load_dotenv()

PDFCROWD_API_KEY = os.getenv('PDFCROWD_API_KEY')
PDFCROWD_USERNAME = os.getenv('PDFCROWD_USERNAME')
PDF_FILE_PATH = "resume.pdf"

html_file_path = input("Enter path to html File: ")
client = pdfcrowd.HtmlToPdfClient(PDFCROWD_USERNAME, PDFCROWD_API_KEY)
client.convertFileToFile(html_file_path, PDF_FILE_PATH)
print(f'File converted and saved to {PDF_FILE_PATH}')
