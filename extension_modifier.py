import os
from sys import argv

directory = raw_input("Give directory name")
os.chdir(directory)
print(os.getcwd())

#iterate over all the files in the directory
for file in os.listdir(os.getcwd()):
	#get the file name
	file_name = os.path.join(os.getcwd(), file)
	#we want to proceed forward iff the file is a .avi file
	if(file_name[-4:] == '.avi'):
			#get the name of the document without the full path
			print(os.path.basename(file_name))