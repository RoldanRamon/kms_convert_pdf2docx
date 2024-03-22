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
    print("Conversion completed successfully!")

def select_pdf_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        convert_pdf_to_docx(file_path)

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Display file dialog to select PDF file
    select_pdf_file()

    root.mainloop()

if __name__ == "__main__":
    main()
