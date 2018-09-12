import re

text = 'kqfl{h4354w_h1um3w_15_gw34p4gq3}'
result = ''

for char in text:
    if bool(re.match('^[a-zA-Z]+$', char)):
        result += chr(ord(char) - 5)
    else:
        result += char

print(result)