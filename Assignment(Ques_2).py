Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> try:
    print(2+'33')
except TypeError as e:
   print('Error Handled',e)
try:
    h = "garg1"
    h=float(h)
except ValueError as e:
    print("Error Handled",e)
class Attributes():
    pass
try:
    print (object.attribute)
except AttributeError as e:
    print('error handled',e)




