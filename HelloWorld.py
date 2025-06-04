print('hello world')
print(25)             #25 is integer 
print('john')         #john is a name 
# comments dont interrupt in the code 
number = 10 
number2=  15 
site_name = 'programiz.com'
site_name2 = 'apple .com'
print(number)
print(number2)
print(site_name)
print (site_name2)
#this is assigning a value to a variable 
a = x = 25
b = y = 30 
print (x)
print (y)
print(a)
print(b)
a, b , c = 5, 3.2, 'hello'     #assigning multiple variables 
print(a )
print(b)
print(c)
site1 = site2 = 'programiz.pro'
print(site1)
p = site1
q = site2
print(p)
print(q)
x  = 9 + 9
print(x)
# collection literals 
#list literals 
fruits = ['apple',"mango","orange"]
print(fruits )
#tuple literals 
numbers = ['1','2', '3']
print(numbers )
#dictionary literals 
alphabets = ['a:' 'apple','b:' 'ball','c:' 'cat']
print(alphabets)
#set literals
vowels = {'a', 'e', 'i','o ', 'u'}
print(vowels)
#phython operators 1) arithemetic operators # there  are 6 arithmetic operators
a = 67
b = 43
print('sum:' , a + b)
print('diffrence:' , a - b)
print('product:' , a * b )
print('division:' , a / b)
print("Floor Division:" , a // b)
print('Modulo:' , a % b )
print("power:" , a ** b)
# 2} phython assigning operators 
a = 85            # assignment  operators 
b = 56
a += 3            #additoon assisgnment operators 
b -= 8            #substarction assignment operators 
print(a)
print(b)
x = 77
y = 88
x *= 7            #multiplication assignment operator 
y /= 2            #division assignment operator
print(x)
print(y)
p = 38 
q = 25
#logical operators 
a = 22
b = 33
print((a<b)and (b>a)) # true 
print((a>b)and(b<a)) #false 
#equal to operator 
print("a = b = ", a == b)
#not equal to operator 
print('a!=b', a!=b)
# greater than operator 
print('a>b', a>b)
#less than operator
print('a<b', a<b)
#greater than or equal to operator 

# # Turtle flower 
# import turtle
# t  = turtle. Turtle()
# turtle.bgcolor("black")
# t.speed(0)
# colors = ["red", "yellow", "blue", "green", "purple", "orange"]
# for i in range(300):
#  t.pencolor(colors[i % 6])
#  t.forward(i * 2)
# t.right(61)
# turtle.do
# ending sequence character"\""
print('myself Faisal \n iam miserable now ')
# like this iam miserable will be in the second line 
# now sep = "" , end = "" and 
print("hey", 6 , 7 , 8 , sep= "-")
# there is a hyphen between the words we choose
print('hey', 6 , 9 , 0 , sep="-" , end='0000\n')
print('harry potter') 
# we can see that there is hyphen (-) and it endeed with 0000 and if we add \n there willl be a paragraph change in next command 
# about strings 
# multiline strings = ''''''
a = """there was a apple and i want to eat that 
iam so craving for it
iam so hungry right now """
print(a)

print(a[0])
# loop character 
# we use for character in a
for character in a: 
    print(character)
b = (str(input('enter your name:' )))
print("hello ," ,str(b) )
print ('how can we help you ', b)

