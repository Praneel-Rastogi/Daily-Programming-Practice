#Given an integer x, return true if x is palindrome integer.

#An integer is a palindrome when it reads the same backward as forward. For example, 121 is
# palindrome while 123 is not

 

#Example 1:

#Input: x = 121
#Output: true
#Example 2:

#Input: x = -121
#Output: false
#Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore 
#it is not a palindrome.
#Example 3:

#Input: x = 10
#Output: false

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        a = str(x)
        if a == a[::-1]:
            return True
        else:
            return False
            
        
      #  list = []
       # n = ''
        #for digit in str(x):
         #   if digit == '-':
          #      return False
           # else:
            #   list.append(int(digit))
            
        #for i in range(len(list)):
         #   n = n + str(list.pop())
            
        #if n == str(x):
         #   return True
        #else:
         #   return False
