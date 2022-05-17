def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    if number % 2 == 1:
        print(3 * number + 1)
        return 3 * number + 1

try:
    print('Enter Number :')
    number = int(input())

    print('\nThe Collatz Sequence is :\n')
    while number != 1:
        number = collatz(number)

except ValueError:
    print('You must type an integer value only !!!')