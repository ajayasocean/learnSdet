"""A Fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5, 8....
The first two terms are 0 and 1. All other terms are obtained by adding the preceding two terms.
This means to say the nth term is the sum of (n-1)th and (n-2)th term. """

# receiving input from user for nth place.

nterm = int(input("Please enter a number for Fibonacci:\n"))

# first two numbers
n1, n2 = 0, 1
count = 0

# checking if provided number of terms is valid

if nterm <= 0:
    print("Please enter positive integer")
# if there is only one term, return n1
elif nterm == 1:
    print("{}{}{}{}".format('Fibonacci till ', nterm, 'is :\n', n1))

# generate fibonacci sequence
else:
    print("Fibonacci sequence:\n")
    while count < nterm:
        print(n1)
        nth = n1+n2
        # updating values here
        n1 = n2
        n2 = nth
        count += 1

