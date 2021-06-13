# write a program to print a given string in reverse as output.
# The concept to be used here is slicing in backward order.

#taking input from user
givenString = input('Please enter string you want to reverse\n')
#reverseString = givenString[::-1]

# doing it with a function
def reverseFunction(input):
    return input[::-1]
reverseString = reverseFunction(givenString)
print('Reverse of your string is \n',reverseString)
