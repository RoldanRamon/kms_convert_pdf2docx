import tkinter as tk
from tkinter import filedialog
from pdf2docx import Converter

def convert_pdf_to_docx(pdf_file_path):
    # Determine the docx file path
    docx_file_path = pdf_file_path[:-3] + 'docx'
    
    # Convert pdf to docx
    cv = Converter(pdf_file_path)
    cv.convert(docx_file_path)
    cv.close()
    print(f"Conversion of {pdf_file_path} completed successfully!")

def select_pdf_files():
    file_paths = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
    if file_paths:
        for file_path in file_paths:
            convert_pdf_to_docx(file_path)

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Display file dialog to select PDF files
    select_pdf_files()

    root.mainloop()

if __name__ == "__main__":
    main()
