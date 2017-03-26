# Objective 
# Today, we're working with binary numbers. Check out the Tutorial tab for learning materials and an instructional video!

# Task 
# Given a base- integer, , convert it to binary (base-). Then find and print the base- integer denoting the maximum number of consecutive 's in 's binary representation.

# Input Format

# A single integer, .

# Constraints

# Output Format

# Print a single base- integer denoting the maximum number of consecutive 's in the binary representation of .

# Sample Input 1

# 5
# Sample Output 1

# 1
# Sample Input 2

# 13
# Sample Output 2

# 2

n = int(raw_input().strip())
n_bin = bin(n)

longest_streak = 0
current_streak = 0


for i in range(2, len(n_bin)):
	# print n_bin[i]

	if current_streak > longest_streak:
		longest_streak = current_streak


	if int(n_bin[i]) == 1:
		current_streak = current_streak + 1
	else:
		current_streak = 0


if int(n_bin[len(n_bin) - 1]) == 1: 
	if current_streak > longest_streak:
		longest_streak = current_streak

print longest_streak