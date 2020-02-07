import re

batRegex = re.compile(r'Bat(man|mobile|copter|arang)')
mo = batRegex.search('The Batmobile is the backup if the Batcopter is out of commission')
mo.group()

print(str(mo.group()))