"""
The coding assignment, design the common classic ancient Chinese puzzle:
We count heads and legs among the chickens and rabbits in a farm.
How many rabbits and how many chickens do we have? then returns the answer as a JSON.
"""
import json


def main():

    # defining a class for the puzzle
    class ChinesePuzzle:

        # instance variable declaration
        def __init__(self):
            self.__heads = 0
            self.__legs = 0
            self.__chickens = 0
            self.__rabbits = 0
            self.__solution = {}
            self.__msg = "No solution"

        # setting values for heads and legs from user input
        def set__head_leg(self, head_count, leg_count):
            self.__heads = head_count
            self.__legs = leg_count

        # finding solution for puzzle
        def get_solution(self):

            # calculating possible number of rabbits
            self.__rabbits = int((self.__legs - (2 * self.__heads)) / 2)

            # calculating possible number of chickens
            self.__chickens = int(self.__heads - self.__rabbits)

            # checking for invalid input values
            if (self.__legs % 2 != 0) or (self.__heads == 0) or (self.__heads > self.__legs):

                # updating resultant dictionary
                self.__solution['message'] = self.__msg

            # checking for negative number of rabbits and chickens
            elif self.__rabbits < 0 or self.__chickens < 0:

                # updating resultant dictionary
                self.__solution['message'] = "Invalid solution"
                self.__solution['rabbits'] = self.__rabbits
                self.__solution['chickens'] = self.__chickens

            else:
                # updating resultant dictionary for valid results
                self.__solution['message'] = 'success'
                self.__solution['rabbits'] = self.__rabbits
                self.__solution['chickens'] = self.__chickens
            # returning resultant dictionary
            return self.__solution

    # asking for user input
    head_count = int(input('Please enter number of heads\n'))
    leg_count = int(input('Please enter number of legs\n'))

    # class object creation
    puz_obj = ChinesePuzzle()

    # calling setter function for passing inputs to class variables
    puz_obj.set__head_leg(head_count, leg_count)

    # calling solution function and dumping resultant dictionary into json
    answer = json.dumps(puz_obj.get_solution(), indent=2)

    # printing result
    print(answer)

# run main()
if __name__ == '__main__':
    main()
