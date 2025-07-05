#Problem:  https://leetcode.com/problems/find-lucky-integer-in-an-array/
#Code Written in python
class Solution(object):
    def findLucky(self, arr):
        L=[]
        for i in set(arr):
            if arr.count(i)==i:
                L.append(i)
        if L==[] :
            return(-1)
        else:
            return(max(L))
    #Get the input
    #call the function

#Found the lucky integer
   
