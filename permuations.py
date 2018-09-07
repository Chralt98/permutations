import re


def dospace(array):
    digity = re.compile(r'^\d$')
    for j in range(0, len(array)):
        if digity.search(array[j]):
            array[j] = ' ' + array[j]


row = input("Geben Sie ihre Zahlenreihe mit Komma getrennt ein (Input a permutation number line divided by comma.): \n")
beforeArray = []
firstArray = []
afterArray = row.split(',')
identity = False
# fill beforeArray with [1..n]
digit = re.compile(r'^\d$')
for i in range(0, len(afterArray)):
    beforeArray.append(str(i + 1))
    firstArray.append(str(i + 1))
dospace(firstArray)
dospace(beforeArray)
dospace(afterArray)
print(beforeArray)
num = 0
newNum = 0
n = 0
zyklen = []
# Beispielpermutation / example permutation: 5,3,2,4,1,8,6,7,9
while not identity:
    n = n + 1
    cache = []
    for i in range(0, len(afterArray)):
        num = int(beforeArray[i])
        newNum = int(afterArray[num-1])
        cache.append(str(newNum))
    dospace(cache)
    print(cache)
    beforeArray = cache
    if cache == firstArray:
        identity = True
        print("Ordnung (Order): "+str(n))
# Another example input: 13,12,11,4,7,15,6,2,8,3,5,1,9,14,10
