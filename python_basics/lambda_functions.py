
a = [1,2,3,4]

# print(map(lambda x: x*2 , a))

print(list(map(lambda x: x*2, [2,3,4,5])))

dict_val = [{'name':'abhik', 'age':22}, {'name':'surbhi', 'age':33}, {'name':'shivangi', 'age':33}]

print(list(map(lambda x: x['age'], dict_val)))

print(list(filter(lambda x: x%2 == 0, [1,2,3,4,5])))


# Check sys module and os module

import sys, os

v = sys.version_info
print('The version details are {} {} {}'.format(*v))
print(os.getcwd())
print(os.getenv('PATH'))
print(os.cpu_count())
print(os.name)

VERSION = (5, 2, 0)

__version__ = '.'.join(map(str, VERSION))
print(__version__)