from PyPDF2 import PdfFileMerger
import os

#var = os.getcwd() for extracting from another folder
merger = PdfFileMerger()
for item in os.listdir():
    if item.endswith('.pdf'):
        merger.append(item)
merger.write("Final_pdf.pdf")
merger = PdfFileMerger()
with open(orignalFile, 'rb') as fin:
    merger.append(PdfFileReader(fin))
os.remove(orginalFile)
merger.close()