#to find the largest odd number that can be obtained by removing digits only from the end.
def largestOddNumbers(s: str) -> str:
    for i in range(len(s) -1, -1, -1):
        if int(s[i]) % 2 !=0: #check whether the digit is odd
                              #s[i] gets the digit at position i
            return s[:i + 1]
    return ""
"""
s = "214638"
the length of s is 6
therefore range(5,-1,-1) #our loop starts at index 5
the values of i will be 5,4,3,2,1,0
"""
"""
for i in range(len(s) -1, -1, -1): #len(s) - 1, len(6) -1 because last character's index is 5
                                   #so 6 - 1 = 5
                                   #now it becomes range(5, -1, -1)
#-1 because que asked you to start from the last digit
"""
"""
if int(s[i]) % 2 !=0: #s[i] character at index 
                      #s = "214638"
                      #i = 5
                      #s[5] = 8
"""
"""
return s[:i + 1] #return s[:4 + 1]
                 #return s[:5] this is called string slicing
                 #s[start:end]
                 #i + 1  We want to include that digit in our answer.
                  Therefore, we use:s[:i + 1]
#If the digit you want to include is at index i, use i + 1 as the ending index in the slice.                  
for eg 
s = "214638"
print(s[:5])
21463
"""
