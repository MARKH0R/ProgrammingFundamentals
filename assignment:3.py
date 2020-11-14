### YOUR CODE FOR openLocks() FUNCTION GOES HERE ###
def openLocks(number_of_lockers,number_of_students):
    if number_of_students<0 or number_of_lockers<0:
        return None
    elif number_of_students==0 or number_of_lockers==0 :
        return 	0
    
    import math
    lockers=number_of_lockers
    students=number_of_students
    lockersOpen=int(math.sqrt(lockers))
    for a in range(1,lockers+1):
        a = False;
        for b in range (1,students+1):
            if a%b == 0:
                a= not a
    lockersOpen = int(lockersOpen)    
    return ( lockersOpen)
### End OF MARKER
""" 
If there are 100 lockers, there are
100 people and each of the 100 goes through the hallway turning
lockers that are multiples of their own number

for example:-
              person #
            --------------------
  locker #  1 2 3 4 5 6 7 8 9 10
     1      +
     2      + -
     3      +   -
     4      + -   +
     5      +       -
     6      + - +     -
     7      +           -
     8      + -   +       -
     9      +   -           +
    10      + -     +         -

I used "+" to mean "opened" and "-" for "closed".

Notice that each time a locker is "touched" it changes from open to 
closed or vice versa.  So in order to end up open, it has to be 
touched an odd number of times
"""




### YOUR CODE FOR mostTouchableLocker() FUNCTION GOES HERE ###
def mostTouchableLocker(number_of_lockers,number_of_students):
    if number_of_students==0 or number_of_lockers==0:
        return 0
    if number_of_lockers<0 or number_of_students<0:
    	return None
    lockers=[number_of_lockers]
    for i in range (1, number_of_lockers):
        lockers.append(0)
    for j in  range (1, number_of_students):
        if j%2==0:
            lockers[i] = lockers[i] + 1
    return max(lockers)    





#### End OF MARKER


