# Objective 
# Today we're expanding our knowledge of Strings and combining it with what we've already learned about loops. Check out the Tutorial tab for learning materials and an instructional video!

# Task 
# Given a string, , of length  that is indexed from  to , print its even-indexed and odd-indexed characters as  space-separated strings on a single line (see the Sample below for more detail).

# Note:  is considered to be an even index.

# Input Format

# The first line contains an integer,  (the number of test cases). 
# Each line  of the  subsequent lines contain a String, .

# Constraints

# Output Format

# For each String  (where ), print 's even-indexed characters, followed by a space, followed by 's odd-indexed characters.

# Sample Input

# 2
# Hacker
# Rank
# Sample Output

# Hce akr
# Rn ak

n = int(raw_input())

array_str = []

for i in range(0, n):
	array_str.append(str(raw_input()))

for i in range(0, n):
	string_odd = ''
	string_even = ''
	for j in range(0, len(array_str[i]), 2):
		string_even = string_even + array_str[i][j]
	for j in range(1, len(array_str[i]), 2):
		string_odd = string_odd + array_str[i][j]

	print string_even, string_odd