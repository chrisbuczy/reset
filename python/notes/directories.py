from pathlib import Path

#a path is the path to a certain file
#absoloute path start from the root of the hard drive
#relative path starts from a certain directorie
#a directorie is a file
#the mkdir function makes a directorie
#the rmdir function removes a directorie
#the glob function searches for files and directories in a current path
#when you use the glob method and you put in the * symbol as one of the arguments than that means it will look through every single file
#too look for a certain file you type *.py will look through python directories

path = Path()
for file in (path.glob('*')):
    print(file)