import os
import sys
from os import listdir
import os.path as Path

targetsFiles = ["swift", "h", "m"]

def isTargetFile(path):
    for subfix in targetsFiles:
        if path.endswith(subfix):
            return True
    return False


def printAllFiles(root, prefixToRemove):
    if Path.isfile(root):
        if isTargetFile(root):
            print("------------------",
                  root.replace(prefixToRemove, ""), 
                  "------------------\n")
            with open(root, "r") as f:
                lines = f.read()
                print(lines)
            print("\n")
    elif Path.isdir(root):
        innerPaths = [Path.join(root, p) for p in listdir(root)]
        for p in innerPaths:
            printAllFiles(p, prefixToRemove)


argv = sys.argv
# print("arguments",argv)

if len(argv) < 2:
    raise Exception("drag the project you want to print here")


rootPath = sys.argv[1]
# print(rootPath)


printAllFiles(rootPath, rootPath+"/")





        


