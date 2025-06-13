#Addition,Subtraction,Multiplication of two data type.
#int+int(-*)
#a = 2
#b = 6
#print(a + b)                # 8
#print(a-b)                  # -4
#print(a*b)                   # 12

#str + str(-*)
#a = "Ram"
#b = "Sham"
#print(a+b)                  # RamSham
#print(a-b)                  # TypeError: unsupported operand type(s) for -: 'str' and 'str'
#print(a*b)                   # TypeError: can't multiply sequence by non-int of type 'str'

#float + float(-*)
#a = 20.2
#b = 10.5
#print(a+b)                  # 30.7
#print(a-b)                  # 9.7
#print(a*b)                   # 212.1

#bool + bool(-*)
#a = False
#b = False
#print(a+b)          # 0 
#print(a-b)          # 0
#print(a*b)          # 0

#a = True
#b = True
#print(a+b)          # 2
#print(a-b)          # 0
#print(a*b)          # 1
      
#a = False
#b = True
#print(a+b)        # 1
#print(a-b)        # -1
#print(a*b)        # 0

#complex + complex(-*)
#a = 2 + 4j
#b = 5 + 8j
#print(a+b)              # (7+12j)
#print(a-b)              # (-3-4j)
#print(a*b)              # (-22+36j)

# list + list(-*)
#a = ["abc",1,5]
#b = ["ravi","sai",2.5]
#print(a+b)                  # ['abc', 1, 5, 'ravi', 'sai', 2.5]
#print(a-b)                  # TypeError: unsupported operand type(s) for -: 'list' and 'list'
#print(a*b)                   # TypeError: can't multiply sequence by non-int of type 'list'

#tuple + tuple(-*)
#a = (1,2,3)
#b = (4,5,6)
#print(a+b)                  # (1, 2, 3, 4, 5, 6)
#print(a-b)                  # TypeError: unsupported operand type(s) for -: 'tuple' and 'tuple'
#print(a*b)                  # TypeError: can't multiply sequence by non-int of type 'tuple'

#set + set(-*)
#a = {3,6,2}
#b = {1,8,9}
#print(a+b)              # TypeError: unsupported operand type(s) for +: 'set' and 'set'
#print(a-b)               # {2, 3, 6}
#print(a*b)              # TypeError: unsupported operand type(s) for *: 'set' and 'set'

#dict + dict(-*)
#a = {"d1":2}
#b = {"d2":4}
#print(a+b)                 # TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
#print(a-b)                  # TypeError: unsupported operand type(s) for -: 'dict' and 'dict'
#print(a*b)                 # TypeError: unsupported operand type(s) for *: 'dict' and 'dict'

# int + str(-*)
#a = 5
#b = "10"
#print(a+b)             # TypeError: unsupported operand type(s) for +: 'int' and 'str'
#print(a-b)             # TypeError: unsupported operand type(s) for -: 'int' and 'str'
#print(a*b)             # 1010101010

#int+float(-*)
a = 4
b = 3.6
#print(a+b)             # 7.6
#print(a-b)             # 0.3999999999999999
#print(a*b)             # 14.4

#int+bool(-*)
a = 4
b = True
#print(a+b)             # 5
#print(a-b)             # 3
#print(a*b)             # 4

a = 4
b = False
#print(a+b)             # 4
#print(a-b)             # 4
#print(a*b)             # 0

#int+complex(-*)
a = 5
b = 2 + 2j
#print(a+b)         # (7+2j)
#print(a-b)         # (3-2j)
#print(a*b)         # (10+10j)

#int+list(-*)
a = 4
b = [1,2,3]
#print(a+b)         # TypeError: unsupported operand type(s) for +: 'int' and 'list'
#print(a-b)          # TypeError: unsupported operand type(s) for -: 'int' and 'list'
#print(a*b)          # [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]

#int+tuple(-*)
a = 4
b = (1,2,3)
#print(a+b)          # TypeError: unsupported operand type(s) for +: 'int' and 'tuple'
#print(a-b)         # TypeError: unsupported operand type(s) for -: 'int' and 'tuple'
#print(a*b)         # (1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)

#int+set(-*)
a = 4
b = {1,2,3}
#print(a+b)         # TypeError: unsupported operand type(s) for +: 'int' and 'set'
#print(a-b)         # TypeError: unsupported operand type(s) for -: 'int' and 'set'
#print(a*b)         # TypeError: unsupported operand type(s) for *: 'int' and 'set'

#int+dict(-*)
a = 4
b = {"d1":1}
#print(a+b)     # TypeError: unsupported operand type(s) for +: 'int' and 'dict'
#print(a-b)     # TypeError: unsupported operand type(s) for -: 'int' and 'dict'
#print(a*b)     # TypeError: unsupported operand type(s) for *: 'int' and 'dict'

#str+float(-*)
#a = "hello"
#b = 3.2
#print(a+b)     # TypeError: can only concatenate str (not "float") to str
#print(a-b)     # TypeError: unsupported operand type(s) for -: 'str' and 'float'
#print(a*b)     # TypeError: can't multiply sequence by non-int of type 'float'

#str+bool(-*)
a = "abc"
b = True
#print(a+b)     # TypeError: can only concatenate str (not "bool") to str
#print(a-b)     # TypeError: unsupported operand type(s) for -: 'str' and 'bool'
#print(a*b)     # abc

#str+complex(-*)
a = "Ram"
b = 2+3j
#print(a+b)     # TypeError: can only concatenate str (not "complex") to str
#print(a-b)     # TypeError: unsupported operand type(s) for -: 'str' and 'complex'
#print(a*b)     # TypeError: can't multiply sequence by non-int of type 'complex'

#str+list(-*)
#a = "hello"
#b = [1,3,2]
#print(a+b)        # TypeError: can only concatenate str (not "list") to str
#print(a-b)        # TypeError: unsupported operand type(s) for -: 'str' and 'list'
#print(a*b)         # TypeError: can't multiply sequence by non-int of type 'list'

#str+tuple(-*)
#a = "Ram"
#b = (1,"abc")
#print(a+b)         # TypeError: can only concatenate str (not "tuple") to str
#print(a-b)          # TypeError: unsupported operand type(s) for -: 'str' and 'tuple'
#print(a*b)         # TypeError: can't multiply sequence by non-int of type 'tuple'

#str+set(-*)
#a = "hello"
#b = {1,2,3}
#print(a+b)         # TypeError: can only concatenate str (not "set") to str
#print(a-b)         # TypeError: unsupported operand type(s) for -: 'str' and 'set'
#print(a*b)         # TypeError: can't multiply sequence by non-int of type 'set'

#str+dict(-*)
#a = "hello"
#b = {"a": 1}
#print(a+b)         # TypeError: can only concatenate str (not "dict") to str
#print(a-b)         # TypeError: unsupported operand type(s) for -: 'str' and 'dict'
#print(a*b)         # TypeError: can't multiply sequence by non-int of type 'dict' 

#float+bool(-*)
#a = 2.3
#b = True
#print(a+b)             # 3.3    
#print(a-b)             # 1.2999999999999998
#print(a*b)             # 2.3

#float+complex(-*)
#a = 2.3
#b = 2+3j
#print(a+b)     # (4.3+3j)
#print(a-b)         # (0.2999999999999998-3j)
#print(a*b)         # (4.6+6.8999999999999995j)

#float+list(-*)
#a = 2.3
#b = [1,2,3]
#print(a+b)         # TypeError: unsupported operand type(s) for +: 'float' and 'list'
#print(a-b)         # TypeError: unsupported operand type(s) for -: 'float' and 'list'
#print(a*b)         # TypeError: can't multiply sequence by non-int of type 'float'

#float+tuple(-*)
#a = 2.3
#b = (1,2)
#print(a+b)         # TypeError: unsupported operand type(s) for +: 'float' and 'tuple'
#print(a-b)          # TypeError: unsupported operand type(s) for -: 'float' and 'tuple'
#print(a*b)         # TypeError: can't multiply sequence by non-int of type 'float'

#float+set(-*)
#a = 2.1
#b = {1,2}
#print(a+b)          # TypeError: unsupported operand type(s) for +: 'float' and 'set'
#print(a-b)          # TypeError: unsupported operand type(s) for -: 'float' and 'set'
#print(a*b)           # TypeError: unsupported operand type(s) for *: 'float' and 'set'

#float+dict(-*)
a = 2.3
b = {"a":1}
#print(a+b)          # TypeError: unsupported operand type(s) for +: 'float' and 'dict'
#print(a-b)          # TypeError: unsupported operand type(s) for -: 'float' and 'dict'
#print(a*b)         # TypeError: unsupported operand type(s) for *: 'float' and 'dict'

#bool+complex(-*)
#a = True
#b = 2+3j
#print(a+b)     # (3+3j)
#print(a-b)     # (-1-3j)
#print(a*b)     # (2+3j)

#bool+list(-*)
a = True
b = [1,2]
#print(a+b)          # TypeError: unsupported operand type(s) for +: 'bool' and 'list'
#print(a-b)          # TypeError: unsupported operand type(s) for -: 'bool' and 'list'       
#print(a*b)         # [1, 2]

#bool+tuple(-*)
#a = True
#b = (1,2)
#print(a+b)          # TypeError: unsupported operand type(s) for +: 'bool' and 'tuple'
#print(a-b)            # TypeError: unsupported operand type(s) for -: 'bool' and 'tuple'
#print(a*b)           # (1, 2)

#bool+set(-*)
#a = True
#b = {1,2}
#print(a+b)          # TypeError: unsupported operand type(s) for +: 'bool' and 'set'
#print(a-b)          # TypeError: unsupported operand type(s) for -: 'bool' and 'set'
#print(a*b)           # TypeError: unsupported operand type(s) for *: 'bool' and 'set'

#bool+dict(-*)
#a = True
#b = {"q":4}
#print(a+b)     # TypeError: unsupported operand type(s) for +: 'bool' and 'dict'
#print(a-b)     # TypeError: unsupported operand type(s) for -: 'bool' and 'dict'
#print(a*b)     # TypeError: unsupported operand type(s) for *: 'bool' and 'dict'

#Complex+list(-*)
#a = 2+3j
#b = [1,2]
#print(a+b)      # TypeError: unsupported operand type(s) for +: 'complex' and 'list'
#print(a-b)      # TypeError: unsupported operand type(s) for -: 'complex' and 'list'
#print(a*b)     # TypeError: can't multiply sequence by non-int of type 'complex'

#Complex+tuple(-*)
a = 2+3j
b = (1,3)
#print(a+b)      # TypeError: unsupported operand type(s) for +: 'complex' and 'tuple'
#print(a-b)       # TypeError: unsupported operand type(s) for -: 'complex' and 'tuple'
print(a*b)

#Complex+set(-*)
#a = 2+3j
#b = {1,2}
#print(a+b)         # TypeError: unsupported operand type(s) for +: 'complex' and 'set'
#print(a-b)         # TypeError: unsupported operand type(s) for -: 'complex' and 'set'
#print(a*b)          # TypeError: unsupported operand type(s) for *: 'complex' and 'set'

#Complex+dict(-*)
#a  = 4+4j
#b = {"a":3}
#print(a+b)             # TypeError: unsupported operand type(s) for +: 'complex' and 'dict'
#print(a-b)             # TypeError: unsupported operand type(s) for -: 'complex' and 'dict'
#print(a*b)             # TypeError: unsupported operand type(s) for *: 'complex' and 'dict'

#list+tuple(-*)
#a = [5,6]
#b = (3,4)
#print(a+b)         # TypeError: can only concatenate list (not "tuple") to list
#print(a-b)         # TypeError: unsupported operand type(s) for -: 'list' and 'tuple'
#print(a*b)         #TypeError: can't multiply sequence by non-int of type 'tuple'

#list+set(-*)
#a =[5,6]
#b = {3,4}
#print(a+b)     # TypeError: can only concatenate list (not "set") to list
#print(a-b)     # TypeError: unsupported operand type(s) for -: 'list' and 'set'
#print(a*b)     # TypeError: can't multiply sequence by non-int of type 'set

#list+dict(-*)
#a = [5,6]
#b = {"a":4}
#print(a+b)     # TypeError: can only concatenate list (not "dict") to list
#print(a-b)     # TypeError: unsupported operand type(s) for -: 'list' and 'dict'
#print(a*b)     # TypeError: can't multiply sequence by non-int of type 'dict'

#tuple+set(-*)
#a = (5,6)
#b = {3,4}
#print(a+b)         # TypeError: can only concatenate tuple (not "set") to tuple
#print(a-b)         # TypeError: unsupported operand type(s) for -: 'tuple' and 'set'
#print(a*b)         # TypeError: can't multiply sequence by non-int of type 'set'

#tuple+dict(-*)
#a = (1,2)
#b = {"r":3}
#print(a+b)      # TypeError: can only concatenate tuple (not "dict") to tuple
#print(a-b)     # TypeError: unsupported operand type(s) for -: 'tuple' and 'dict'
#print(a*b)     # TypeError: can't multiply sequence by non-int of type 'dict'

#print("*"*5)       # *****

#a = [1,2,3]
#print(a*4)         # [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]

#a = "rakhi"
#print(a*2)     # rakhirakhi


























