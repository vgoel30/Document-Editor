from docx import Document
from docx.shared import Inches


def modify_indents(filename):
	#get the document with the given filename
    doc = Document(filename) 

    #iterate over all the paragraphs in the document
    for paragraph in doc.paragraphs:
    	#delete all the leading white space for new indent
        paragraph.text = paragraph.text.lstrip()
        #modify the indentation 
        paragraph_format = paragraph.paragraph_format
        paragraph_format.left_indent = Inches(0.5)

	doc.save(filename)


modify_indents('sample.docx')