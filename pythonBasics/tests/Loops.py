# for loop
obj = [2, 3, 5, 7, 9]
for i in obj:  # for iterationKey in dataSet:
    print(i)  # action as for block

# print multiples of 2 for every element in obj
for i in obj:  # for iterationKey in dataSet:
    print(i*2)  # action as for block

# sum of first 3 natural numbers i.e. 1+2+3+4+5
# definite for loop, function range(i,j) is i to j-1
total = 0
for j in range(1, 6):
    total = total + j
print('Total of first five natural numbers = ', total)

# definite for loop, function range(i,j,k) is i to j-1 with i+k
# (k is the difference in iteration like i++ is 1, i+2 is 2 as so on )
for j in range(1, 10, 2):
    print(j)

# loop with only end argument(upper bound) (k) runs from 0 to k-1 with 1 diff in next iteration
print('for loop with only end argument in range')
for k in range(10):
    print(k)
