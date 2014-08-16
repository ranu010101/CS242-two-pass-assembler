
import assembler

#Function to link various external tags between the files and generating a common file
def link( fileNames ):
	asCode = []
	i = 0
	for fileName in fileNames :
		inputFile = open(fileName, 'r')
		fileName = fileName.split('.')[0]
		externTable[fileName] = []
		code = inputFile.read()
		lines = code.split('\n')	
		for line in lines :
			line = line.lstrip().rstrip()
			if line !='' :
				if 'EXTERN' in line :
					if validExtern(line.split(' ')[1], fileNames):
						externTable[fileName].append(line.split(' ')[1])
					else :
						print 'ERROR :' + line
						print 'Files Required for Linking not found'
						exit(0)
				else :
					asCode.append(line)
					i = i+1
		fileLengthTable.append(i)
		outputFile = open(fileName+'.l','w')
		outputFile.write('\n'.join(asCode))
		asCode = []
		outputFile.close()

	for fileName in fileNames :
		fileName = fileName.split('.')[0]
		inputFile = open(fileName+'.l.8085', 'r')
		code = inputFile.read()
		lines = code.split('\n')
		j = 0
		asCode = []
		for line in lines :
			line = line.rstrip().lstrip()
			tags = ''.join(line.split(' ')[1:]).split(',')
			for tag in tags :
				if tagPresent(tag,fileName):
					line =  line.replace(tag, externAddress(tag, fileNames)+'#'+tag)
			asCode.append(line)
		outputFile = open(fileName+'.l.8085','w')
		outputFile.write('\n'.join(asCode))

#Function to check if the variable is an extern variable or not
def tagPresent(tag, fileName):
	for extern in externTable[fileName] :
		if extern ==  tag.split('+')[0].strip() :
			return True
	return False

#Function to validate the defined extern
def validExtern(tag, fileNames):
	for fileName in fileNames :
		for extern in variableScopeTable[fileName.split('.')[0]] :
			if extern ==  tag and variableScopeTable[fileName.split('.')[0]][tag] == 'GLOBAL':
				return True
	return False

#Function to link various external tags between the files
def externAddress(tag, fileNames):
	for fileName in fileNames :
		for extern in variableTable[fileName.split('.')[0]] :
			if extern ==  tag.split('+')[0].strip() :
				return fileName.split('.')[0]
	return ''

externTable = {}
fileLengthTable = []
variableScopeTable = assembler.variableScopeTable
variableTable = assembler.variableTable
