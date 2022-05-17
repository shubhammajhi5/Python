def comma_code(spam):
    combined = ''
    for i in range(len(spam)):
        if i != (len(spam) - 1):
            combined += spam[i] + ', '
        else:
            combined += 'and ' + spam[i]
    
    return combined 


spam = ['apples', 'bananas', 'tofu', 'cats', 'dogs', 'rats', 'mice']
final_str = comma_code(spam)
print(final_str)