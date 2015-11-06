__author__ = 'Deepak'
uniqueList = []
blackList = []
testList = [1,2,3,2,2,2,3,2,3]
newList = []

def removeDuplicates():
    x = 0
    while x < len(testList):
        if testList[x] in uniqueList:
            blackList.append(x)
        else:
            uniqueList.append(testList[x])
        x = x+1

    y = 0
    while y < len(testList):
        if y not in blackList:
         newList.append(testList[y])
        y = y+1



    return newList




print(removeDuplicates())
print(uniqueList)
print(blackList)

