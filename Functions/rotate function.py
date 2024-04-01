import fitz
from tkinter import Tk, filedialog

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