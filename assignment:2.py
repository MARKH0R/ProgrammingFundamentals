### YOUR CODE FOR chocolatePrice() FUNCTION GOES HERE ###
def chocolatePrice(ali_budget,bashir_budget):

    if type(ali_budget)==str or type(bashir_budget)==str:
        return "Not Possible"
    elif ali_budget==0 and bashir_budget==0:
        return "Not Possible"
    elif ali_budget > bashir_budget:
        smaller = bashir_budget
    else:
        smaller = ali_budget
    
    for i in range(1, smaller+1):
        if((ali_budget% i == 0) and (bashir_budget% i == 0)):
            z= i        
    
    return z
    


#### End OF MARKER

"""here in this program we calculate choclate price but we have some rule and regulation are as following 
	1. The first constraint is to spend all their money in buying chocolates so no change
    is left.
	2. The second constraint on them is that each one of them has to buy the same
    chocolate. This will ensure that both Ali and Bashir will pay the same price for 1
    chocolate.
	3. The last of these constraints is that both have to buy the chocolate with the
    maximum price.
so in above program we us somme if else statements which stop or elert the user to 'do not enter string value and zero value' because price could not be in the form of string and zero. 
After this we use the HIghest Commen Factor (HCF) in which we will check if one is greater then other then we assign other value into 'smaller' variable. And vice varsa then after assigning the values we will use the for loop that will iterate to the value which we assign to the smaller value further in 'for loop' we use 'if' and in if conditional statement we take modules of both the entered values by 'i' and if both were true the that value will be assign to the new variable 'z'.
In last our function will return "z". Which is requiredd answer."""

### YOUR CODE FOR calculateProfit() FUNCTION GOES HERE ###
def calculateProfit(ali_budget,bashir_budget):
    
    if type(ali_budget)==str or type(bashir_budget)==str:
        return "Not Possible"
    elif ali_budget==0 or bashir_budget==0:
        return "Not Possible"
    elif ali_budget<0 or bashir_budget<0:
        return "Not Possible"
    a=ali_budget-int(ali_budget)
    if a >=0.5:
        ali_budget = int(ali_budget+1) 
    else :
        ali_budget = int (ali_budget)
    
    b=bashir_budget-int(bashir_budget)
    if b>=0.5:
        bashir_budget = int (bashir_budget+1)
    else:
        bashir_budget = int (bashir_budget)
           
    if ali_budget>bashir_budget:
    
        x = ali_budget*(3/2)-ali_budget
        y = bashir_budget*2-bashir_budget

        return y
    else :

        x = ali_budget*2-ali_budget
        y = bashir_budget*(3/2)-bashir_budget
        if x>y:
        	return x
        else :
        	return y	
        	
#### End OF MARKER
"""  In secound function we discuss the profit that they have get individule as above we use round of function which will round of float value into integer value.then for for greater value we multiply the smaller by '2' and greater value by '3/2' and vice varsa. 
And in last we return the maximum value or profit that one of them get.  """

