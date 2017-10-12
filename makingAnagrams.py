'''Alice is taking a cryptography class and finding anagrams to be very useful. 
We consider two strings to be anagrams of each other if the first string's letters can 
be rearranged to form the second string. In other words, both strings must contain the 
same exact letters in the same exact frequency For example, bacdc and dcbac are anagrams, 
but bacdc and dcbad are not.

Alice decides on an encryption scheme involving two large strings where encryption is dependent 
on the minimum number of character deletions required to make the two strings anagrams. 
Can you help her find this number?

Given two strings,  and , that may or may not be of the same length, determine the minimum number 
of character deletions required to make  and  anagrams. Any characters can be deleted from either of the strings.

Input Format:
The first line contains a single string, a. 
The second line contains a single string, b.

Constraints:
1 <= |a|, |b| <= 10^4
It is guaranteed that a and b consist of lowercase English alphabetic letters 
(i.e.,  through ).

Output format: 
Print a single integer denoting the number of characters you must delete to make 
the two strings anagrams of each other.

Problem taken from https://www.hackerrank.com/challenges/ctci-making-anagrams'''

from collections import Counter
from collections import OrderedDict
import string
lenAlpha = 26

def number_needed(a, b):
    
    countA = OrderedDict(sorted(dict.fromkeys(string.ascii_lowercase,0).items()))
    countB = OrderedDict(sorted(dict.fromkeys(string.ascii_lowercase,0).items()))
    
    total = 0
    
    for key in countA.keys():
        if key in a:
            countA[key] = a.count(key)

    for k in countB.keys():
        if k in b:
            countB[k] = b.count(k)
            
    for i in range(0,len(countA)):
        total += abs( countA.values()[i] - countB.values()[i])
    
    
    return total
    
a = "cde"
b = "abc"

print number_needed(a, b)

#Output: 4
