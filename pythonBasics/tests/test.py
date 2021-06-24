"""
Define a class where in you have two member variables num1 and num2
two functions for sum and product. constructor
"""


# declaring a class here
class SumProd:
    def __init__(self, a, b):  # constructor
        self._num1 = a
        self._num2 = b

    # method to calculate total (sum)
    def get_total_of_nums(self):
        return self._num1 + self._num2

    # method to calculate product (multiply)
    def get_product_of_nums(self):
        return self._num1 * self._num2


# taking input from user and since this program is for sum and product, i'll eval them
def driver():
    a = eval(input("Please first number\n"))
    b = eval(input("Please first second\n"))
    obj = SumProd(a, b)  # object instance
    print('sum of numbers', obj.get_total_of_nums())  # method call for total
    print('product of numbers', obj.get_product_of_nums())  # method call for multiply


driver()
