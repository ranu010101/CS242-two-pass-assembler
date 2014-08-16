#Preprocessor file for carrying out preprocessor requests.
#Author:- Ranu Vikram, Vikram Bishnoi, Parag Gangil
#This file is to be called by test.py for carrying out macro and opcode queries.

#Macro-Processing unit
#creates the macro-table and replaces the corresponding macros in the table with the labels

def createMacroTable( fileNames ):
	i=0
	for fileName in fileNames :
		inputFile = open(fileName, 'r')
		code = inputFile.read()
		lines = code.split('\n')
		lastMacro =''
		expcode = []
		flag = 0
		ascode =[]
		for line in lines :
			line = line.split(';')[0].lstrip().rstrip()
			if 'MACRO' in line:
				lastMacro = line.split(' ')[1]
				macroTable[lastMacro] = ' '.join(line.split(' ')[2:])
				flag = 1
			elif 'MEND' in line : 
				macrocode[lastMacro]='\n'.join(expcode)
				flag = 0
				expcode = []
				lastMacro =''
			elif flag == 1 :
				expcode.append(line)
			else :
				if(line!='') :
					ascode.append(line)
		code =  '\n'.join(ascode)
		fileNames[i] = fileNames[i].split('.')[0]+'.pp'
		outputFile = open(fileNames[i], 'w')		
		outputFile.write(code)
		tableFile = open(fileNames[i].split('.')[0]+'.table', 'w')
		mcode = '-------------MACROS-------------\n'
		for macros in macroTable :
			mcode = mcode + macros + "\t" + macroTable[macros]
			mcode = mcode + '\n'+ macrocode[macros]+'\n \n'
		mcode = mcode + '-------------MACROS-------------\n'
		tableFile.write(mcode)
		outputFile.close()
		inputFile.close()
		i=i+1

#Function to expand each occurance of macros in the code via looking into the macroTable
def replaceMacros( fileNames ):
	for fileName in fileNames :
		replacements = True
		while replacements :
			replacements = False
			inputFile = open(fileName.split('.')[0] + '.pp', 'r')
			code =  inputFile.read()
			lines = code.split('\n')
			ascode =[]
			for line in lines :
				line = line.lstrip().rstrip()
				tag = macroPresent(line)
				if  tag != '':
					pams =  ''.join(line.split(tag)[1:]).lstrip().rstrip().split(',')
					tag_pam = mapping_macro(tag,pams)
					line = macrocode[tag]
					for pam in tag_pam :
						line = line.replace(pam,tag_pam[pam])
					replacements = True
				if(line!='') :
					ascode.append(line);
			code =  '\n'.join(ascode)
			outputFile = open(fileName, 'w')
			outputFile.write(code.upper())
			outputFile.close()
			inputFile.close()

# Function to map parameters of each of macros with the corrosponding parameters provided in the code
def mapping_macro( tag,pams ):
	tag_pam ={}
	pam_list = macroTable[tag].lstrip().rstrip().split(',')
	i=0
	for pam in pam_list:
		tag_pam[pam] = pams[i]
		i=i+1
	return tag_pam	

# Function to check if the macro is present in the code
def macroPresent( line ):
	tags = line.split(' ')
	for tag in tags :
		tagged = tag.lower()
		for entry in macroTable :
			if tagged == entry.lower():			
				return entry
	return ''

macroTable = {}
macrocode= {}


#Opcode processing unit
def createOpcodeTable():
	inputFile = open('config/opcodes.config', 'r')
	code = inputFile.read()
	lines = code.split('\n')
	lastOpcode =''
	expcode = []
	flag = 0
	for line in lines :
		line = line.lstrip().rstrip()
		if 'OPCODE' in line:
			lastOpcode  = line.split(' ')[1]
			opcodeTable[lastOpcode ] = ' '.join(line.split(' ')[2:])
			flag = 1
		elif 'OPEND' in line : 
			opcodecode[lastOpcode ]='\n'.join(expcode)
			flag = 0
			expcode = []
			lastOpcode  =''
		elif flag == 1 :
			expcode.append(line)

#Function to expand each occurance of opcodes in the code via looking into the opcodeTable

def replaceOpcodes( fileNames ):
	for fileName in fileNames :
		replacements = True
		while replacements :
			replacements = False
			inputFile = open(fileName, 'r')
			code =  inputFile.read()
			lines = code.split('\n')
			ascode =[]
			for line in lines :
				line = line.lstrip().rstrip()
				tag = opcodePresent(line)
				if  tag != '':
					pams =  ''.join(line.split(tag)[1:]).lstrip().rstrip().split(',')
					tag_pam = mapping(tag,pams)
					line = opcodecode[tag]
					for pam in tag_pam :
						line = line.replace(pam,tag_pam[pam])
					replacements = True
				line = variablePresent(line)
				if(line!='') :
					ascode.append(line);
			code =  '\n'.join(ascode)
			inputFile.close()
			outputFile = open(fileName, 'w')
			outputFile.write(code)
			outputFile.close()

# Function to map parameters of each of custom opcode with the corrosponding parameters provided in the code
def mapping( tag,pams ):
	tag_pam ={}
	pam_list = opcodeTable[tag].lstrip().rstrip().split(',')
	i=0
	for pam in pam_list:
		tag_pam[str(pam)] = pams[i]
		i=i+1
	return tag_pam	

# Function to check if the custom opcode is present in the code
def opcodePresent( line ):
	tags = line.split(' ')
	for tag in tags :
		if tag in opcodeTable :
			return tag
	return ''

def variablePresent( line ):
	tags = line.split(' ')
	for tag in tags :
		if '[' in tag :
			add = tag.split('[')[-1].split(']')[0]
			if not add.isdigit() :
				add = '0'
			#line = line.replace(tag,tag.split('[')[0].strip()+'+'+str(add))
			line = line.replace('['+add+']','+'+str(add))
	return line

opcodeTable = {}
opcodecode = {}


