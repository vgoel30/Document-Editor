import os
import os.path
from sys import argv
from docx import Document
from docx.shared import Pt
from docx.shared import Inches


#modifies the indent amount in a .docx file
def modify_indents(filename, indent_amount):

	#get the document with the given filename
    doc = Document(filename) 

    #iterate over all the paragraphs in the document
    for paragraph in doc.paragraphs:
    	#delete all the leading white spaces for new indent
        paragraph.text = paragraph.text.lstrip()
        #modify the indentation 
        paragraph_format = paragraph.paragraph_format
        paragraph_format.left_indent = Inches(indent_amount)
        
        for run in paragraph.runs:
            font = run.font
            font.name = "Times New Roman"
            font.size = Pt(15)


	doc.save(filename)

#if inadequate arguments are provided
if(len(argv) != 2):
    print("\nERROR!\nSample Usage: python document_editor.py 2.5\n")
    quit()

#get the command line arguments
script, indent_amount = argv

#ensure that the indent amount provided is a float
# if not isinstance(indent_amount, float):
#     print("Indent amount must be a float data type")
#     quit()

#test the function
modify_indents('SAFCR7.docx', float(indent_amount))

#code for iterating over all the .docx files in the directory. 
#To be relased after modifying font-settings

#iterate over all the files in the directory
# for file in os.listdir(os.getcwd()):
#     #get the file name
#     file_name = os.path.join(os.getcwd(), file)
#     #we want to proceed forward iff the file is a .docx file
#     if(file_name[-5:] == '.docx'):
#         #last safety check to see it is actually a file
#         if os.path.isfile(file_name):
#             #get the name of the document without the full path
#             print(os.path.basename(file_name))