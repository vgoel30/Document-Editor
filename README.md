# Python-Scripts

A collection of python scripts

###1. document_editor.py:
This script will go through all the .docx (Word) files in the directory it is located in and change the **left indenting level** and the **font-size** as specified by the user. The default font is Times New Roman

####Dependencies
This script uses *python-docx*, a Python library for creating and updating Microsoft Word (.docx) files. 
The installation link: [python-docx installation](https://python-docx.readthedocs.io/en/latest/user/install.html#install)

*python-docx* will require a package manager like [pip](https://pypi.python.org/pypi/pip) in order to be installed. 

####How to use
After all the dependency requirements have been met, copy the *document_editor.py* file into the directory with the .docx files which you want to modify.

The script takes two command-line arguments (other than the script name itself)

The command: ``python document_editor.py indent_distance font_size`` 

**NOTE**: Indent distance is in inches and font size is in pt.

####Sample Usage
``python document_editor.py 1.5 13`` will set the indent distance to 1.5 inches and the font-size to 13 pt for all the .docx documents in the directory.

``python document_editor.py 2 11`` will set the indent distance to 2 inches and the font-size to 11 pt.


###2. extension_modifier.py:
This script will change the extension of all files of a particular extension in the specified directory to the new extension as specified by the user. 


####How to use

The script takes two command-line arguments (other than the script name itself)

The command: ``python extension_modifier.py old_extension new_extension`` 

The script will then prompt for the directory path in which the modification is to be performed.

####Sample Usage
``python extension_modifier.py .jpg .png`` will change all .jpg files in the specified directory into .png


