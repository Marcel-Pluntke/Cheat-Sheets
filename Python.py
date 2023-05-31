# Python Cheat Sheet
# Numbers and Aritmetic
# Python data types of numbers
type(8) # int 
type(-90) # int
type(0) # int
type(0.6) # float
type(4.2) # float
type(4E2) # float - 4*10 to the power of 2

# Arithmetic
10 + 5 # 15
10 - 5 # 5
10 * 3 # 30
10 ** 3 # 1000
10 / 3 # 3.3333333333333335
10 // 3 # 3 --> floor division - no decimals and returns an int
10 % 3 # 1 --> modulo operator - return the reminder. Good for deciding if number is even or odd

# Basic Functions
pow(5, 2) # 25 --> like doing 5**2
abs(-50) # 50
round(5.46) # 5
round(5.468, 2)# 5.47 --> round to nth digit
bin(512) # '0b1000000000' --> binary format
hex(512) # '0x200' --> hexadecimal format

# Converting Strings to Numbers
age = input("How old are you?")
age = int(age)
pi = input("What is the value of pi?")
pi = float(pi)

# Strings
type('Hellloooooo') # str
'I\'m thirsty'
"I'm thirsty"
"\n" # new line
"\t" # adds a tab
'Hey you!'[4] # y

name = 'Marcel'
name[4] # e
name[:] # Marcel
name[1:] # arcel
name[:1] # M
name[-1] # l
name[::1] # Marcel
name[::-1] # lecraM
name[0:10:2]# Mre
# : is called slicing and has the format [ start : end : step ]

'Hi there ' + 'Viewer' # 'Hi there Viewer' --> This is called string concatenation

'*'*10 # **********

# Basic Functions
len('turtle') # 6
# Basic Methods
' I am alone '.strip() # 'I am alone' --> Strips all whitespace 
characters from both ends.
'On an island'.strip('d') # 'On an islan' --> # Strips all passed 
characters from both ends.
'but life is good!'.split() # ['but', 'life', 'is', 'good!']
'Help me'.replace('me', 'you') # 'Help you' --> Replaces first with 
second param
'Need to make fire'.startswith('Need')# True
'and cook rice'.endswith('rice') # True
'bye bye'.index(e) # 2
'still there?'.upper() # STILL THERE?
'HELLO?!'.lower() # hello?!
'ok, I am done.'.capitalize() # 'Ok, I am done.'
'oh hi there'.find('i') # 4 --> returns the starting index position of the first occurrence
'oh hi there'.count('e') # 2

# String Formatting
name1 = 'Andrei'
name2 = 'Sunny'
print(f'Hello there {name1} and {name2}') # Hello there Andrei and 
Sunny - Newer way to do things as of python 3.6
print('Hello there {} and {}'.format(name1, name2)) # Hello there Andrei and 
Sunny
print('Hello there %s and %s' %(name1, name2)) # Hello there Andrei and Sunny --> you can also use %d, %f, %r for integers, floats, string 
representations of objects respectively

#Palindrome check
word = 'reviver'
p = bool(word.find(word[::-1]) + 1)
print(p) # True

#boolean
bool(True)
bool(False)
# all of the below evaluate to False. Everything else will evaluate to True in 
Python.
print(bool(None))
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool([]))
print(bool({}))
print(bool(()))
print(bool(''))
print(bool(range(0)))
print(bool(set()))

# lists
my_list = [1, 2, '3', True]# We assume this list won't mutate for each example 
below
len(my_list) # 4
my_list.index('3') # 2
my_list.count(2) # 1 --> count how many times 2 appears
my_list[3] # True
my_list[1:] # [2, '3', True]
my_list[:1] # [1]
my_list[-1] # True
my_list[::1] # [1, 2, '3', True]
my_list[::-1] # [True, '3', 2, 1]
my_list[0:3:2] # [1, '3']
# : is called slicing and has the format [ start : end : step ]

# Add to List
my_list * 2 # [1, 2, '3', True, 1, 2, '3', True]
my_list + [100] # [1, 2, '3', True, 100] --> doesn't mutate original list, creates new one
my_list.append(100) # None --> Mutates original list to [1, 2, '3', True, 100] # Or: <list> += [<el>]
my_list.extend([100, 200]) # None --> Mutates original list to [1, 2, '3', True, 100, 200]
my_list.insert(2, '!!!') # None --> [1, 2, '!!!', '3', True] - Inserts item at index and moves the rest to the right.
' '.join(['Hello','There'])# 'Hello There' --> Joins elements using string as separator.

