# OOPS basics, class & objects
def exam():  # method declaration
    print('method of a class')


class Example:  # class declaration
    num = 100  # class variable declaration


obj = Example()  # object creation
exam()  # method call via a object
print(obj.num)  # call variable call via object


# constructor and self


def get_value():  # method declaration
    print('I am executing as method in class')


class Test:  # class declaration
    val = 10  # class variable declaration

    def __init__(self):  # default constructor
        print('I am called automatically  when object is created')


obj1 = Test()  # object creation
get_value()  # method call via a object
print(obj1.val)  # call variable call via object

obj2 = Test()  # object creation
get_value()  # method call via a object
print(obj2.val)  # call variable call via object


# instance variable & self

class Calculator:
    base = 10

    def __init__(self, a, b):
        self.firstNum = a  # instance variable
        self.secondNum = b  # instance variable

    def addition(self):
        return self.firstNum + self.secondNum + self.base  # adding and returning


objC = Calculator(2, 3)
print('Addition of arguments in first object', objC.addition())

objD = Calculator(4, 5)
print('Addition of arguments in second object', objD.addition())
