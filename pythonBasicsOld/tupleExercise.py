#You have the tuple tup = ('www', 'thapar', 'edu','index','php','about-us','mission')
# now you can make a full URL like this www.thapar.edu/index.php/about-us/mission

rawTup = ('www', 'thapar', 'edu','index','php','about-us','mission')
urlTup = (rawTup[0],'.',rawTup[1],'.',rawTup[2],'/',rawTup[3],'.',rawTup[4],'/',rawTup[5],'/',rawTup[6])
print(rawTup)
print(urlTup)
url = ''.join(urlTup)
print(url)
print(''.join(rawTup))
