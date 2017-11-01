'''
Given the value of  and the cost of each flavor for t trips to the Ice Cream Parlor, 
help Sunny and Johnny choose two distinct flavors such that they spend their entire pool of
money during each visit. 

EXAMPLE:
Input: m(target) = 4, a = 1 4 5 3 2 
output: 1 4

Explanation ice cream #1 cost $1 and ice cream#2 cost $3, so its sum is 1+3 = 4'''

m = 4
a = [1,4,5,3,2]
    
menuHash = {}
result = ()

# We go through the ice cream menu once, and calculating the complement by subtracting
# the target with the current element. If the complement is on the list, then we already have 
# our answer. If not, we keep filling the hash with the cost of the current ice cream as key 
# and the index as its value.

for i in range(0, len(a)):
    complement = m - a[i]
    if complement in menuHash.keys():
        result = menuHash[complement], i+1
    menuHash[a[i]] = i+1
    
for j in result:
    print j,
print