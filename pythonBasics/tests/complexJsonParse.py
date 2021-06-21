# Parsing complex Json with nested Structure and extract values
import json
findCoursePrice = input('Please enter course name for which you want to know the price\n')
with open("../config/sampleJson.json") as f:
    data = json.load(f)
    #  print(type(data['courses']))
    for course in data['courses']:  # iterating json without using index and use for loop with if condition
        #  print(course)
        if course['title'] == findCoursePrice:
            print('Price of ', course['title'], ' is ', course['price'])
            assert course['price'] == 45   # asserting to validate price value
            # assert course['price'] == 450  # asserting invalid value throwing assertionError
