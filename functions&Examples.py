"""fuction which find even and odd number"""

def even_odd(x):
    if x%2==0:
        return "the number is even"
    else :
        return "number is odd"
 
 
 # ending of function 


"""the function which check wather the number is negative or positive  """



def _P_N_number(x):    
    if x>0:
        return "number is positive"
    elif x==0:
        return "nither positive nor negative"
    else:
        return "number is negative"


# ending of function 


"""function to find greater and smaller number """


def differenceGandL(a,b):
    if a>b:
        return (a,"is grater then",b)
    elif b>a:
        return (b,"is grater then",a) 
    else:
        return "both numbers are equal"


# ending of function         


"""function to find fibonachi number. You Have to give a number whome series you want. """


x=int(input('enter a number to find fibonacci series\t:' ))
a=0
b=1
print (a,b)
for i in range (1,x):
    z=a+b
    a=b
    b=z
    print (z)


# ending of function                


"""the function which seprate the even and odd number form series. In this functionyou have to give a number which series you want. Then it will seprate odd and even number from list. FOR Example we give 100 to function it will make a list of 100 numbers and then it will seprate odd and even numbers from the list

print(fun(100)) 

OUTPUT:

([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100], [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99])

 """        
def fun(x):
    a=[]
    b=[]
    c = []
    for i in range(1,x+1):
        if i%2==0:
            a.append(i)
        elif not(i%2==0):
            b.append(i)
    return a,b



# ending of function 


"""this function print the age of any person you need to give name and age as perimeter """
def printinfo (name ,age=35):
    print ("Name",name)
    print ("Age",age)
    return

# ending of function 



"""
* collects all the positional arguments in a tuple.
** collects all the keyword arguments in a dictionary.
this function will add the mamber of tuple as we pass the tuple as an argument, so in this function will add or return the sum  of the given tuple
"""
def plus (*arg):
    "sum"
    return sum (arg)
"""print (plus(1,2,3))
OUTPUT: 6
"""

# ending of function 


"""function which inter change tow strings"""

x=input("enter any string:\n")
z=input("enter an other string to swapwith frist:\t")
y=x
x=z
z=y
print( x ,z) 

# ending of function 

"""Write a Python program to get the Python version you are using.
for this we use library of sys"""
import sys
print("python version")
print (sys.version)
print ("python version info")
print (sys.version_info)

# ending of function 

"""Write a Python program to display the current date and time.
#for this we import date and time library"""
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

# ending of function 

"""Write a Python program which accepts the radius of a circle from the user and compute the area"""
pi=  3.1415
def ares_of_circle(radius):
    area= pi* radius**2
    return area
# ending of function 

"""Write a Python program which accepts the user's first and 
last name and print them in reverse order with a space between them"""
x=input("enter frist name:\t")
y= input('enter last name:\t')
z=x
x=y
y=z
print (x , y)

# ending of function 

"""Write a Python program which accepts a sequence of comma-separated numbers
from user and generate a list and a tuple with those numbers"""

values = input("Input some comma seprated numbers : ")
list = values.split(",")

print('List : ',list)
print('Tuple : ',tuple)

# ending of function 

""" in this function the user will deposit or withdraw money every time this function will ask the user to add or withdraw money 
when he deposit the money will be add in the account and when he withdraw the amount will be deducted for his or her bank account  """


    while True:
        var=input ("press D to Deposit, W for withdraw or Q for quit:")	
        if var=="D" :                

            x= int (input("enter Deposit amount : "))
            print ("D = ",x) 
            varsum = x+x 
        elif var== "W" :
            y= int (input("enter withdraw amount : "))
            print ("W = ",y)
            add = varsum-y
        elif var =="Q":
            break
        
        
# ending of function 

""" function converts pound into gram """
def convert (x):
	# 1 pound = 0.454 kilo
	# 1 pound = 453.59 gram
	y = 0.456*x
	z = 453.59*x
	return y,z
# ending of function 	
	 
"""function for volume and circumference """
from math import pi
def function (radius , hight ):
	c=2*pi*radius
		
	V=pi *pow(radius,2)*hight
	return c,V

# ending of function     

""" function for linear relationship """
k = 2.5
def linear_function(x):
	y= k*x
	return y
# ending of function 

""" This function will calculate the table of which the user ask and then print   """
a=int(input("table for :\t"))
c=int(input("enter the length of your table: \t"))
for b in range(1,c+1):
    z=a*b
    print ( a,"*",b, "=",z)

# ending of function 



"""this function will rounde off the any float number into integer """
def convert(x):
    a=x-int(x)
    if a >=0.5:
        return int(x+1) 
    else :
        return int (x)

# ending of function

"""This function will return the maximum number between two numbers """
def maxno (a,b ):
    if a>b:
        return a 
    else :
        return b
# ending of function


""" This function is made for uni/school/college students , which check wather student have following things
1.mask 
2. id card
3. dressing 

"""
def getcheck(mask= input ("enter your answer in True or False:\t  "),ID_card = input ("enter your answer in True or False:\t  "),Dressing = input ("enter your answer in True or False:\t  ")):
    
    if mask== True:
        if ID_card == True:
            if Dressing == True:
                print ("\t\t\tpass let this enter in universty \n \t \tthank you for your coprate")
            else:
                print ("your dressing is not proper")
        else :
            print ("Your ID CARD is missinng \n bring it with you \n thank you")
    else :
        print ("sorry your mask is missing \n \"NO MASK? NO ENTRY!\" \n bring it with you")
            
# ending of function

"""This function will fund you the highest common factor of two numbers"""
def calculatehcf(x, y):

# choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            z = i 
    print(z) 
    
# ending of function

"""
2.Write a Python functionto get unique values from a list.(DONOT useSETS)
	a.Your function take list as a parameter.
	b.Returna new_list having unique numbers.
"""

def unique_value(x):
    m=[]     #empty list for new list whish will store unique numbers 
    
    
    for i in x:
        
        if i not in  m:
            m.append(i)
        
    return m

# ending of function        

""" this function will sort the list in decending order"""
def bubble_sort(z): 
   s= True    # the loop will run atlest once 
    while s:
    	s=False     
        for i in range(len(z)-1):
            if z[i]<z[i+1]:       #if frist index is less then secound index in list this will replace but in case frist inder
                                  # is greater then secound it will not replace its position
                z[i] , z[i+1] =z[i+1] ,z[i]    # it will replace the oder of two numbers in list
                s= True   #it will keep iterate the loop 
     # function for decending order bubble sort            

     # function for accending order bubble sort            

def bubble_sort(z): 
   s= True    # the loop will run atlest once 
    while s:
    	s=False     
        for i in range(len(z)-1):
            if z[i]>z[i+1]:       #if frist index is greater then secound index in list this will replace 
                z[i] , z[i+1] =z[i+1] ,z[i]    # it will replace the oder of two numbers in list or in short this process is called swaping the variable
                s= True   #it will keep iterate the loop       
  
# ending of function 


""" function for findng the length of list it could be used for string."""
def list_length(a):
    count=0
    for i in a:          
        count+=i
    print( count)		# Print the length of the give peremeter

# ending of function 

"""
Question#02
Write a function that calculates the sum of all the elements of a given list.
Name the function 'sum_listand' the list should be passed to the function as a parameter.
Assuming the list either contains integers or floats or both.

"""

def sum_listand(x=[]):
    a=0
    n=len(x)
    
    for i in x:
        a+=i
    return a    
        
# Question:5 Write a function that takes two lists and returns True if they have at least one common member.

def  common_list(a,b):
    for x in a :
        for y in b:
            if x==y:
                return True
# ending of function 
"""
Question#06
Write a function that takes an integer as a parameter and returns the sum of digits in that integer.
"""
def intsum(x):
    x=str (x)
    j=0
    for i in  x:
        j+=int(i)
    return j    
# ending of function        
           


