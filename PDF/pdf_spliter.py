from PyPDF2 import PdfWriter, PdfReader

def cropper(start, end, file):
    input_pdf = PdfReader(open(file, "rb"))
    out_pdf = PdfWriter()

    ostream = open(file.split(".")[0] + "_cropped.pdf", "wb")

    for page_number in range(start - 1, end):
        out_pdf.add_page(input_pdf.pages[page_number])

    out_pdf.write(ostream)
    ostream.close()

cropper(1, 3, "component.pdf")
