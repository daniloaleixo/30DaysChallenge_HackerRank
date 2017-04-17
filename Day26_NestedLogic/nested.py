# Objective 
# Today's challenge puts your understanding of nested conditional statements to the test. You already have the knowledge to complete this challenge, but check out the Tutorial tab for a video on testing!

# Task 
# Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine (if any). The fee structure is as follows:

# If the book is returned on or before the expected return date, no fine will be charged (i.e.: .
# If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, .
# If the book is returned after the expected return month but still within the same calendar year as the expected return date, the .
# If the book is returned after the calendar year in which it was expected, there is a fixed fine of .
# Input Format

# The first line contains  space-separated integers denoting the respective , , and  on which the book was actually returned. 
# The second line contains  space-separated integers denoting the respective , , and  on which the book was expected to be returned (due date).

# Constraints

# Output Format

# Print a single integer denoting the library fine for the book received as input.

# Sample Input

# 9 6 2015
# 6 6 2015
# Sample Output

# 45


import datetime
    
def calc_fine(due, turn_in):
    if turn_in <= due:
        return 0
    else:
        if turn_in.year == due.year:
            if turn_in.month == due.month:
                return 15 * (turn_in.day - due.day)
            else:
                return 500 * (turn_in.month - due.month)
        else:
            return 10000

trn_d, trn_m, trn_y = [int(x) for x in input().split()]
due_d, due_m, due_y = [int(x) for x in input().split()]
trn_y += 1900  #strptime doesnt handle years below 1900
due_y += 1900 

due = datetime.datetime.strptime("{} {} {}".format(due_d, due_m, due_y ), "%d %m %Y")
turn_in = datetime.datetime.strptime("{} {} {}".format(trn_d, trn_m, trn_y ), "%d %m %Y")
print( calc_fine(due, turn_in))