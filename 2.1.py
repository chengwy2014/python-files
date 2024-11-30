Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
li = [1,2,3]
li[0]
1
tp=(1,2,3)
tp[0]
1
dt = {"name":"jack","age":18,"sex":"male"}
dt
{'name': 'jack', 'age': 18, 'sex': 'male'}
dt["name"]
'jack'
dt["name"] = "hello"
dt
{'name': 'hello', 'age': 18, 'sex': 'male'}
dt["age"] = 10
dt
{'name': 'hello', 'age': 10, 'sex': 'male'}
dt["sex"] = "female"
dt
{'name': 'hello', 'age': 10, 'sex': 'female'}
dt["hobby"] = "打坤坤"
dt
{'name': 'hello', 'age': 10, 'sex': 'female', 'hobby': '打坤坤'}
dt["hobby"] = "Ctrl"
dt
{'name': 'hello', 'age': 10, 'sex': 'female', 'hobby': 'Ctrl'}
dt["hobby"] = "Alt"
dt
{'name': 'hello', 'age': 10, 'sex': 'female', 'hobby': 'Alt'}
dt["hobby"] = "Fn"
dt
{'name': 'hello', 'age': 10, 'sex': 'female', 'hobby': 'Fn'}
delete dt["hobby"]
SyntaxError: invalid syntax
del dt["hobby"]
dt
{'name': 'hello', 'age': 10, 'sex': 'female'}
help
Type help() for interactive help, or help(object) for help about object.
help(guanjianzi)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    help(guanjianzi)
NameError: name 'guanjianzi' is not defined
help(print)
Help on built-in function print in module builtins:

print(*args, sep=' ', end='\n', file=None, flush=False)
    Prints the values to a stream, or to sys.stdout by default.
    
    sep
      string inserted between values, default a space.
    end
      string appended after the last value, default a newline.
    file
      a file-like object (stream); defaults to the current sys.stdout.
    flush
      whether to forcibly flush the stream.

help(print)
Help on built-in function print in module builtins:

print(*args, sep=' ', end='\n', file=None, flush=False)
    Prints the values to a stream, or to sys.stdout by default.
    
    sep
      string inserted between values, default a space.
    end
      string appended after the last value, default a newline.
    file
      a file-like object (stream); defaults to the current sys.stdout.
    flush
      whether to forcibly flush the stream.





























































































































































































































































































































































































































































































































































































































































































































































































































































































a = 我好幸运
Traceback (most recent call last):
  File "<pyshell#315>", line 1, in <module>
    a = 我好幸运
NameError: name '我好幸运' is not defined
a = ("我好幸运")
a
'我好幸运'





































a = (我好幸运)
Traceback (most recent call last):
  File "<pyshell#331>", line 1, in <module>
    a = (我好幸运)
NameError: name '我好幸运' is not defined

























































a
'我好幸运'
del a
a
Traceback (most recent call last):
  File "<pyshell#354>", line 1, in <module>
    a
NameError: name 'a' is not defined
ture
Traceback (most recent call last):
  File "<pyshell#355>", line 1, in <module>
    ture
NameError: name 'ture' is not defined. Did you mean: 'tuple'?
false
Traceback (most recent call last):
  File "<pyshell#356>", line 1, in <module>
    false
NameError: name 'false' is not defined. Did you mean: 'False'?
yes
Traceback (most recent call last):
  File "<pyshell#357>", line 1, in <module>
    yes
NameError: name 'yes' is not defined
no
Traceback (most recent call last):
  File "<pyshell#358>", line 1, in <module>
    no
NameError: name 'no' is not defined
I Love You
SyntaxError: invalid syntax





































































































































































































































dt.clear()
dt
{}
del dt
dt
Traceback (most recent call last):
  File "<pyshell#440>", line 1, in <module>
    dt
NameError: name 'dt' is not defined













































dt = {"name":"jack","age":18,"sex":"male"}
dt
{'name': 'jack', 'age': 18, 'sex': 'male'}
d =
SyntaxError: incomplete input
a = ("滚！")













































a
'滚！'














































d = dt.copy()

d
{'name': 'jack', 'age': 18, 'sex': 'male'}
type(d)
<class 'dict'>
a = ("jchdslcfshdkufhwufhewuhfyugyugyudgyucdskjhckjdnkjenfekjhrejfioeqpurwfueytyreiuoytriuewyfiuefuiehfugfygygcyrgyrgfyugyuvcgvyugyugchgefyrecgygcrfewvrruhduihsuidhuewdhiewuhfeiuhfkjenvfekjvnfewkjrhfuiewfuierhfuiehfueh")













































a
'jchdslcfshdkufhwufhewuhfyugyugyudgyucdskjhckjdnkjenfekjhrejfioeqpurwfueytyreiuoytriuewyfiuefuiehfugfygygcyrgyrgfyugyuvcgvyugyugchgefyrecgygcrfewvrruhduihsuidhuewdhiewuhfeiuhfkjenvfekjvnfewkjrhfuiewfuierhfuiehfueh'
del a
a
Traceback (most recent call last):
  File "<pyshell#528>", line 1, in <module>
    a
NameError: name 'a' is not defined













































len(d)
3
Ture
Traceback (most recent call last):
  File "<pyshell#547>", line 1, in <module>
    Ture
NameError: name 'Ture' is not defined
"age" in d
True
"sb" in d
False
>>> 
>>> 

... 
... 
>>> 

>>> 

... 
... 
... 
>>> 

>>> 

... 
... 
>>> 

>>> 

... 
... 
>>> 

>>> 

... 
... 
... 
>>> 

>>> 

... 
... 
... 
>>> 

>>> 

>>> 
>>>
