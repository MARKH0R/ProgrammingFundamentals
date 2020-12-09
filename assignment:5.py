## IMPORTS GO HERE
import os
## END OF IMPORTS


#### YOUR CODE FOR text_count FUNCTION GOES HERE ####
def text_count(directory , name, perimeter = False,fourth_perimeter = False):
	

	words=0    
	count=0
	low_words=0
	filename = os.path.join(directory, name)
	f=open(filename,"r")
	
	if perimeter== False and fourth_perimeter == False:

		d = f.read().split()
		for i in d:
		    words+=1
		return words
	
	if perimeter == True:    
		x= f.read().split()

		for i in x:
		    w=i
		    if w.islower() == True :
		        low_words+=1
		return low_words
	
	
	if fourth_perimeter == True:
		z=f.read()
		    
		for i in z:
			count += len (i)
	return  count 
	f.close()



#### End OF MARKER

#### YOUR CODE FOR copy_lines FUNCTION GOES HERE ####
def copy_lines(input_file_path,Output_file_path,lines):
	i_f= open (input_file_path,"r")
	o_f= open (Output_file_path,"w")
	
	q=0
	for i in range (0: lines):
		if q+1<lines:
			line=i_f.readline().strip()
			o_f.write(line)
		if q+1== lines:
			line= i_f.read()
			o_f.write(line.strip())
		q+=1

	i_f.close()
	o_f.close()

#### End OF MARKER




