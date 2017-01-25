import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 080-8169-8088.')
#print('Phone number found: ' + mo.groups())
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)