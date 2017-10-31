
'''
Author: ADEMOLA HUSSAIN
Email address: demola.hussainin@gmail.com
Phone number: +2348039539268
Date: 17 June, 2017
Time: 3:30 P.M.
'''

'''
	Question 1:
	Write a program which will find all such numbers which are divisible by 7 but are not a multiple
	of 5,
	between 2000 and 3200 (both included).
	The numbers obtained should be printed in a comma-separated sequence on a single line from
	the largest to the smallest.
'''
def questionOne():			#declare function questionOne
	maximumNumber = 3200	#declare variable maximumNumber
	minimumNumber = 2000	#declare variable minimumNumber
	for i in range (maximumNumber, minimumNumber-1, -1) :	#loop through, within the range of maximumNumber and minimumNumber
		if ( (i % 7 == 0) and (i % 5 != 0) ):			    #check if number is divisible by 7 and not a multiple of 5
			print (str(i)+','),							    #print number that passes above test on a single line
	return												    #returns contol back to the calling function
questionOne()

'''
Question 2:
Write a recursive function/program which can compute the factorial of a given number from the
console.
The result should be a tuple of the answer and a dictionary of the number of digit(s) occurrence.
Suppose the following input is supplied to the program:
8
Then, the output should be a the number and a dictionary that counts the number of occurrence
of each digits :
(40320, {4: 1, 0: 2, 3: 1, 2:1})
'''
 
def questionTwo():						#declare function questionOne
	def factorial(number):				#declare function factorial
		if (number<=0):					#check if number is lessthan or equal to zero so as to ensure a valid input
			print 'Cannot find factorial of '+str(number)	#Tells the user an invalid input has been entered
		elif (number == 1):									#checks for the base case i.e. if number is eaqual to one
			return 1										#return a value '1' when the base case is reached
		else:
			return number*factorial(number-1)				#returnsa simplified version of the original problem
	number = int(input('Enter a number: '))					#Asks for input from the user and converts it to an integer
	result = str((factorial(number)))						#Converts the number returned by the factorial function to a string
	numberOfOccurrence = dict()								#creates an empty dictionary object
	for i in range(len(result)):							#loops through the string
		numberOfOccurrence[int(result[i])] = result.count(result[i]) 
	print ( factorial(number), numberOfOccurrence )			#Prints a tuple of the factorial of a number and the occurrance of each number 
	return													#returns contol back to the calling function 
questionTwo()

'''
Question 3:
With a given integral number n, write a program to generate a dictionary that contains (i, i*i)
such that is an integral number between 1 and n (both included), and then the program should
print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

'''

def questionThree():				#declare function questionThree
	result = dict()					#declare an empty dictionary object
	number = int(input('Enter a number: '))		#Asks user for input and converts to a string
	for i in range(1,number+1):					#loops through the range betwen '1' and the input
		result[i] = i*i							#assigns a key:value pair to the dictionary
	print result								#prints the dictionary
	return										#returns contol back to the calling function
questionThree()













