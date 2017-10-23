'''Given n strings of brackets, determine whether each sequence of brackets is balanced. If a string is balanced, print YES on a new line; otherwise, print NO on a new line.

Input Format
The first line contains a single integer,n, denoting the number of strings. 
Each line i of the n subsequent lines consists of a single string, , denoting a sequence of brackets.

Output Format
For each string, print whether or not the string of brackets is balanced on a new line. If the brackets are balanced, print YES; otherwise, print NO.

Sample Input
3
{[()]}
{[(])}
{{[[(())]]}}

Sample Output
YES
NO
YES

Coding challenge recovered from https://www.hackerrank.com/challenges/ctci-balanced-brackets
'''
#Make the Stack. Can be done with a simple list but it's good to practice Classes
class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self,element):
        self.items.append(element)
    def pop(self):
        self.items.pop()
    def see(self):
        return self.items[len(self.items)-1]
    def seeAll(self):
        return self.items
    def size(self):
        return len(self.items)

def is_matched(expression):
    newStack =  Stack()
    
    #print "Input: ", expression
    #Check for cases where the first character is a closing bracket
    if expression[0] == ")" or expression[0] == "]" or expression[0] == "}":
        return False
    
    for i in expression:
        #print "Current: ", i
        #If it's a closing bracket, push into stack
        if i == "{" or i == "(" or i == "[":
            newStack.push(i)
        elif newStack.size() > 0:
            #Look for opening and closing  brackets and pop
            if i == "}":
                if newStack.see() == "{":
                    newStack.pop()
            #If not, means there's a single closing bracket so it's False
                else:
                    return False
            elif i == ")":
                if newStack.see() == "(":
                    newStack.pop()
                else:
                    return False
            elif i == "]":
                if newStack.see() == "[":
                    newStack.pop()
                else:
                    return False

    if newStack.size() == 0:
        return True
    return False

t = int(raw_input().strip())
for a0 in xrange(t):
    print "Write the number of expressions followed by the expressions as a string: "
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"