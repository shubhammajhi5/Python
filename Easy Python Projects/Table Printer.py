# function to print the data in padded format
def printTable(tableData):
    
    col_width = []
    for item in tableData:
        col_width.append(max(map(lambda x : len(x), item)))


    for i in range(len(tableData[0])):
        for j in range(len(tableData)):
            print(tableData[j][i].rjust(max(col_width)), end = '')
        print()


# raw data
tableData = [
    ['apples', 'oranges', 'cherries', 'bananas'],
    ['raja', 'ram', 'mohun', 'roy'],
    ['dogs', 'cats', 'mouse', 'goose']
]

printTable(tableData)