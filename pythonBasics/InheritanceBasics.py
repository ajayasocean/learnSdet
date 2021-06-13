# inheritance basics , this is a child class, we will be using oopsBasics.py as parent here.
from oopsBasics import Calculator  # syntax : from fileName import ClassName


class ChildImpl (Calculator):
    base2 = 100
    def __init__(self, x, y):
        Calculator.__init__(self, x, y)
        # since parent class is having a non default consructor hence we need to call that here in child constructor


    def get_complete_data(self):
        return self.addition()


print('Program to test inheritance for addtition')
user_input1 = eval(input('Please enter first number'))
user_input2 = eval(input('Please enter second number'))
objchild = ChildImpl(user_input1, user_input2)
print('Adding via inheriting', objchild.get_complete_data())


