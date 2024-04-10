
# Operators
# Operatores are the special symbols which are used to carry out arithmetical and logical operations.
# Like in any other language pyhothon also has it's set of operators
    # 1. Arithimetic Operators
    # 2. Logical Opertors
    # 3. Relational Operators 
    # 4. Assigment Operators
    # 5. Membership Operators
    # 6. Identity Operators 

# 1. Arithimetic Operators (+, -, /, *, **, %)

a=1 # Python Statement
b=2 # Python Statement
result = a+b
print("The result of the sum is", result)

result=b**2
print(result)

result = 5 % 2
print(result) #1

result =5 / 2
print(result) #2.5

# 2. Relational / Comparion Operators(>,<, >=, <=, ==, !=)
# The result of comparision operatons are either True or False
a=20
b=15
print(a>b)#True
print(a<b)# False
print(a==b) # False 
print(a>=b) # True
print(a <=b) # False
print(a !=b) # True

# 3. Logical Operatora (and, or, not)
# The result of logical operatons is either True or False
# AND
print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False 

# OR 

print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) # True

# NOT 
print(not True) # False
print(not False) # True

a=1
b=15
c=15
if a>b or b==c:
    print("Hello World")

# 4 Assignment Operator ( =, +=, -=,*=,/=)
    message="Hello World"
    b=5
    b=b+5
    print(b)# 10
    b+=5
    print(b)#15
    b-=5
    print(b)#10

# 5. Membership Operator ('in' and 'not in')
# The result of membership operation is also True or False
# Memnbership operatorsare used in the sequential data (iterables) e.g, list, array,tuple etc.
vowels=['a','e','i','o','u']
print('a' in vowels) #True
print('A'in vowels) # False
print('A'not in vowels) # True
print("a" not in vowels) # False 












# Relational Oper
a = 1
b = 15
c = 15
if a > b or b == c:
    print("Hello World")

