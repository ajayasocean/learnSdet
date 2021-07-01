"""
The coding assignment, that I have for you is:
Create a FAST API based application,
which exposes an endpoint where you can fill in the values for {head_count} & {leg_count}
to formulate the common classic ancient Chinese puzzle:
We count {head_count} heads and {leg_count} legs among the chickens and rabbits in a farm.
How many rabbits and how many chickens do we have? then returns the answer as a JSON.
"""


def main():
    # defining a class for the puzzle
    class ChinesePuzzle:
        def __init__(self):
            self.__heads = 0
            self.__legs = 0
            self.__chickens = 0
            self.__rabbits = 0
            self.__solution = {}
            self.__msg = "No solution"

        def set__head_leg(self, head_count, leg_count):
            self.__heads = head_count
            self.__legs = leg_count

        def get_solution(self):
            if (self.__legs % 2 != 0) or (self.__heads == 0) or (self.__heads > self.__legs):
                self.__solution['message'] = self.__msg
            else:
                self.__rabbits = int((self.__legs-(2*self.__heads))/2)
                self.__chickens = int(self.__heads - self.__rabbits)
                self.__solution['message'] = 'success'
                self.__solution['rabbits'] = self.__rabbits
                self.__solution['chickens'] = self.__chickens
            return self.__solution

    head_count = 2
    leg_count = 8
    puz_obj = ChinesePuzzle()
    # print(puz_obj._ChinesePuzzle__solution)
    puz_obj.set__head_leg(head_count, leg_count)
    answer = puz_obj.get_solution()
    print(answer)


if __name__ == '__main__':
    main()
