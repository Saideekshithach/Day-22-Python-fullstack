Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: C:/Users/asus/AppData/Local/Programs/Python/Python311/a.py
[4, 6, 3, 7, 0]
Traceback (most recent call last):
  File "C:/Users/asus/AppData/Local/Programs/Python/Python311/a.py", line 15, in <module>
    " ".split(b)
TypeError: must be str or None, not list

====== RESTART: C:/Users/asus/AppData/Local/Programs/Python/Python311/a.py =====
[4, 6, 3, 7, 0]

====== RESTART: C:/Users/asus/AppData/Local/Programs/Python/Python311/a.py =====
[9, 1, 5, 2, 8]

====== RESTART: C:/Users/asus/AppData/Local/Programs/Python/Python311/a.py =====
[9, 1, 5, 2, 8]

====== RESTART: C:/Users/asus/AppData/Local/Programs/Python/Python311/a.py =====
[9, 1, 5, 2, 8]
[0, 3, 4, 6, 7]
[1, 2, 5, 8, 9]

====== RESTART: C:/Users/asus/AppData/Local/Programs/Python/Python311/a.py =====
[9, 1, 5, 2, 8]
[0, 3, 4, 6, 7]
[1, 2, 5, 8, 9]
[7, 6, 4, 3, 0]
[9, 8, 5, 2, 1]

====== RESTART: C:/Users/asus/AppData/Local/Programs/Python/Python311/a.py =====
[9, 1, 5, 2, 8]
[0, 3, 4, 6, 7]
[1, 2, 5, 8, 9]
[7, 6, 4, 3, 0]
[9, 8, 5, 2, 1]
[7, 6, 4, 3, 0, 9, 8, 5, 2, 1]
>>> 
=============================== RESTART: C:/Users/asus/AppData/Local/Programs/Python/Python311/a.py ===============================
[9, 1, 5, 2, 8]
[0, 3, 4, 6, 7]
[1, 2, 5, 8, 9]
[7, 6, 4, 3, 0]
[9, 8, 5, 2, 1]
[7, 6, 4, 3, 0, 9, 8, 5, 2, 1]
>>> 
=============================== RESTART: C:/Users/asus/AppData/Local/Programs/Python/Python311/a.py ===============================
[7, 6, 4, 3, 0, 9, 8, 5, 2, 1]
>>> 
=============================== RESTART: C:/Users/asus/AppData/Local/Programs/Python/Python311/a.py ===============================
[7, 6, 4, 3, 0, 9, 8, 5, 2, 1]
>>> a=[9,1,5,2,8,4,6,3,7,0]
>>> b=[:5]
SyntaxError: invalid syntax
>>> b=a[:5]
>>> c=a[5:10]
>>> b.sort()
>>> c.sort()
>>> b.reverse()
>>> c.reverse()
>>> print(b+c)
[9, 8, 5, 2, 1, 7, 6, 4, 3, 0]
>>> ptiny(c+b)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    ptiny(c+b)
NameError: name 'ptiny' is not defined. Did you mean: 'print'?
>>> print(c+b)
[7, 6, 4, 3, 0, 9, 8, 5, 2, 1]
