from PyPDF2 import PdfFileWriter, PdfFileReader
import getpass

def pass_pdf(pdf_file, your_pass):
    pdfwriter=PdfFileWriter()
    pdf=PdfFileReader(pdf_file)

    for page_num in range(pdf.numPages):
        pdfwriter.addPage(pdf.getPage(page_num))

    password=getpass.getpass(prompt=your_pass)
    pdfwriter.encrypt((password))
    with open('ho.pdf','wb') as f:
        pdfwriter.write(f)

if __name__ == '__main__':
    PdfFile=input("Enter the pdf file path here:-\n")
    PdfPass=input("enter your password to protect the pdf here:-\n")

    pass_pdf(PdfFile,PdfPass)
