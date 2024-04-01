import PyPDF2
from tkinter import Tk, filedialog

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
