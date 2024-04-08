import tkinter as tk
import PyPDF2
import fitz
from tkinter import ttk, messagebox, filedialog, Tk
from PIL import Image, ImageTk
from pdf2docx import Converter

def convert_rules():  
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

def merge_rules():
    def merge_pdfs(output_path, input_paths):
        merger = PyPDF2.PdfMerger()
        for path in input_paths:
            merger.append(path)
        merger.write(output_path)
        merger.close()

    def select_files():
        root = Tk()
        root.withdraw()  # Ocultar a janela principal

        files = filedialog.askopenfilenames(title="Selecionar arquivos PDF")
        return files

    def select_output_path():
        root = Tk()
        root.withdraw()  # Ocultar a janela principal

        output_path = filedialog.asksaveasfilename(defaultextension=".pdf", title="Salvar como")
        return output_path

    def main():
        input_paths = select_files()

        if input_paths:
            output_path = select_output_path()
            if output_path:
                merge_pdfs(output_path, input_paths)
                print("PDFs juntados com sucesso em:", output_path)
            else:
                print("Operação cancelada.")
        else:
            print("Nenhum arquivo PDF selecionado.")

    if __name__ == "__main__":
        main()

def rotate_documents():
    def rotate_pdf(input_path, output_path):
        doc = fitz.open(input_path)
        for page in doc:
            page.set_rotation(180)

        doc.save(output_path)

    def select_file():
        root = Tk()
        root.withdraw()  # Ocultar a janela principal
        file_path = filedialog.askopenfilename(title="Selecionar arquivo PDF")
        return file_path

    def select_output_path():
        root = Tk()
        root.withdraw()  # Ocultar a janela principal
        output_path = filedialog.asksaveasfilename(defaultextension=".pdf", title="Salvar como")
        return output_path

    def main():
        input_path = select_file()
        if input_path:
            output_path = select_output_path()
            if output_path:
                rotate_pdf(input_path, output_path)
                print("PDF rotacionado e salvo com sucesso em:", output_path)
            else:
                print("Operação de salvar cancelada.")
        else:
            print("Nenhum arquivo PDF selecionado.")

    if __name__ == "__main__":
        main()

# Function to load an image and resize it
def load_image(file_name, width, height):
    image = Image.open(file_name)
    image = image.resize((width, height))
    return ImageTk.PhotoImage(image)

# Creating the main window
window = tk.Tk()
window.title('')

# Style for the buttons
button_style = ttk.Style()
button_style.configure('Button.TButton', font=('Arial', 12, 'bold'))

# Frame for the upper buttons
upper_buttons_frame = tk.Frame(window)
upper_buttons_frame.pack()

# Loading icons
convert_icon = load_image('Images/word.ico', 30, 30)
merge_icon = load_image('Images/merge.png', 30, 30)
rotate_icon = load_image('Images/rotate.png', 30, 30)

# Button to Convert pdf2docx
convert_button = ttk.Button(upper_buttons_frame, text='Converter PDF para Word', image=convert_icon, compound=tk.LEFT, command=convert_rules, style='Button.TButton')
convert_button.pack(side=tk.LEFT, padx=5, pady=5)  # Positions the button to the left

# Button to Merge PDFs
merge_button = ttk.Button(upper_buttons_frame, text='Juntar PDFs', image=merge_icon, compound=tk.LEFT, command=merge_rules, style='Button.TButton')
merge_button.pack(side=tk.LEFT, padx=5, pady=5)  # Positions the button to the left

# Frame for the lower buttons
lower_buttons_frame = tk.Frame(window)
lower_buttons_frame.pack()

# Button to Rotate PDF
rotate_button = ttk.Button(lower_buttons_frame, text='Girar PDF', image=rotate_icon, compound=tk.LEFT, command=rotate_documents, style='Button.TButton')
rotate_button.pack(side=tk.LEFT, padx=5, pady=5)  # Positions the button to the left


# Feedback message
message = tk.Label(window, text='')
message.pack()

# Running the GUI
window.mainloop()
