#!/bin/python


# Objective 
# Today, we're getting started with Exceptions by learning how to parse an integer from a string and print a custom error message. Check out the Tutorial tab for learning materials and an instructional video!

# Task 
# Read a string, , and print its integer value; if  cannot be converted to an integer, print Bad String.

# Note: You must use the String-to-Integer and exception handling constructs built into your submission language. If you attempt to use loops/conditional statements, you will get a  score.

# Input Format

# A single string, .

# Constraints

# , where  is the length of string .
#  is composed of either lowercase letters () or decimal digits ().
# Output Format

# Print the parsed integer value of , or Bad String if  cannot be converted to an integer.

# Sample Input 0

# 3
# Sample Output 0

# 3
# Sample Input 1

# za
# Sample Output 1

# Bad String


import sys


S = raw_input().strip()

try:
	print int(S)
except ValueError:
	print 'Bad String'


	