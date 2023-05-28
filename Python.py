# Python Cheat Sheet
# Numbers and Aritmetic
# Python data types of numbers
type(1) # int 
type(-10) # int
type(0) # int
type(0.0) # float
type(2.2) # float
type(4E2) # float - 4*10 to the power of 2

# Arithmetic
10 + 3 # 13
10 - 3 # 7
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
