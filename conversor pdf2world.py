from pdf2docx import Converter

pdf_file = 'C:/Users/rala/OneDrive - Komatsu Forest/Área de Trabalho/Ramon/BS001-12 - Kit Nível de Óleo Hidráulico.pdf'
docx_file = 'C:/Users/rala/OneDrive - Komatsu Forest/Área de Trabalho/Ramon/sample.docx'

# convert pdf to docx
cv = Converter(pdf_file)
cv.convert(docx_file)      # all pages by default
cv.close()