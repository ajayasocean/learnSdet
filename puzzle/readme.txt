"""
The coding assignment, that I have for you is:
Create a FAST API based application,
which exposes an endpoint where you can fill in the values for {head_count} & {leg_count}
to formulate the common classic ancient Chinese puzzle:
We count {head_count} heads and {leg_count} legs among the chickens and rabbits in a farm.
How many rabbits and how many chickens do we have? then returns the answer as a JSON.
"""

Install venv:
$ sudo apt-get install python3-venv

Install below packages in requirement.txt file:
1. pip install fastapi
2. pip install uvicorn[standard]

Navigate to the module directory (../puzzle) then activate venv:
$ source .venv/bin/activate

Launch the puzzle app:
$ uvicorn api.main:app --reload

api root url: http://127.0.0.1:8000

api puzzle url: http://127.0.0.1:8000/heads/35/legs/94

format: http://127.0.0.1:8000/heads/{head_count}/legs/{leg_count}

curl: curl 'http://127.0.0.1:8000/heads/35/legs/94'
You may use curl or open url in any browser.

documentation:
1. http://127.0.0.1:8000/docs
2. http://127.0.0.1:8000/redoc

To stop the uvicorn server use keyboard shortcut : ctrl+c
