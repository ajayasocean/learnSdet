# test identity operations and id() function
print('This program take input from user and performs identity operation on them\n')
#accepting input from user.
a=eval(input('Please enter first  number for operation less that equal to 256\n'))
b=eval(input('Please enter same number again\n'))
x= id(a)
y = id(b)
if a is b:
    print('address of a',x,'address of b',y, 'hence a is b')
elif a is not b:
shell variable:
variableName = "Hello"
echo $variableName


    print('address of a',x,'address of b',y, 'hence a is not b')

a=eval(input('Please enter first  number for operation greater that 256\n'))
b=eval(input('Please enter same number again\n'))
x= id(a)
y = id(b)
if a is b:
    print('address of a',x,'address of b',y, 'hence a is b')
elif a is not b:
    print('address of a',x,'address of b',y, 'hence a is not b')


print('In case of a list same list assigned to two variables, the identity result for is operation is false as lists are mutable and have different address\n')

lst1 = [1,2]
lst2 = [1,2]
q= id(lst1)
z = id(lst2)

if lst1 is lst2:
    print('address of lst1',q,'address of lst2',z, 'hence lst1 is lst2')
elif lst1 is not lst2:
    print('address of lst1',q,'address of lst2',z, 'hence lst1 is not lst2')
