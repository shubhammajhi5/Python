import os, glob, re

os.chdir("C:\\Users\\dell\\Desktop\\RegexSearchTextFiles")
userRegex = re.compile(input('Enter your Regex expression :'))

# email_regex = [a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4})

for textFile in glob.glob("*.txt"):
    currentFile = open(textFile) #open the text file and assign it to a file object
    textCurrentFile = currentFile.read() #read the contents of the text file and assign to a variable
    print(textCurrentFile)
    searchedText = userRegex.search(textCurrentFile)
    print(searchedText.group() if searchedText else None)