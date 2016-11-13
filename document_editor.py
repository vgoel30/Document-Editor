import os
import os.path
from sys import argv
from docx import Document
from docx.shared import Pt
from docx.shared import Inches


#modifies the indent amount in a .docx file
def modify_indents(filename, indent_amount, font_size):
	#get the document with the given filename
    doc = Document(filename) 

    #iterate over all the paragraphs in the document
    for paragraph in doc.paragraphs:
    	#delete all the leading white spaces for new indent
        paragraph.text = paragraph.text.lstrip()
         #check to see non-empty paragraph
        if(len(paragraph.text) > 0):
            #modify the indentation
            paragraph_format = paragraph.paragraph_format
            paragraph_format.left_indent = Inches(indent_amount)
            #for all the different components in the paragraph
            for run in paragraph.runs:
                font = run.font
                font.name = "Times New Roman"
                font.size = Pt(font_size)
    #save the modified content to the file
	doc.save(filename)


#checks to see if the provided value is a float value
def is_number(number):
    try:
        float(number)
        return True
    except ValueError:
        return False

#if inadequate arguments are provided
if(len(argv) != 3):
    print("\nERROR!\nSample Usage: python document_editor.py 2.5 13\n")
    quit()

#get the command line arguments
script, indent_amount, font_size = argv

#ensure that the indent amount provided is a float
if not is_number(indent_amount):
    print("\nERROR: Indent value must be a float\n")
    quit()

#ensure that the font size amount provided is a float
if not is_number(font_size):
    print("\nERROR: Font size value must be a float\n")
    quit()

#iterate over all the files in the directory
for file in os.listdir(os.getcwd()):
    #get the file name
    file_name = os.path.join(os.getcwd(), file)
    #we want to proceed forward iff the file is a .docx file
    if(file_name[-5:] == '.docx'):
        #last safety check to see it is actually a file
        if os.path.isfile(file_name):
            #get the name of the document without the full path
            base_name = os.path.basename(file_name)
            #print(base_name)
            modify_indents(base_name, float(indent_amount), float(font_size))
