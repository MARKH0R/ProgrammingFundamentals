### YOUR CODE FOR calculateArea() FUNCTION GOES HERE ###
def calculateArea(length,width):
    area = length * width
    return area

#### End OF MARKER

###hear in this code we calculate the Area of plot then we check how much number of tiles are going to fit in the given area for
###which we take mode of the pw to twand then use logical opeartor then again take mode pl to tl and use logical operator "and" then
#
#
#
#
####
### YOUR CODE FOR checkTilesFit() FUNCTION GOES HERE ###
def checkTilesFit(plot_width, plot_length, tile_width, tile_length):
    pw = plot_width
    pl =plot_length
    tw =tile_width
    tl =tile_length
    if ((pw%tw))==0 and ((pl%tl))==0 and ((pw%tl))==0 and ((pl%tw))<=0 :
    	ap=pw*pl
    	at=tw*tl
    	ap/at==0
    	return False
    elif (pw*pl)==(tw*tl):
    	return True
    elif pw<0 or pl<0 or tw<0 or tl<0:
    	return False	
    else :
    	return False			

#### End OF MARKER
##in last we gust calculate the number of tiles which we use in plot. for which we make showr that user does not enter the alphabet 
##as well as value that usergiving us do not equal to zero. the program check both of the conditions we calculate area of plot and 
#area of tiles and devide both of them.before calculating area we will call the secound function it is equal to True then the 
#function will calculate the area other wise it return not possible ot user.
#
### YOUR CODE FOR calculateTiles() FUNCTION GOES HERE ###
def calculateTiles(plot_width, plot_length, tile_width, tile_length):
    pw = plot_width
    pl =plot_length
    tw =tile_width
    tl =tile_length
   
    
    if type (pw) is str or type(pl) is str or type(tw) is str or type(tl) is str:
        return ("Invalid Input")
    elif(pw==0 or pl==0 or tw==0 or tl==0):
        return None
    elif checkTilesFit(plot_width, plot_length, tile_width, tile_length) == True:
    	Ap = pw*pl
    	At = tw*tl
    	total = Ap/At
    	return int (total)
    else:	 
        return "Not Possible"
    
        
#### End OF MARKER

