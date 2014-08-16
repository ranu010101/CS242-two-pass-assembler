#! /bin/python

import time
from libs import assembler,linker,loader,preprocessor

files = []
file_name = raw_input('Enter the file name : ')
while (file_name!='') :
	files.append(file_name)
	file_name = raw_input('Enter the file name : ')

#Pre-processor carries out various operations to generate macro_table and opcode_table.
#They store macro data and opcode data for each file.

preprocessor.createMacroTable ( files )
preprocessor.replaceMacros ( files )
preprocessor.createOpcodeTable ()
preprocessor.replaceOpcodes ( files )




raw_input('Pre-Processing done.\n.pp, .table and .op files have been generated.\nHit any key to continue. ')
assembler.createSymbolTable( files )   #Pass 1 performed
raw_input('Pass 1 Assembling Done.\nSymbol table has been created.\nHit any key to continue.')
assembler.replaceTable( files )        #Pass 2 performed
raw_input('Pass 2 Assembling Done.\n.s files have been generated.\nHit any key to continue. ')
linker.link(files)                     #Linking performed
raw_input('Linking Done.\n.l files have been generated after linking the files.\nHit any key to continue.')
loader.load(files)	               #Loader executed
raw_input('Loader execution performed.\n.8085 and .l.8085 files have been generated.\nHit any key to continue.')
