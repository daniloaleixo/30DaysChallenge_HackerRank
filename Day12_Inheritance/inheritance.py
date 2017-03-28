# Objective 
# Today, we're delving into Inheritance. Check out the Tutorial tab for learning materials and an instructional video!

# Task 
# You are given two classes, Person and Student, where Person is the base class and Student is the derived class. Completed code for Person and a declaration for Student are provided for you in the editor. Observe that Student inherits all the properties of Person.

# Complete the Student class by writing the following:

# A Student class constructor, which has  parameters:
# A string, .
# A string, .
# An integer, .
# An integer array (or vector) of test scores, .
# A char calculate() method that calculates a Student object's average and returns the grade character representative of their calculated average:
# Grading.png

# Input Format

# The locked stub code in your editor calls your Student class constructor and passes it the necessary arguments. It also calls the calculate method (which takes no arguments).

# You are not responsible for reading the following input from stdin: 
# The first line contains , , and , respectively. The second line contains the number of test scores. The third line of space-separated integers describes .

# Constraints

# Output Format

# This is handled by the locked stub code in your editor. Your output will be correct if your Student class constructor and calculate() method are properly implemented.

# Sample Input

# Heraldo Memelli 8135627
# 2
# 100 80
# Sample Output

#  Name: Memelli, Heraldo
#  ID: 8135627
#  Grade: O

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print "Name:", self.lastName + ",", self.firstName
		print "ID:", self.idNumber

class Student(Person):

    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
    	self.firstName = firstName;
    	self.lastName = lastName;
    	self.idNumber = idNumber;
    	self.scores = scores;

    

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
    	return self.average(sum(self.scores)/len(self.scores))

    def average(self, grade):
    	if grade <= 100 and grade >= 90:
    		return 'O'
    	elif grade < 90 and grade >= 80:
    		return 'E'
    	elif grade < 80 and grade >= 70:
    		return 'A'
    	elif grade < 70 and grade >= 55:
    		return 'P'
    	elif grade < 55 and grade >= 40:
    		return 'D'
    	else: 
    		return 'T'




line = raw_input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(raw_input()) # not needed for Python
scores = map(int, raw_input().split())
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print "Grade:", s.calculate()