import os
import fitz  # PyMuPDF
from concurrent.futures import ProcessPoolExecutor

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
    
    total_files = len(pdf_files)

    batch_size = min(total_files, 10) 

    #this process using with parralelize task with batch size = 10 
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(is_password_protected, pdf_files, chunksize=batch_size))

    for filename, is_protected in zip(os.listdir(directory), results):
        count += 1
        if is_protected:
            num_password_protected += 1
            print(f"{filename} is password-protected")
        else:
            print(f"{filename} is not password-protected")

    print(f"Total PDFs: {count}")
    print(f"Password-protected PDFs: {num_password_protected}")

if __name__ == '__main__':
    directory = r'D:\project\pdf-password-checker' 
    count_password_protected_pdfs(directory)