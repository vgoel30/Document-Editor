import os
from sys import argv

#get the original and new extensions as command line arguments
script, orginal_extension, new_extension = argv

#user must provide the proper arguments
if(len(argv) != 3):
	print("\nSAMPLE USAGE: python extension_modifier.py .jpeg .png")

#the extension names should have only a single .
if(orginal_extension.count('.') != 1 or new_extension.count('.') != 1):
	print("\nProvide proper extension name like: .avi or .png\n")
	quit()

#if the previous condition is met, the . should be the first character
if(orginal_extension[:1] != '.' or new_extension[:1] != '.'):
	print("\nProvide proper extension name like: .avi or .png\n")
	quit()

#get the directory name from the user
directory = raw_input("Give directory name")
#cd to directory
os.chdir(directory)

#iterate over all the files in the directory
for file in os.listdir(os.getcwd()):
	#get the file name
	file_name = os.path.join(os.getcwd(), file)
	#get the length of the extension
	extension_length = len(orginal_extension)
	#we want to proceed forward iff the file has the same extension as the user desires
	if(file_name[-extension_length:] == orginal_extension):
			#get the new name for the file by modifying extesion
			new_name = file_name.replace(orginal_extension, new_extension)
			#rename the file 
			os.rename(file_name, new_name)
