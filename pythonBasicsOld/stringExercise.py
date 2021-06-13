# Obtain the domain name (thapar.edu) name from the URL

url = 'http://www.thapar.edu/index.php/about-us/mission'
domainName = 'thapar.edu'
#urlLength = len(url)
domainNameLenght = len(domainName)
domainStartIndex = url.find(domainName)
print('Domain Name index is', domainStartIndex)
domainEndIndex = domainStartIndex + domainNameLenght
print('Domain name in url is', url[domainStartIndex : domainEndIndex])

#another way
dotindex = url.find(".")
domainStartIndex = dotindex+1
domainEndIndex = domainStartIndex+domainNameLenght
print('Domain name in url is',url[domainStartIndex : domainEndIndex])
