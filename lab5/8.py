import re
text = input(str(""))
t = (re.findall('[A-Z][^A-Z]*', text))
print (t)