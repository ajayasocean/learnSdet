#To validate that whether user inputs makes a triangle or not, If yes the which one among equilateral, isosceles, scalene triangle.
side1 = eval(input('Please enter length of side 1 in centimeters\n'))
side2 = eval(input('Please enter length of side 2 in centimeters\n'))
side3 = eval(input('Please enter length of side 3 in centimeters\n'))

#checking if given dimensions makes a triangle
if (side1+side2 >= side3) and (side2+side3 >= side1) and (side1+side3 >= side2) :
    print('Dimensions provided by you may make a triangle!')
    #checking for which type of a triangle is possible with given dimensions
    if (side1 == side2 == side3):
        print(side1,'cm,',side2,'cm,',side3,'cm, makes a equilateral triangle.')
    elif (side1 == side2) or (side2 == side3) or (side1 == side3):
        print(side1,'cm,',side2,'cm,',side3,'cm, makes a isosecles triangle.')
    else :
        print(side1,'cm,',side2,'cm,',side3,'cm, makes a scalene triangle.')
else:
    print('Dimensions provided by will not make a triangle.')


    
