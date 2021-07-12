#Given a signed 32-bit integer x, return x with its digits reversed. 
#If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then #return 0.

#Example 1:

#Input: x = 123
#Output: 321
#Example 2:

#Input: x = -123
#Output: -321
#Example 3:

#Input: x = 120
#Output: 21
#Example 4:

#Input: x = 0
#Output: 0 

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 2**31-1 or x <= -2**31:
            return 0
        else:
            stack = []
            n = ""
            if x == 0:
                return 0
            else:
                while x%10 == 0:
                    x = x/10
        
            for digit in str(x):
                if digit == '-':
                    n = n + '-'
                else:
                    stack.append(int(digit))
        
            for i in range(len(stack)):
                n = n + str(stack.pop())
            
            n = int(n)
            if n >= 2**31-1 or n <= -2**31:
                return 0
       # if n[0] == '0':
        #    if len(n) == 1:
         #       pass
          # else:
           #     n = n[1:]
       # for i in range(2,len(n)):
        #    if len(n) > 1:
         #       if n[i-1] == '0':
          #          if n[0] == '-':
           #             n = n[:i-1] + n[i:]
            #        else:
             #           pass
              #  else:
               #     break
           
        return n