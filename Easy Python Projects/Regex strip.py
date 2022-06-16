import re

def regexStrip(string, x=''):

    if x == '':
        spaceLeft = re.compile(r'^\s+')
        stringLeft = spaceLeft.sub('',string)
        spaceRight = re.compile(r'\s+$')
        stringBoth = spaceRight.sub('',stringLeft)
        return stringBoth
        

    else:
        charLeft = re.compile(r'^(%s)+'%x)
        stringLeft = charLeft.sub('',string)
        charRight = re.compile(r'(%s)+$'%x)
        stringBoth = charRight.sub('',stringLeft)
        return stringBoth


string1 = '   Shubham Majhi     '
string2 = '1234Jabalpur'
string3 = '@@@@@Data Analytics@@@'
stripped1 = regexStrip(string1)
stripped2 = regexStrip(string2, '1234')
stripped3 = regexStrip(string3, '@')
print(stripped1)
print(stripped2)
print(stripped3)