"""
The coding assignment, that I have for you is:
Create a FAST API based application,
which exposes an endpoint where you can fill in the values for {head_count} & {leg_count}
to formulate the common classic ancient Chinese puzzle:
We count {head_count} heads and {leg_count} legs among the chickens and rabbits in a farm.
How many rabbits and how many chickens do we have? then returns the answer as a JSON.
"""
# importing required packages
from fastapi import FastAPI

# fast api object creation
app = FastAPI()


# root get api for testing api endpoint and printing welcome message
@app.get("/")
def read_root():
    return {"details": "Ancient Chinese Puzzle"}


# get api for the puzzle, taking inputs as path parameters
@app.get("/heads/{head_count}/legs/{leg_count}")
# defining function to accept path parameters and solve puzzle
def solve_puzzle(head_count: int, leg_count: int):
    # variable initialization
    solution = {}
    heads, legs, rabbits, chickens = 0, 0, 0, 0

    # path parameters assignment to actual variables.
    heads = head_count
    legs = leg_count

    # calculating possible number of rabbits
    rabbits = int((legs - (2 * heads)) / 2)

    # calculating possible number of chickens
    chickens = int(heads - rabbits)
    # checking for invalid input values
    if (legs % 2 != 0) or (heads == 0) or (heads > legs):
        # updating resultant dictionary
        solution['details'] = "no_solution"

    # checking for negative number of rabbits and chickens
    elif rabbits < 0 or chickens < 0:
        # updating resultant dictionary
        solution['message'] = "invalid_solution"
        solution['rabbits'] = rabbits
        solution['chickens'] = chickens

    else:
        # updating resultant dictionary for valid results
        solution['details'] = 'success'
        solution['rabbits'] = rabbits
        solution['chickens'] = chickens
    # returning resultant dictionary
    return solution
