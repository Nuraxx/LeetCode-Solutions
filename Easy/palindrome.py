class Solution(object):
    def isPalindrome(self, x):
        return(str(x)==str(x)[::-1]) # checking is the string of the number is equal to the string of the number in reverse (using string slicing)

#get inputs
# time complexity : o(n)
# space complexity : o(n)
