"""
Define a class where in you have two member variables num1 and num2
two functions for sum and product. constructor
Seter getter methods
"""


# declaring a class here
class SumProd:
    def __init__(self):  # constructor
        self.__num1 = 1
        self.__num2 = 1
        self.__sum = 0
        self.__product = 1

    # setting values for num1 & num2 from user input
    def set__values(self, a, b):
        self.__num1 = a
        self.__num2 = b

    # method to calculate sum and return it
    def get_sum_of_nums(self):
        self.__sum = self.__num1 + self.__num2
        return self.__sum

    # method to calculate product (multiply) and return it
    def get_product_of_nums(self):
        self.__product = self.__num1 * self.__num2
        return self.__product


# taking input from user and since this program is for sum and product, i'll eval them
def driver():
    a = eval(input("Please first number\n"))
    b = eval(input("Please first second\n"))
    obj = SumProd()  # object instance
    obj.set__values(a, b)
    # print(obj.__sum)
    print(obj._SumProd__sum)  # name mangling
    print(obj._SumProd__product)  # name mangling
    print('sum of numbers', obj.get_sum_of_nums())  # method call for total
    print('product of numbers', obj.get_product_of_nums())  # method call for multiply


driver()
