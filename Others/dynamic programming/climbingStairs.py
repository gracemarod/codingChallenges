'''You are climbing a staircase that has n steps. You can take the steps either 1 or 2 at a time. 
Calculate how many distinct ways you can climb to the top of the staircase.
Recovered from https://codefights.com/interview-practice/task/oJXTWuwEZiC6FTw3A'''

def climbingStairs(n):
        count = 0
        #Go through the bases cases first.
        # if n = 0, there are no steps to climb
        # for n = 1, there's only one step to climb
        # for 2 steps, you can either climb 2 steps at once or 1 step two times
        # so return 2
        if n<=2:
                return n
        else:
                #make array to store fib values
                table = [0 for x in range(n+1)] 
                #save base cases values
                table[0]=0 
                table[1]=1
                table[2]=2
                
                for i in range(2,n):
                        #calculate fibonnaci in each iteration
                        table[i] = table[i-1] + table[i-2]
                        count += table[i]
 
        return count+2

