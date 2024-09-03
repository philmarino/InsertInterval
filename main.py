#I realize this doesn't meet the problem description, but I like my question/answer better as the unique intervals after the new interval is introduced.

def insert(intervals, newInterval):
    tempList = []
    for interval in intervals:
        for i in range(interval[0], interval[1] + 1): #add one since range is exclusive of the stop parameter
            tempList.append(i)
    for i in range(newInterval[0], newInterval[1] + 1): #add one since range is exclusive of the stop parameter
        tempList.append(i)

    #now all the nummbers are in the templist
    tempList = list(set(tempList)) #removes duplicates
    tempList.sort()
    #print(tempList)
    currentInterval = []
    previousValue = -1
    retList = []
    #return tempList
    for i in range(len(tempList)):
        if currentInterval == []:
            currentInterval.append(tempList[i])
            previousValue = tempList[i]
            continue
        if tempList[i] == previousValue + 1:
            previousValue = previousValue + 1
        else:
            currentInterval.append(previousValue)
            retList.append(currentInterval)
            currentInterval = [tempList[i]]
            previousValue = tempList[i]
    if currentInterval != []:
        currentInterval.append(tempList[i])
        retList.append(currentInterval)

    return retList


# Example 1:
# Input: 
intervals = [[1,3],[6,9]]
newInterval = [2,5]
print(insert(intervals, newInterval))
# Output: [[1,5],[6,9]]

# Example 2:
# Input: 
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
print(insert(intervals, newInterval))
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
