Python 3.3.3 (v3.3.3:c3896275c0f6, Nov 16 2013, 23:39:35) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> def uc(a):
	a = a.upper()
	print (a)

	
>>> uc('test')
TEST
>>> uc('test')
TEST
>>> result = uc('python')
PYTHON
>>> result
>>> result
>>> result
>>> result == None
True
>>> result == False
False
>>> result is False
False
>>> def uc(a):
	a = a.upper()
	print (a)
	return a

>>> result = uc('python')
PYTHON
>>> result
'PYTHON'
>>> result == None
False
>>> result is True
False
>>> result is not None
True
>>> type(res2)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    type(res2)
NameError: name 'res2' is not defined
>>> type(result)
<class 'str'>
>>> 
