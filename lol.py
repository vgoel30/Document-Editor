import os
import os.path
from docx import Document

#os.chdir('/Users/varungoel/Desktop')
# num_files = [f for f in os.listdir(os.getcwd())
#                 if os.path.isfile(os.path.join(os.getcwd(), f))]
# print(num_files)

#iterate over all the files in the directory
for file in os.listdir(os.getcwd()):
	#get the file name
	file_name = os.path.join(os.getcwd(), file)
	#we want to proceed forward iff the file is a .docx file
	if(file_name[-5:] == '.docx'):
		#last safety check to see it is actually a file
		if os.path.isfile(file_name):
			#get the name of the document without the full path
			print(os.path.basename(file_name))



