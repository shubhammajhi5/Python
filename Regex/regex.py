import re

with open('data.txt') as f:
    content = f.read()

emails = '''
CoreyMSchaefer@gmail.com
corey.schaefer@university.edu
corey-321-schaefer@my-work.net
'''

names = '''
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

# pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
# pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-z-]+\.(com|edu|net)')
pattern = re.compile(r'https?://(www\.)?\w+\.(com|gov)')
matches = pattern.finditer(content)

# print(matches)
for match in matches:
    print(match)

