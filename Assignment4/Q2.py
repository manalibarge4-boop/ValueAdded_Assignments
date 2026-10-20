#Q Second highest occuring element
#arr = [1, 2, 2, 3, 3, 3]
def secondHighestOccurringElement(arr):
    freq = {}

    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1 
    #dict created freq = {1 : 1, 2 : 2, 3: 3}        
    #collect the different frequency
    counts = [] #create an empty list

    for num in freq: #num = 1
        if freq[num] not in counts: #if 1 not in counts
                                    #because count is empty, the cond is true
            counts.append(freq[num])#therefore counts.append(1)
                                    #now counts = [1]
    counts.sort(reverse=True) #this arrange them from highest to lowest

    if len(counts) < 2:
        return -1

    second_count = counts[1] #because indexing starts at 0 highest = 1, second highest = 1 
    result = None

    for num in freq:
        if freq[num] == second_count:
            if result is None or num < result:
                result = num

    return result

"""
#2nd iteration  (freq[2] is 2)
for num in freq: #num = 2
        if freq[num] not in counts: #if 2 not in counts
                                    #because count has only 1, the cond is true
            counts.append(freq[num])#therefore counts.append(2)
                                    #now counts = [1, 2]
    counts.sort(reverse=True)
"""
"""
#3rd iteration  (freq[3] is 3)
for num in freq: #num = 3
        if freq[num] not in counts: #if 3 not in counts
                                    #because count has only 1 and 2, the cond is true
            counts.append(freq[num])#therefore counts.append(3)
                                    #now counts = [1, 2, 3]
    counts.sort(reverse=True) 
"""    