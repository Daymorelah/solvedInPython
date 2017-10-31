
# Import the math library to be able to use the 'sqrt' function
import math

'''
Question One
Write a function called isSquare() that takes a number and tells if the number is a perfect square
or not.
'''
def isSquare(number):
	if ( (type(number) != int) and (type(number) != float) ):						#check if the input is not a number
		print('Please enter an integer')																	#Prompts user to input an integer
	else:
		if(number < 1):
			print ('Please enter a number greater than or equal to one ')		#Promts user to enter a number greater than or equal to one
		else:
			squareroot = math.sqrt(number)
			result = squareroot % 10																				#check if the input is an integer or a float
			if (result == int):
				print('The number you entered, '+number+', is a perfect square') #Prompts user input is a perfect square
			else:
				result =type(squareroot)
				print ('The number, '+str(number)+', is not a perfect square')		#Prompts user input is not a perfect square
	return
			

'''
Question 3:
Write a function that takes a list of values and returns a dictionary in the format below
Sample Input:
['book', 3 , pin, 3.5]
sample output:
{
string: ['book','pin'],
number: [3,5]
}
'''	
def questionThree(inputValues):
	stringList,integerList,floatList = ( [] for i in range(3) )	#Creates three empty list
	result = {}																									#Creates an empty dictionary
	for i in inputValues:																				#Loops through each element of the array
		if( type(i) == str):																			#checks if element is a string
			stringList.append(i)																		#Adds element to the string list if element is a string
		elif( type(i) == int):																		#checks if element is an integer
			integerList.append(i)																		#Adds element to the integer list if element is an integer
		elif( type(i) == float):																	#checks if element is a float
			floatList.append(i)																			#Adds element to the float list if element is a float
	result['string'] = stringList																#Adds list to dictionary
	result['integer'] = integerList															#Adds list to dictionary
	result['float'] = floatList																	#Adds list to dictionary
	print result																								#Prints result to the console
	return																											


'''
Write a function called 'getEncryptedText()' that takes a random string and generates a
password out of it and another function called 'getDecryptedText()' that takes the output of the
'getEncryptedText()' function and returns the original string.
'''
def questionTwo(textToPassword):
	
	textLength = len(textToPassword)					#Determines the lenght of the input
	password = []															#Creates an empty list
	
	def getEncryptedText(textToPassword):			
		for i in range(textLength):							
			password.append(textToPassword[i])		#Converts the input string into a list
		print password
		password.append('z')										#Appends 'z' to the end of the list
		password.reverse()											#Reverses the elements in the list
		password.insert((textLength-3),'k')			#Inserts 'k' into the 'textLength-3' positionin the list
		password.append('t')										#Appends 't' to the end of the list
		password.insert(2,'x')									#Inserts 'x' into the third element in the list
		password.reverse()											#Reverses the elements in the list
		password.append('q')										#Appends 'q' to the end of the list
		password.insert((textLength/2),'j')			#Inserts 'j' into the 'textLength/2' positionin the list
		password.reverse()											#Reverses the elements in the list
		print password
		
	def getDencryptedText():
		password.reverse()											#Reverses the elements in the list
		password.pop(textLength/2)							#Removes the element at the position 'testLength/2' in the list
		password.pop(len(password)-1)						#Removes the element at the position 'len(password)-1' in the list
		password.reverse()											##Reverses the elements in the list
		password.pop(2)													#Removes the third element in the list
		password.pop(len(password)-1)						#Removes the element at the position 'len(password)-1' in the list
		password.pop(textLength-3)							#Removes the element at the position 'testLength-3' in the list
		password.reverse()											##Reverses the elements in the list
		password.pop(len(password)-1)						#Removes the element at the position 'len(password)-1' in the list
		print password
		
	getEncryptedText(textToPassword)
	getDencryptedText()

#questionTwo('helloworld')
#isSquare(10)
#questionThree(["book",3,'pin',4,2.1,2,2,'we',6,3.5])
	
	
