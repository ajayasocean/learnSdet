# Json Parser with python module
# we are going to parse a json string

import json

ajay_skills = '{"name": "Ajay Ocean", "skills":["QA", "Python"]}'

# loads method parses a json string and return a dictionary object.

dict_ajay_skills = json.loads(ajay_skills)
print(type(dict_ajay_skills))
print('Parsed json in dictionary is: ', dict_ajay_skills)
key_name = dict_ajay_skills['name']
print(key_name)
# not lets try  to pull out first skill, login says since skills have a list then first store
# value of skills and then access it as a list: syntax list1[n]
key_skills = dict_ajay_skills['skills']
print(key_skills, ' : ', type(key_skills))
number_of_skills = len(key_skills)
print('Number of skills : ', number_of_skills)
print('first skills is: ', key_skills[1])
# one liner method for advance level
print(dict_ajay_skills['skills'][0])
