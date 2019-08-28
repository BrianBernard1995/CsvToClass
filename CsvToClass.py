import csv
import os

class CsvToClass:
    def __init__(self,PathToCsvFile,ClassName,ClassPath):
        #counter to get first row
        RowCounter = 0
        #Resulting Python Class File
        with open(ClassPath, 'w+') as PythonClassFile:
            PythonClassFile.write("{} {}:\n\t{}".format("class",ClassName, "def __init__(self,row):\n"))
        #CSV file to generate ClassFile on
            with open(PathToCsvFile) as csv_file:
            #CSV function to read CSV File
                csv_reader = csv.reader(csv_file)
            #Iterate through CSV File
                for row in csv_reader:
                #Display Error in which column has bad formatting
                    ColumnCounter = 0
                #Grab First Row
                    if RowCounter == 0:
                    #iterate through first row
                        for col in row:
                        #if col is blank (in my dataset NflPicks has spaces in data)
                            if col == "":
                                print("Empty Column, Column Number - {}".format(ColumnCounter))
                            else:
                            #Write PythonClassFile
                                PythonClassFile.write("\t\tself.{}\n".format(col))

                            ColumnCounter+=1
                    RowCounter+=1



csv = CsvToClass('/Users/brianbernard/Documents/PythonProjects/CsvToClass/data.csv','NflStats',"{}{}.py".format(os.getcwd(),"/NflStats"))
