#Numbers
Varnum =123
pi= 3.14159

#Strings
varString="Hello World"
varText="This is a string"

#Lists
varlist=["abc", 123]

#Tuples
varTuple= 'abc',123, "HELLO"

#Dictionaries
var=3
varDict={'first':1, '2':'2nd',3:var}
varDict={}
varDict['First']=1
varDict['2']='2nd'
varDict[3]= var

#Arithmetic
a=5+3
print(a)
#Subtraction
b=5-3
print(b)
#Multiplication
c=5*3
print(c)
#Exponent
d=5**3
print(d)
#Division
e=5/3
print(e)
f=5%3
print(f)
g=5//3
print(g)


#Arithmetic
#>Increlment/Decrement
h=5
h+=1
print(h)
#Decrement
i=5
i-=1
print(i)
#String Concatenation
j='Hello'+'World'
print(j)
#Complex Expressions
k= 3+ 5- 6* 2/4
print(k)

#Boolean Condtions
x= True
print('\n')

if x:
    print("var is True")
    
else:
    print("var is False")
#> var x is True
#String Conditions
x="Hello World!"
if x== 'Hello World!':
    print("var x is Hello World!")
else:
    print("var x is not Hello world!")

#>var x is Hello World!    

#Numerical Conditions
x= int(10)
if x=='10':
    print("var x is a string")
elif x==10:
    print("var x is an integer")
else:
    print("var x is not of the above")
#>var x is an integer

print('\n')

#Loops
#For Loops
for var in range(0,5,2):
    print(var)
#While loops
var=0
while var<5:
    print(var)
    var+=2
#Nested Loops
x=0
while x < 5:
    for y in range (0, x):
        print(y, end='')
    x+=1
    print()
    
print('\n')
    
#Lists
pi=3.14159
varlists= [1, 2, 'A', 'B', 'Hello!', pi]
print(varlists[0])

print(varlists[4])

varlists.append('World!')
print(varlists[6])

len(varlists)
print(len(varlists))
print(varlists[5])

varlists.remove(pi)
print(varlists[5])

#Dictionaries

var="Hello World!"
varDict={'first':123, 2: 'abc', '3' :var, 4: ['lista', 'listb']}

print(varDict[2])

print(varDict['3'])

print(varDict[4])

print(varDict[4][1])

len(varDict)
print(len(varDict))

print('\n')
#Generators

def gen_num_up_to(n):
    num=0
    while num < n:
        yield num
        num +=1
print (gen_num_up_to(5))

varlist= gen_num_up_to(5)
print([var for var in varlist])

def gen_num_up_to(n):
    num=0
    while num < n:
        yield num
        num +=2
varlist= gen_num_up_to(5)
print([var for var in varlist])

varlist= range( 0, 5 ,2 )
print([var for var in varlist]) 
 
print('\n')

varlist=[1, 2, 3, 4, 5, 6, 7 ,8, 9 ,10]
print(varlist[:5])

print(varlist[5:])

print(varlist[:-2])

print(varlist[-2:])

print(varlist[2:-2])

print(varlist[2:8:2])   

print('\n')
def remainder(n,m):
    while True:
        if n - m <0:
            return n
        else:n = n - m
        
print(remainder(10,4))