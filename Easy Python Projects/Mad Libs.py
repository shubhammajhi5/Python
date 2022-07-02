import re

# Open madlib File and new Adlib file
madlib = open('C:\\Users\\dell\\Desktop\\madlibs.txt', 'r')
content = str(madlib.read())
print(content)
madlib.close()

# Find capital word in file and prompt user to enter one
reg_obj = re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB')
mo = reg_obj.findall(content)
for i in range(len(mo)):
    new_word = input(f'Please enter a(n) {mo[i]}: \n')
    content = reg_obj.sub(new_word, content, 1)

print(content)

new_madlib = open('C:\\Users\\dell\\Desktop\\new_madlibs.txt', 'w')
new_madlib.write(content)
new_madlib.close()