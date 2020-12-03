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

