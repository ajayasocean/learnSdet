# Define a class where in you have two member variables num1 and num2
# two functions for sum and product. constructor
# getter setter


# taking input from user and since this program is for sum and product, i'll eval them
a = eval(input("Please first number\n"))
b = eval(input("Please first second\n"))


# declaring a class here
class SumProd:
    c = 3  # class variable

    def __init__(self):  # constructor
        num1 = a  # instance variables
        num2 = b  # instance variables

    # method to calculate total (sum)
    def get_total_of_nums(self):
        total = self.num1 + self.num2
        return total

    # method to calculate product (multiply)
    def get_product_of_nums(self):
        product = self.num1 * self.num2
        return product


obj = SumProd()  # object instance
obj.num1 = a  # assigning value to call variable
obj.num2 = b  # assigning value to call variable
total = obj.get_total_of_nums()  # method call for total
product = obj.get_product_of_nums()  # method call for multiply

print('sum of numbers', total)
print('product of numbers', product)
