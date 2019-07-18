#In this tutorial i will be demonstrating how to us genartors and save both time and memory.
#the first syntax, we will be using the return keyword while in the second we will be using the generator function, yield ,
#DIY too

#Note: Make sure you comment either in case you want to run one. 


#Using the return keyword 

def create_cubes(n):
	result = []

	for x in range(n):
		result.append(x**3)

	return result

#Uing the Genrator function

def create_cubes(n):

	for x in range(n):
		
		yield x**3

		

