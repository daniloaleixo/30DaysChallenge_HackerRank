# Objective 
# Today we're discussing scope. Check out the Tutorial tab for learning materials and an instructional video!

# The absolute difference between two integers,  and , is written as . The maximum absolute difference between two integers in a set of positive integers, , is the largest absolute difference between any two integers in .

# The Difference class is started for you in the editor. It has a private integer array () for storing  non-negative integers, and a public integer () for storing the maximum absolute difference.

# Task 
# Complete the Difference class by writing the following:

# A class constructor that takes an array of integers as a parameter and saves it to the  instance variable.
# A computeDifference method that finds the maximum absolute difference between any  numbers in  and stores it in the  instance variable.
# Input Format

# You are not responsible for reading any input from stdin. The locked Solution class in your editor reads in  lines of input; the first line contains , and the second line describes the  array.

# Constraints

# , where 
# Output Format

# You are not responsible for printing any output; the Solution class will print the value of the  instance variable.

# Sample Input

# 3
# 1 2 5
# Sample Output

# 4


class Difference:
	def __init__(self, a):
		self.__elements = a

	def fabs(self, x):
		return x if x > 0 else int(x * -1)

	def computeDifference(self):
		sorted_arr = sorted(self.__elements)

		maximumDifference = 0
		if len(sorted_arr) >= 2:
			min_value = sorted_arr[0]
			min_2_value = sorted_arr[1]
			max_value = sorted_arr[len(sorted_arr) - 1]
			max_2_value = sorted_arr[len(sorted_arr) - 2]

			if self.fabs(min_value - min_2_value) > maximumDifference:
				maximumDifference = self.fabs(min_value - min_2_value)
			if self.fabs(min_value - max_value) > maximumDifference:
				maximumDifference = self.fabs(min_value - max_value)
			if self.fabs(min_value - max_2_value) > maximumDifference:
				maximumDifference = self.fabs(min_value - max_2_value)
			if self.fabs(min_2_value - max_value) > maximumDifference:
				maximumDifference = self.fabs(min_2_value - max_value)
			if self.fabs(min_2_value - max_2_value) > maximumDifference:
				maximumDifference = self.fabs(min_2_value - max_2_value)
			if self.fabs(max_value - max_2_value) > maximumDifference:
				maximumDifference = self.fabs(max_value - max_2_value)


		self.maximumDifference = maximumDifference


# End of Difference class

_ = raw_input()
a = [int(e) for e in raw_input().split(' ')]

d = Difference(a)
d.computeDifference()

print d.maximumDifference