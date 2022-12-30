import PyPDF2

pdffile = open('FILES/c.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdffile)
print(pdfReader.numPages)

pageObj = pdfReader.getPage(0)
print(pageObj.extractText())
pdffile.close()

pypdffile = PyPDF2.PdfFileReader(open('FILES/e.pdf', 'rb'))
print(pypdffile.isEncrypted)

# pypdffile.getPage(0)
pypdffile.decrypt('abc')
pageObj02 = pypdffile.getPage(0)
pageObj02ex = pageObj02.extractText()
print(pageObj02ex)
