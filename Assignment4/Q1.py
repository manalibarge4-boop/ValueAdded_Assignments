#Q highest occuring element in an array
#for [2, 2, 5, 5, 5]
def highestOccurringElement(nums):
    freq = {}  #creates an empty dictionary to store the number and its frequency in key:value pair
    for n in nums: #to go through all the numbers presented
        if n in freq: # first iteration n=2, since 2 isnt in dict, conditionj will false
            freq[n] += 1 #here this square brackets let us access a value associated with particular key in a dictionary ,, dictionary[key]
        else:          #since the condition is false python executes else 
            freq[n] = 1 #therefore freq[2] = 1, so dict is now freq = {2 : 1}
                        #we have stored the number 2 and its frequency is 1
    max_count = 0   #start with max freq of 0
    result = nums[0] #initially assume the first element is the answer 
    for n in freq:   #visit each number in the frequency dictionary
        if freq[n] > max_count: #did we find a higher frequency?
            max_count = freq[n] #save the new highest frequency
            result = n          #save the number that has this frequency
        elif freq[n] == max_count and n < result: #does the numbers have the same high freq?
                                                  # is this number smaller than our current answer?
            result = n    #if both conditions are true, choose the smaller number
    return result   #send back the final answer

"""
#2nd iteration
freq = {2 : 1} #by first iteration now dictionary has stored the n which is 2 and there freq 1  
    for n in nums: 
        if n in freq: # since n which is 2 is already exist, the condition is true
            freq[n] += 1 #python executes this because n = 2, this become freq[n] += 1, so the frequency increases from 1 to 2
                         #now our dictionary becomefreq = {2 : 2}
        else:           
            freq[n] = 1 
"""
"""
#3rd iteration
freq = {2 : 2} #by second iteration now dictionary has stored the n which is 2 and there freq 2 
    for n in nums:  #n = 5
        if n in freq: # since n which is 5 isnt exist, the condition is false
            freq[n] += 1 
        else:           #since condition is false it executes else 
            freq[n] = 1 #therefore freq[5] = 1,, so dict is now freq = {2 : 2, 5 : 1}
"""
"""
#4th iteration
freq = {2 : 2, 5 : 1} #by third iteration 
    for n in nums:  #n = 5
        if n in freq: # since n which is 5 does exist in dict, the condition is true
            freq[n] += 1 # freq[5] += 1, so it becomes 5 : 2,, {2 : 2, 5 : 2}
        else:            
            freq[n] = 1 
"""
#and so on iterations moves
#this means 2 appears twice and 5 appears three times
"""
#now to find the number that occurs the most times
max_count = 0 #create a variable to track the highest frequency found so far,, initially starting maximum is 0
result = nums[0] 
"""
"""
nums = [4, 4, 2, 2, 2, 7, 7]
after counting, dictionary becomes freq = {4 : 2, 2 : 3, 7 : 2}
now we have to find the number with highest frequency, ans is 2

max_count = 0 #create a variable to track the highest frequency found so far,, initially starting maximum is 0
              #as we check dict, this value may change max_count = 0, 2, 3
              #stores the highest frequency found so far 
              #max_count stores a frequency, not a number from the original list
result = nums[0] #index of nums[0] is 4 result = 4
                 #we need a variable to store our current best answer, it stores the number currently considered the answer.
                 #initially we use the first element as our starting answer, as we examine the frequencies we'll update result whenever we find better ans
                 #for now we found for but letter we discover 2 has high, then we change it 
#both are related but stores different things
 for n in freq: #loops the dict keys, visit each number in freq dict
        if freq[n] > max_count: #if frequency of current number is greater than the highesr frequency we found
                                #freq[4] = 2, max_count = 0,, if 2 > 0
                                #condition true
            max_count = freq[n] #now max_count = freq[4], so max_count = 2
            result = n  # also need to remember which number produced that frequency
                        # result = 4
                        #our variables now contain max_count = 2, result = 4
        elif freq[n] == max_count and n < result:
            result = n    
    return result
"""

"""
#now we encounter 2 whose frequency is 3
for n in freq: #loops the dict keys, visit each number in the freq dict
        if freq[n] > max_count: #if freq[2] = 3 > max_count
                                #if 3 > 2 which is true
            max_count = freq[n]  #so max_count = 3
            result = n           #result = 2
        elif freq[n] == max_count and n < result:
            result = n    
    return result
"""
"""
#now we encounter 7 whose frequency is 2 (which is lower than previous one)
for n in freq: #loops the dict keys, visit each number in freq dict
        if freq[n] > max_count: #if freq[7] > max_count
                                #if 2 > 3 which is false
            max_count = freq[n]  
            result = n           
        elif freq[n] == max_count and n < result: #this line handles situation where two or more numbers have the same high freq
            result = n    
    return result
"""
    