import os
import fitz  # PyMuPDF
from concurrent.futures import ThreadPoolExecutor

def is_password_protected(pdf_path):
    try:
        pdf_document = fitz.Document(pdf_path)
        return pdf_document.needs_pass
    except Exception as e:
        return False

def count_password_protected_pdfs(directory):
    num_password_protected = 0
    count = 0

    pdf_files = [os.path.join(directory, filename) for filename in os.listdir(directory) if filename.lower().endswith('.pdf')]

    if not pdf_files:
        print("No PDF files found in the specified directory.")
        return

    for filename in pdf_files:
        is_protected = is_password_protected(filename)
        count += 1
        if is_protected:
            num_password_protected += 1
            print(f"{filename} is password-protected")
        else:
            print(f"{filename} is not password-protected")

    print(f"Total PDFs: {count}")
    print(f"Password-protected PDFs: {num_password_protected}")

# Specify your directory name with the correct path format
directory = r'D:\Project'

# Call the function to check for password-protected PDFs
count_password_protected_pdfs(directory)
