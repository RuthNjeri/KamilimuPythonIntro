# This is python 101
"""
this is how
you write multiple comments
"""
print("Hello world, a string in double quotes")
print('This is a string in single quotes')

#variables

name = "Ruth"
age = 58

print("Hello " , "another string",name)
print("Hello my name is",name ,"and my age is " ,age)


#Arithmetics
print("5**1=",5**1)
print("5-1+3*4=",5-1+3*4)
print("(5-1+3)*4=",(5-1+3)*4)

#DataTypes: LIST

shopping_list = ["pen"]
print (shopping_list)
shopping_list.append("tomatoes")
shopping_list.append("onions")
shopping_list.append("bread")
shopping_list.append("2")

del shopping_list[4]

print(shopping_list)


#tuple
myTuple=(1,2,3,4,4)


myTupleList= list(myTuple)
myTuple= tuple(myTupleList)

print(myTuple)

#Loop
age = input("Enter your age ")

age2 = int(age)

if age2<18 or age2==None:
	print("You cannot vote")
elif age2>18:
	print("you can vote")
else:
	print("you have not entered your age")
