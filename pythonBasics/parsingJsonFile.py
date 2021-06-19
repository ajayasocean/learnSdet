# parsing a json file into dictionary
# parsing a complete file
import json

with open("config/sampleJson.json") as f:
    jsonData = json.load(f)  # json data is of dictionary data type
    print(type(jsonData), '\n', jsonData)

#  accessing second course from json i.e. 1st course from list
    secondCourse = jsonData['courses'][1]
    print(secondCourse)

#  accessing second course content from json i.e. 1st course from list and its content
    secondCourseTitle = jsonData['courses'][1]['title']  # list and then again dictionary type value
    secondCoursePrice = jsonData['courses'][1]['price']
    print('Title: ', secondCourseTitle)
    print('Price: ', secondCoursePrice)

# accessing dashboard website from json
    dashBoard = jsonData['dashboard']
    print(type(dashBoard), '\n', dashBoard)
    webSite = jsonData['dashboard']['website']  # dictionary type value
    print(webSite)
