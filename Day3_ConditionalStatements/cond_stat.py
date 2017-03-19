# Task 
# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird
# Complete the stub code provided in your editor to print whether or not  is weird.

# Input Format

# A single line containing a positive integer, .

# Constraints

# Output Format

# Print Weird if the number is weird; otherwise, print Not Weird.

# Sample Input 0

# 3
# Sample Output 0

# Weird
# Sample Input 1

# 24
# Sample Output 1

# Not Weird

N = int(raw_input().strip())

if N % 2 == 1: print 'Weird'
else:
	if N >=2 and N <= 5: print 'Not Weird'
	elif N >= 6 and N <= 20: print 'Weird'
	elif N > 20: print 'Not Weird'

