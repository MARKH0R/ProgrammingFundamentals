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
           

