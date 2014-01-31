Python 3.3.3 (v3.3.3:c3896275c0f6, Nov 16 2013, 23:39:35) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> s1 = set([0,2,4,6])
>>> type(s1)
<class 'set'>
>>> s2 = set('cbtnuggets')
>>> s1
{0, 2, 4, 6}
>>> s2
{'b', 'c', 'g', 'e', 'n', 's', 't', 'u'}
>>> s3 = ([10, 12, 14, 16])
>>> s1.update(s3)
>>> s1
{0, 2, 4, 6, 10, 12, 14, 16}
>>> newset = set(s1)
>>> newset
{0, 2, 4, 6, 10, 12, 14, 16}
>>> id(newset)
4358672928
>>> id(s1)
4319783960
>>> s1
{0, 2, 4, 6, 10, 12, 14, 16}
>>> sx = s1
>>> sd(s1)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    sd(s1)
NameError: name 'sd' is not defined
>>> id(s1)
4319783960
>>> id(sx)
4319783960
>>> sx.pop()
0
>>> sx
{2, 4, 6, 10, 12, 14, 16}
>>> id(sx)
4319783960
>>> s1
{2, 4, 6, 10, 12, 14, 16}
>>> sx = sx.pop()
>>> id(sx)
4297273536
>>> s1
{4, 6, 10, 12, 14, 16}
>>> sx
2
>>> s1.pop()
4
>>> s1
{6, 10, 12, 14, 16}
>>> s1.remove(10)
>>> s1
{6, 12, 14, 16}
>>> s1
{6, 12, 14, 16}
>>> 8 in s1
False
>>> 6 in s1
True
>>> 12 not in s1
False
>>> 13 not in s1
True
>>> s1.clear()
>>> s1
set()
>>> el = []
>>> type(el)
<class 'list'>
>>> ================================ RESTART ================================
>>> s1 = set()
>>> s1.add(0)
>>> s1
{0}
>>> s1.add(1)
>>> s1
{0, 1}
>>> s2 = set([2, 3, 4, 5])
>>> s1.update(s2)
>>> s1
{0, 1, 2, 3, 4, 5}
>>> s2
{2, 3, 4, 5}
>>> lang = ['lisp', 'python', 'abc', 'c', 'python', 'ruby', 'perl', 'ruby']
>>> lang
['lisp', 'python', 'abc', 'c', 'python', 'ruby', 'perl', 'ruby']
>>> l1 = set(lang)
>>> l1
{'abc', 'c', 'ruby', 'lisp', 'python', 'perl'}
>>> morelang = ['sql', 'erlang', 'perl', 'haskell']
>>> l2 = set(morelang)
>>> l2
{'haskell', 'erlang', 'sql', 'perl'}
>>> l1 - l2
{'c', 'abc', 'ruby', 'python', 'lisp'}
>>> l1 - l2
{'c', 'abc', 'ruby', 'python', 'lisp'}
>>> l1.intersection(l2)
{'perl'}
>>> u = l1.union(l2)
>>> u
{'c', 'erlang', 'sql', 'abc', 'lisp', 'python', 'perl', 'haskell', 'ruby'}
>>> l1
{'abc', 'c', 'ruby', 'lisp', 'python', 'perl'}
>>> for i in l1:
	print(i)

	
abc
c
ruby
lisp
python
perl
>>> 
s1 = set([0,2,4,6])
>>> s2 = set([10,12,14,16])
>>> s1.update(s2)
>>> s1
{0, 2, 4, 6, 10, 12, 14, 16}
>>> s2
{16, 10, 12, 14}
>>> s1
{0, 2, 4, 6, 10, 12, 14, 16}
>>> s2
{16, 10, 12, 14}
>>> s1.issubset(s2)
False
>>> s2.issubset(s1)
True
>>> s2
{16, 10, 12, 14}
>>> 
