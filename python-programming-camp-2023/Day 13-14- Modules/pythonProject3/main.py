from pdf2docx import Conveter

pdf_path = "sample.pdf"
docx_path = "sample.docx"

cv= Conveter(pdf_file=pdf_path)
cv.convert(docx_filename=docx_path)
cv.close()