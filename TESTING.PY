# read a text file as a list of lines
# find the last line, change to a file you have
fileHandle = open ( 'test3.txt',"r" )
lineList = fileHandle.readlines()
fileHandle.close()
print lineList
print "The last line is:"
print lineList[len(lineList)-1]
# or simply
print lineList[-1]