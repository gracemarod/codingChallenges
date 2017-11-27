'''Given a string, S , of lowercase letters, determine the index of the character whose removal 
will make  a palindrome. If  is already a palindrome or no such character exists, then print S. 
There will always be a valid solution, and any correct answer is acceptable. 
For example, if  "bcbc", we can either remove 'b' at index  or 'c' at index .'''

import sys

#Make new string by deleting letter of index given. Return true if new string
#equals reversed new string.
def isPalindrome(index,s):
    newStr = s[0:index] + s[index+1:len(s)]
    if newStr == newStr[::-1]:
        return True
    else:
        return False

def palindromeIndex(s):
   
    #setting indexes for beginning and end of string   
    low = 0
    high = len(s)-1
    
    if s == s[::-1]:
        return -1
    
    while(low<high):
        if s[low] == s[high]:
            low+=1
            high-=1

        else:
            #If removing str[low] makes the new string a palindrome, return index low
            if(isPalindrome(low,s)):
                return low
            #Else if removing str[high] makes a palindrome return index high
            elif(isPalindrome(high,s)):
                return high
            
s1 = "hgygsvlfcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnwcwflvsgygh"
print palindromeIndex(s1)
s2 = "quyjjdcgsvvsgcdjjyq"
print palindromeIndex(s2)

    