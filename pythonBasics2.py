# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code. Make sure to add what is going to be returned.


# Part A. count_threes
# Define a function count_threes(n) that takes an int and
# returns the number of multiples of 3 in the range from 0
# to n (including n).

def count_threes(n):
    # YOUR CODE HERE

    return int(n) / 3


# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that takes
# a string s and returns the character that has the longest consecutive repeat.
def longest_consecutive_repeating_char(a):
    # YOUR CODE HERE
    n = len(a)
    ctr = 1
    mx = 1
    ch = a[0]
    for i in range(0,n-1):
        if a[i] ==a[i+1]:
            ctr += 1

        else:
            if ctr > mx:
                mx = ctr 
                ch = a[i]
            ctr = 1
    if ctr > mx:
        mx = ctr
        ch = a[i]
    return ch



# Part C. is_palindrome
# Define a function is_palindrome(s) that takes a string s
# and returns whether or not that string is a palindrome.
# A palindrome is a string that reads the same backwards and
# forwards. Treat capital letters the same as lowercase ones
# and ignore spaces (i.e. case insensitive).
def is_palindrome(s):
    # YOUR CODE HERE
    i = 0
    j = len(s)-1
    while i <= j:
        if s[i] == ' ':
            i += 1
            continue
        if s[j] == ' ':
            j -= 1
            continue
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True
