# Raising an exception in python
a = 0

if a != 2:
    # raise Exception('A is not equal to 0')
    pass
assert (a == 0)

# Try catch example

try:
    with open('../config/testTextFile.txt', 'r') as reader:
        reader.read()
except:
    print('Something went wrong, please check')

# with capturing interpreter error

try:
    with open('../config/testTextFile.txt', 'r') as reader:
        reader.read()
except Exception as e:
    print(e)

# with finally keyword

try:
    with open('../config/testTextFile.txt', 'r') as reader:
        reader.read()
except Exception as e:
    print(e)
finally:
    print('Executed finally')
