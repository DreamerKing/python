url = input("Please intput a url:")
first = url.find('//') + 2
last = url.find('.')
domain = url[first:last]
print("Domain:", domain)