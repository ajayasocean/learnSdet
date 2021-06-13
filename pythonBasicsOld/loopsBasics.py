# for loop
tup1 = (1,2,4,6,8)
for each in tup1:
    print(each*each)  # printing square of each

print([each*each for each in tup1]) # output as list

# for loop with range

for i in range(10):
    print('range',i)

for i in range(1,10):
    print('range(i,j): ',i)

for i in range(1,10,1):
    print('range(i,j,k): ',i)

for i in range(1,10,2):
    print('range(i,j,k+): ',i)
    
