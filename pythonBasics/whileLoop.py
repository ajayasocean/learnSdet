# while loop : checks for a condition to execute while block and runs till the condition is true
it = 4
while it > 1:
    print(it)  # this case is like a infinite loop as this condition is true infinitely now
    #  to make it a definite loop lets do below action
    it -= 1 # assignment variation ( here it = it-1)
print('while loop finished execution')
#  print('conditon is not true')

# while loop variation with a if condition
print('while execution with if condition')
wit = 4
while wit > 1:
    if wit != 3:
        print(wit)
    wit -= 1 # assignment variation ( here it = it-1)


# while loop variation with a break
print('while loop variation with a break')
a = 10
while a > 1:
    if a == 3:
        break
    print(a)
    a -= 1 # assignment variation ( here it = it-1)

# while loop variation with a continue
print('while loop variation with a continue')
a = 10
while a > 1:
    if a == 9:
        a -= 1  # decrement counter here as if not done before continue then this loop will be stuck in a==9 condition and will run infinitely
        continue
    print(a)
    if a == 3:
        break
    a -= 1


