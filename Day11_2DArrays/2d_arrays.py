# Objective 
# Today, we're building on our knowledge of Arrays by adding another dimension. Check out the Tutorial tab for learning materials and an instructional video!

# Context 
# Given a  2D Array, :

# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# We define an hourglass in  to be a subset of values with indices falling in this pattern in 's graphical representation:

# a b c
#   d
# e f g
# There are  hourglasses in , and an hourglass sum is the sum of an hourglass' values.

# Task 
# Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum.

# Input Format

# There are  lines of input, where each line contains  space-separated integers describing 2D Array ; every value in  will be in the inclusive range of  to .

# Constraints

# Output Format

# Print the largest (maximum) hourglass sum found in .

# Sample Input

# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 2 4 4 0
# 0 0 0 2 0 0
# 0 0 1 2 4 0
# Sample Output

# 19

arr = []
for arr_i in xrange(6):
   arr_temp = map(int,raw_input().strip().split(' '))
   arr.append(arr_temp)

largest_sum = -10 * 7
current_sum = 0

for i in range(1, 5):
	for j in range(1, 5):
		current_sum = arr[i][j] + arr[i-1][ j-1] + arr[i-1][ j] + arr[i-1][ j+1]  + arr[i+1][ j-1] + arr[i+1][ j] + arr[i+1][ j+1]
		print current_sum
		if current_sum > largest_sum:
			largest_sum = current_sum

print largest_sum