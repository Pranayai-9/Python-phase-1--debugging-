#FizzBuzz problem - LeetCode 412
class Solution(object):
    def fizzBuzz(self, n):
        final = []
        for i in range(1,n+1):
            final.append(str(i))
        
        for i in range(len(final)):
        
            if int(final[i]) % 3 == 0 and int(final[i]) % 5 == 0:
                final[i] = "FizzBuzz"
            elif int(final[i]) % 3 == 0:
                final[i] = "Fizz"
            elif int(final[i]) % 5 == 0:
                final[i] = "Buzz"
          
                
        return final

