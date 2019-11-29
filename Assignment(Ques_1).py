Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class SurajException(Exception):
    def __init__(self,v):
        self.v=v
    def __str__(self,v):
        print(v)
i=int(input())
j=int(input())
def abc (i,j):
    return i+j
if abc(i,j)>150:
    print(i+j)
else:
    raise SurajException('custom exception Occured Here!')
