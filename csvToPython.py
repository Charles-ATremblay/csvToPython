# This class will take a csv file and create a python file with the same name.
# The python file will contain a class containing the attributes of the csv file. 
import csv
import os

# The path of the csv file.(Change this to the path of your csv file)
filePath = "csvToPython\sampleCSVHeader\sample1.csv"

# This method will be used to create the name of the python file.
def getCSVFileName(csvFilePath):

    # Extract the name of the csv file.
    fileName = os.path.basename(csvFilePath)

    # Extract the name of the csv file without the extension.
    fileNameWithoutExtension = os.path.splitext(fileName)[0]

    return fileNameWithoutExtension

# This method will be used to create the python file.
def createPythonFile(fileNameWithoutExtension):
    
    # Create a new python file with the name of the csv file.
    pythonFile = open(fileNameWithoutExtension + ".py", "w+")    
    
    return pythonFile

# This method will be used to create the class.
def createClass(pythonFile, fileNameWithoutExtension):
    
    pythonFileName = fileNameWithoutExtension + ".py"
    #if the file already exists, we want to delete it and create a new one.
    if os.path.exists(pythonFileName):
        pythonFile.close()
        os.remove(pythonFileName)
    
    pythonFile = open(pythonFileName, "w+", encoding="utf-8-sig")

    # Create a class with the name of the csv file in the new python file.
    pythonFile.write("class " + fileNameWithoutExtension + ":\n")

    return pythonFile

# This method will be used to replace the dot with an underscore.
def replaceDotWithUnderscore(string):
    if "." in string:
        string = string.replace(".", "_")
    return string

# This method will be used to create the methods of the class (the constructer, the getters and setters)
def createMethods(pythonFile, csvFilePath):
    
    # Open the csv file.
    with open(csvFilePath, encoding="utf-8-sig") as csvFile, open(pythonFile.name, "a", encoding="utf-8-sig") as pythonFile:
   
        # Read the csv file.
        csvReader = csv.reader(csvFile, delimiter=",")
   
        # Extract the first line of the csv file.
        firstLine = next(csvReader)
  
        # Create the __init__ method.
        pythonFile.write("\tdef __init__(self, ")
    
        # Create the parameters of the __init__ method.
        for i in range(len(firstLine)):
            firstLine[i] = replaceDotWithUnderscore(firstLine[i])
            pythonFile.write(firstLine[i] + ", ")
    
        # Delete the last comma and space.
        pythonFile.seek(pythonFile.tell() - 2, os.SEEK_SET)
        pythonFile.truncate()
    
        # Close the __init__ method.
        pythonFile.write("):\n")

        # Create the attributes of the class.
        for i in range(len(firstLine)):
            firstLine[i] = replaceDotWithUnderscore(firstLine[i])
            pythonFile.write("\t\tself." + firstLine[i] + " = " + firstLine[i] + "\n")

        # Create the get method. We want this format getAttribute(): return attribute
        for i in range(len(firstLine)):
            firstLine[i] = replaceDotWithUnderscore(firstLine[i])
            pythonFile.write("\n\tdef get" + firstLine[i][0].upper() + firstLine[i][1:] + "(self):\n")
            pythonFile.write("\t\treturn self." + firstLine[i] + "\n")
            
        # Create the set method. We want this format setAttribute(attribute): self.attribute = attribute
        for i in range(len(firstLine)):
            firstLine[i] = replaceDotWithUnderscore(firstLine[i])
            pythonFile.write("\n\tdef set" + firstLine[i][0].upper() + firstLine[i][1:] + "(self, " + firstLine[i] + "):\n")
            pythonFile.write("\t\tself." + firstLine[i] + " = " + firstLine[i] + "\n")



#Run the methods.
fileName = getCSVFileName(filePath)
pyFile = createPythonFile(fileName)
createClass(pyFile, fileName)
createMethods(pyFile, filePath)