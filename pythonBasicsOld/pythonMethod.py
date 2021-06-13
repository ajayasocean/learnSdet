# user defined

class vehicle:
  def __init__(self,color):
    self.color=color
  def start(self):
    print("Starting engine")
  def showcolor(self):
    print(f"I am {self.color}") #formated string literal
car=vehicle('black')
car.start()
car.showcolor()


# another example
surName = input('Please enter your last Name:\n')
#print(surName)
class test:
    def __init__(self,user):
        self.user = user
    def showName (self):
        print(f'I am {self.user}') #formated string literal
testRef = test(surName)
testRef.showName()


# build in method

import math
ceilVal = math.ceil(15.25)
print( "Ceiling value of 15.25 is : ", ceilVal)
