## This file contain the requirements and individual task description for this project

### Requirement

* Allowed editors: vi, vim, emacs
* All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All files should end with a newline character
* The first line of all script files should be exactly #!/usr/bin/python3
* A README.md file, at the root of the folder of the project, is mandatory
* Code should use the pycodestyle (version 2.8.*)
* All files must be executable
* The length of files will be tested using wc
* .txt Answer Files
* Only one line
* No Shebang
* All files should end with a new line

### Task Description

* 0-a function would you use to get the type of an object? The name of the function shoul be written in the file, without ().
* 1-How do you get the variable identifier (which is the memory address in the CPython implementation)?
* 2-In the following code, do a and b point to the same object? Answer with Yes or No.
>>> a = 89
>>> b = 100
* 3-In the following code, do a and b point to the same object? Answer with Yes or No.
>>> a = 89
>>> b = 89
* 4-In the following code, do a and b point to the same object? Answer with Yes or No.
>>> a = 89
>>> b = a
* 5-In the following code, do a and b point to the same object? Answer with Yes or No.
>>> a = 89
>>> b = a + 1
* 6-What do these 3 lines print?
>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)
* 7-What do these 3 lines print?
>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)
* 8-What do these 3 lines print?
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)
* 9-What do these 3 lines print?
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)
* 10-What do these 3 lines print?
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)
* 11-What do these 3 lines print?
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)
* 12-What do these 3 lines print?
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
* 13-What do these 3 lines print?
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
* 14-What does this script print?
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
* 15-What does this script print?
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
* 16-What does this script print?
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
* 17-What does this script print?

def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
* 18-What does this script print?

def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
* 19-Write a function def copy_list(l): that returns a copy of a list.
* 20-a = ()
Is a a tuple? Answer with Yes or No.
* 21-a = (1, 2)
Is a a tuple? Answer with Yes or No.
* 22-a = (1)
Is a a tuple? Answer with Yes or No.
* 23-a = (1, )
Is a a tuple? Answer with Yes or No.
* 24-What does this script print?

a = (1)
b = (1)
a is b
* 25-What does this script print?

a = (1, 2)
b = (1, 2)
a is b
* 26-What does this script print?

a = ()
b = ()
a is b
* 27-[200~>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
Will the last line of this script print 139926795932424? Answer with Yes or No.
* 28->>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
Will the last line of this script print 139926795932424? Answer with Yes or No
* 100-a function magic_string() that returns a string “BestSchool” n times the number of the iteration (see code)
* 101-a class LockedClass with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called first_name.
* 102-How many int objects are created by the execution of the first line of the script? (103-line1.txt)
How many int objects are created by the execution of the second line of the script (103-line2.txt)

