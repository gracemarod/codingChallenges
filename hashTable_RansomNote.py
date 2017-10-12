'''A kidnapper wrote a ransom note but is worried it will be traced back to him. 
He found a magazine and wants to know if he can cut out whole words from it and use 
them to create an untraceable replica of his ransom note. The words in his note are 
case-sensitive and he must use whole words available in the magazine, meaning he cannot 
use substrings or concatenation to create the words he needs.

Given the words in the magazine and the words in the ransom note, 
print Yes if he can replicate his ransom note exactly using whole words from the magazine; otherwise, print No.

Input Format:
The first line contains two space-separated integers describing the respective values of m 
(the number of words in the magazine) and n (the number of words in the ransom note). 
The second line contains m space-separated strings denoting the words present in the magazine. 
The third line contains n space-separated strings denoting the words present in the ransom note.

Constrains: 
1<=m,n<=3000
1<= length of any word <=5
Each word consists of English alphabetic Letters
The words in the note and magazine are care-sensitive'''

from collections import Counter
from collections import OrderedDict

def ransom_note(magazine, ransom):
    result = True
    
    magazineString = Counter(magazine)
    ransomString = Counter(ransom)
    
    
    for key,value in ransomString.items():
        if key not in magazineString:
            result = False
        else:
            if(value > magazineString[key]):
                result = False
       
    return result        
    

m, n = 6,5
magazine = "two times three is not four"
ransom = "two times two is four"
answer = ransom_note(magazine, ransom)
if(answer):
    print "Yes"
else:
    print "No"

#Output: No
