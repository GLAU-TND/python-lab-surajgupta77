Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> try:
    h=eval(input())
    print(10/h)
except EOFError as e:
    print('EOF end of file error')
except ValueError as e:
    print('value not valid error')
except(ZeroDivisionError,TypeError,AttributeError) as e:
    print('unknown error ',e)
finally:
    print('done')
